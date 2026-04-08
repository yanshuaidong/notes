#!/usr/bin/env python3

import json
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WEEKS_DIR = ROOT / "data" / "weeks"
INDEX_PATH = ROOT / "market-emotion-events.json"


def iso_week_key(date_text: str) -> str:
    year, week, _ = date.fromisoformat(date_text).isocalendar()
    return f"{year}-W{week:02d}"


def load_week_files():
    week_files = sorted(WEEKS_DIR.glob("*.json"))
    if not week_files:
        raise SystemExit("未找到任何周数据文件。")

    all_events = []
    summaries = []
    meta = None
    emotion_palette = None
    direction_palette = None

    for week_file in week_files:
        payload = json.loads(week_file.read_text(encoding="utf-8"))
        if meta is None:
            meta = payload.get("meta", {})
            emotion_palette = payload.get("emotion_palette", {})
            direction_palette = payload.get("direction_palette", {})

        week_key = payload.get("week")
        events = payload.get("events", [])
        for event in events:
            derived_week = iso_week_key(event["date"])
            if derived_week != week_key:
                raise SystemExit(f"{week_file.name} 中存在跨周事件：{event['id']} -> {event['date']}")

        dates = sorted({event["date"] for event in events})
        months = sorted({event["date"][:7] for event in events})
        all_events.extend(events)
        summaries.append(
            {
                "week": week_key,
                "path": f"./data/weeks/{week_file.name}",
                "event_count": len(events),
                "dates": dates,
                "months": months,
            }
        )

    return meta, emotion_palette, direction_palette, all_events, summaries


def build_aggregates(events):
    direction_counts = Counter(event.get("direction", "未填写") for event in events)
    driver_counts = Counter(
        driver
        for event in events
        for driver in event.get("driver_types", [])
    )

    return {
        "event_count": len(events),
        "latest_date": max((event["date"] for event in events), default=""),
        "months": sorted({event["date"][:7] for event in events}),
        "instruments": sorted({event.get("instrument", "未填写") for event in events}),
        "directions": sorted(direction_counts),
        "drivers": sorted(driver_counts),
        "horizons": sorted({event.get("trade_horizon", "未填写") for event in events}),
        "direction_counts": dict(sorted(direction_counts.items())),
        "driver_counts": dict(driver_counts.most_common()),
    }


def main():
    meta, emotion_palette, direction_palette, events, summaries = load_week_files()
    manifest = {
        "meta": {
            **meta,
            "version": 3,
            "storage_mode": "weekly-manifest",
            "updated_at": max((event["date"] for event in events), default=meta.get("updated_at", "")),
        },
        "emotion_palette": emotion_palette,
        "direction_palette": direction_palette,
        "aggregates": build_aggregates(events),
        "weeks": summaries,
    }
    INDEX_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"已生成 {INDEX_PATH}")


if __name__ == "__main__":
    main()
