#!/usr/bin/env python3
"""
Fetch China futures main-contract daily bars for a target trade date.

Examples:
    python fetch_futures_daily.py --date 2026-03-05 --symbol aum
    python fetch_futures_daily.py --date 2026-03-05 --symbol aum,cum,rbm
    python fetch_futures_daily.py --date 2026-03-05 --symbol 沪金,RB0
    python fetch_futures_daily.py --list-symbols
    python fetch_futures_daily.py --list-symbols --keyword 螺纹
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    import akshare as ak
    import pandas as pd
except ModuleNotFoundError as exc:
    missing = exc.name or "dependency"
    print(
        json.dumps(
            {
                "error": f"Missing Python package: {missing}",
                "hint": "Run: python -m pip install akshare pandas",
            },
            ensure_ascii=False,
            indent=2,
        ),
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


SCRIPT_DIR = Path(__file__).resolve().parent
SYMBOLS_PATH = SCRIPT_DIR / "futures_symbols.json"
COLUMN_MAP = {
    "日期": "trade_date",
    "开盘价": "open_price",
    "最高价": "high_price",
    "最低价": "low_price",
    "收盘价": "close_price",
    "成交量": "volume",
    "持仓量": "open_interest",
}


def load_symbols() -> Dict[str, Dict[str, str]]:
    return json.loads(SYMBOLS_PATH.read_text(encoding="utf-8"))


def normalize_trade_date(value: str) -> str:
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError as exc:
        raise SystemExit("`--date` must use YYYY-MM-DD, for example 2026-03-05") from exc


def build_alias_map(symbols: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    aliases: Dict[str, str] = {}
    for symbol, cfg in symbols.items():
        api_symbol = cfg["api_symbol"].lower()
        name = cfg["name"]
        base_name = name.removesuffix("主连")
        aliases[symbol.lower()] = symbol
        aliases[api_symbol] = symbol
        aliases[api_symbol.removesuffix("0")] = symbol
        aliases[name.lower()] = symbol
        aliases[base_name.lower()] = symbol
    return aliases


def parse_symbols(raw_symbols: str) -> List[str]:
    return [item.strip() for item in raw_symbols.split(",") if item.strip()]


def resolve_symbols(
    raw_symbols: Iterable[str],
    symbols: Dict[str, Dict[str, str]],
) -> List[Tuple[str, str, Dict[str, str]]]:
    alias_map = build_alias_map(symbols)
    resolved: List[Tuple[str, str, Dict[str, str]]] = []
    seen = set()

    for raw_symbol in raw_symbols:
        key = raw_symbol.strip().lower()
        canonical = alias_map.get(key)
        if not canonical:
            supported = ", ".join(list(sorted(symbols))[:12])
            raise SystemExit(
                f"Unsupported symbol `{raw_symbol}`. "
                f"Use `--list-symbols` to inspect the mapping. Examples: {supported}..."
            )
        if canonical in seen:
            continue
        seen.add(canonical)
        resolved.append((raw_symbol, canonical, symbols[canonical]))

    return resolved


def safe_float(value):
    if value is None:
        return None
    if isinstance(value, str):
        stripped = value.strip()
        if stripped in {"", "-", "None", "null"}:
            return None
        value = stripped
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_daily_row(api_symbol: str, trade_date: str, max_retries: int = 3):
    for attempt in range(1, max_retries + 1):
        try:
            frame = ak.futures_main_sina(symbol=api_symbol)
            if frame is None or frame.empty:
                return None

            rename_map = {src: dst for src, dst in COLUMN_MAP.items() if src in frame.columns}
            frame = frame.rename(columns=rename_map)
            if "trade_date" not in frame.columns:
                return None

            frame["trade_date"] = pd.to_datetime(frame["trade_date"], errors="coerce").dt.strftime(
                "%Y-%m-%d"
            )
            row = frame.loc[frame["trade_date"] == trade_date]
            if row.empty:
                return None

            return row.iloc[0]
        except Exception:
            if attempt >= max_retries:
                raise
            time.sleep((2 ** attempt) + random.uniform(0.3, 1.2))


def format_row(row, trade_date: str) -> Dict[str, object]:
    return {
        "trade_date": trade_date,
        "open_price": safe_float(row.get("open_price")),
        "high_price": safe_float(row.get("high_price")),
        "low_price": safe_float(row.get("low_price")),
        "close_price": safe_float(row.get("close_price")),
        "volume": int(safe_float(row.get("volume")) or 0),
        "open_interest": int(safe_float(row.get("open_interest")) or 0),
    }


def list_symbols(symbols: Dict[str, Dict[str, str]], keyword: str | None) -> Dict[str, object]:
    records = []
    normalized_keyword = keyword.strip().lower() if keyword else None

    for symbol in sorted(symbols):
        cfg = symbols[symbol]
        row = {
            "symbol": symbol,
            "api_symbol": cfg["api_symbol"],
            "name": cfg["name"],
            "exchange": cfg["exchange"],
        }
        if normalized_keyword:
            haystack = " ".join(row.values()).lower()
            if normalized_keyword not in haystack:
                continue
        records.append(row)

    return {
        "count": len(records),
        "keyword": keyword,
        "results": records,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch China futures main-contract daily bars")
    parser.add_argument("--date", "-d", help="Trade date in YYYY-MM-DD")
    parser.add_argument(
        "--symbol",
        "-s",
        help="One or more symbols separated by commas, e.g. aum,cum,rbm or 沪金,RB0",
    )
    parser.add_argument(
        "--list-symbols",
        action="store_true",
        help="Print the built-in symbol mapping and exit",
    )
    parser.add_argument(
        "--keyword",
        help="Filter `--list-symbols` results by code, API symbol, Chinese name, or exchange",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indent size. Use 0 for compact output.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    symbols = load_symbols()

    if args.list_symbols:
        payload = list_symbols(symbols, args.keyword)
        print(json.dumps(payload, ensure_ascii=False, indent=args.indent or None))
        return 0

    if not args.date or not args.symbol:
        parser.error("`--date` and `--symbol` are required unless `--list-symbols` is used.")

    trade_date = normalize_trade_date(args.date)
    requested_symbols = parse_symbols(args.symbol)
    resolved_symbols = resolve_symbols(requested_symbols, symbols)
    results = []

    for index, (input_symbol, canonical, cfg) in enumerate(resolved_symbols):
        try:
            row = fetch_daily_row(cfg["api_symbol"], trade_date)
        except Exception as exc:
            print(
                json.dumps(
                    {
                        "error": f"AkShare request failed for {cfg['api_symbol']}: {exc}",
                        "trade_date": trade_date,
                        "symbol": canonical,
                    },
                    ensure_ascii=False,
                    indent=args.indent or None,
                ),
                file=sys.stderr,
            )
            return 1

        result = {
            "input_symbol": input_symbol,
            "symbol": canonical,
            "api_symbol": cfg["api_symbol"],
            "name": cfg["name"],
            "exchange": cfg["exchange"],
        }
        if row is None:
            result["status"] = "no_data"
            result["message"] = f"No row returned for {trade_date}"
        else:
            result["status"] = "ok"
            result["data"] = format_row(row, trade_date)

        results.append(result)

        if index < len(resolved_symbols) - 1:
            time.sleep(random.uniform(0.4, 0.9))

    payload = {
        "trade_date": trade_date,
        "requested_symbols": requested_symbols,
        "results": results,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=args.indent or None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
