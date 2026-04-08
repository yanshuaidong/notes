# market-emotion

这是一个独立的市场观察视角。

起点是把市场报道、研报、分析文本里的情绪抽出来看；现在进一步升级成面向期货盘前与复盘的交易线索工具。
它不替代交易决策，但会把研报拆成更容易使用的几个部分：方向、驱动、周期、执行提示、风险点和失效条件。

## 文件

- `market-emotion-events.json`：页面先读取的索引文件，包含统计汇总和按周 JSON 清单。
- `data/weeks/*.json`：真正的事件数据，按 ISO 周拆分存放。
- `index.html`：市场情绪与交易线索页面，包含最新交易焦点、筛选面板、风险雷达和情绪日历。
- `inbox/daily-analysis-inbox.md`：每日新增分析的统一收件箱。
- `scripts/rebuild_market_emotion_index.py`：扫描各周 JSON，重建首页索引文件。

## 当前能做什么

- 盘前快速看最新日期的偏多、偏空、震荡品种。
- 按品种、方向、驱动和周期筛选研报线索。
- 直接查看每条记录的执行提示、风险点和失效条件。
- 保留日期视图，用于做历史复盘和情绪样本观察。

## 打开方式

建议在当前目录运行：

```bash
python3 -m http.server
```

然后访问：

```text
http://localhost:8000/market-emotion/
```

## 新增分析的工作流

1. 把当天日期、品种和分析内容追加到 `inbox/daily-analysis-inbox.md`。
2. 在 Codex 里给一句简单提示词，例如：`处理 market-emotion 收件箱，把待处理内容入库`。
3. 我会把内容整理成结构化事件，写入对应周的 `data/weeks/*.json`。
4. 更新后运行：

```bash
python3 scripts/rebuild_market_emotion_index.py
```

这样首页索引会自动刷新，页面就能直接看到结果。
