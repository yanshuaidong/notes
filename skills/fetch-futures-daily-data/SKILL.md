---
name: fetch-futures-daily-data
description: Fetch China futures main-contract daily bars for a specified trade date and one or more symbols through AkShare. Use when Codex needs to query futures day-level OHLCV and open-interest data by custom symbol code such as aum/cum/rbm, by Chinese variety name such as 沪金 or 螺纹钢, or by API symbol such as AU0/RB0, and return the result as structured JSON without writing to a database.
---

# Fetch Futures Daily Data

## Overview

Use [`scripts/fetch_futures_daily.py`](./scripts/fetch_futures_daily.py) to fetch a target trade date for one or more futures main contracts from AkShare's Sina endpoint. Keep the workflow self-contained inside this skill directory; do not depend on external project files.

## Quick Start

If `akshare` is missing, install runtime dependencies first:

```powershell
python -m pip install akshare pandas
```

List supported symbols:

```powershell
python .\scripts\fetch_futures_daily.py --list-symbols
```

Fetch one symbol:

```powershell
python .\scripts\fetch_futures_daily.py --date 2026-03-05 --symbol aum
```

Fetch multiple symbols:

```powershell
python .\scripts\fetch_futures_daily.py --date 2026-03-05 --symbol aum,cum,rbm
```

Resolve by Chinese variety name or API symbol:

```powershell
python .\scripts\fetch_futures_daily.py --date 2026-03-05 --symbol 沪金,RB0
```

## Workflow

1. Prefer the custom canonical codes in `scripts/futures_symbols.json`, such as `aum`, `cum`, `rbm`.
2. Accept Chinese names such as `沪金` or `沪金主连` when the user does not know the code.
3. Run the script from the skill root or any directory with an absolute path.
4. Return the JSON result directly to the user unless they ask for a file export.

## Output Contract

The script prints JSON to stdout with these top-level fields:

- `trade_date`: normalized `YYYY-MM-DD`
- `requested_symbols`: raw symbols from the command
- `results`: one object per resolved symbol

Each result object contains:

- `input_symbol`: raw user input
- `symbol`: canonical skill code such as `aum`
- `api_symbol`: AkShare/Sina symbol such as `AU0`
- `name`: Chinese variety name
- `exchange`: exchange code
- `status`: `ok` or `no_data`
- `data`: daily bar when `status=ok`
- `message`: explanation when `status=no_data`

## Notes

- Use only main-contract daily data from `akshare.futures_main_sina`.
- Expect `no_data` on non-trading days or when the upstream source has no row for that date.
- Treat symbol resolution as case-insensitive.
- Use `--list-symbols --keyword 关键词` to filter the built-in mapping before fetching.
