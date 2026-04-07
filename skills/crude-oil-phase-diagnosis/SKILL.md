---
name: crude-oil-phase-diagnosis
description: Diagnose the current trading phase of crude oil futures and map it to a suitable response strategy. Use when the user wants to judge whether crude oil is in the shock, expectation expansion, expectation realization, or sentiment fade stage; when Codex should produce a decision flowchart, phase checklist, or stage-specific trading response; or when the user asks how to handle oil under different market regimes instead of predicting a single direction.
---

# Crude Oil Phase Diagnosis

Use this skill to classify the current crude oil market into a trading phase, then respond with the matching strategy template.

## Output Rules

- Do not promise a directional win.
- Focus on regime identification first, strategy second.
- Prefer Chinese if the user asks in Chinese.
- If the current phase cannot be distinguished cleanly, say it is a transition state and list the two most likely phases.

## Four Phases

1. `突发冲击期`
   Conditions:
   - A fresh geopolitical, policy, transport, or supply event hits the market.
   - Price gaps or moves sharply within 1 to 3 sessions.
   - Intraday reversals are violent and news flow is dense.
   Default response:
   - Prefer light size or no trade.
   - Avoid chasing the first move without confirmation.

2. `预期发酵期`
   Conditions:
   - The market keeps trading one dominant storyline.
   - Pullbacks are bought or selloffs are pressed again.
   - New headlines still extend the move instead of getting ignored.
   Default response:
   - Trade with the prevailing direction only after confirmation.
   - Avoid top-picking or bottom-picking.

3. `预期兑现期`
   Conditions:
   - The original story is still active, but price stops extending smoothly.
   - Good news fails to push much higher, or bad news fails to push much lower.
   - Range expansion and two-way swings increase.
   Default response:
   - Lower holding-period expectations.
   - Prefer faster trades and tighter discipline.

4. `情绪退潮期`
   Conditions:
   - News is still present, but the market reacts with less consistency.
   - Direction becomes messy and stop-hunts become common.
   - The old storyline no longer produces clean follow-through.
   Default response:
   - Trade less or stand aside.
   - Only act when structure is unusually clear.

## Quick Diagnostic Workflow

Check in this order:

1. Was there a fresh event that changed supply, transport, sanctions, or war risk within the last 1 to 3 sessions?
2. Did price gap or move abnormally hard right after it?
3. Are headlines still extending the same move, or are they being absorbed?
4. Is the market still trending after pullbacks, or has it shifted into broad two-way swings?
5. Has the storyline weakened enough that price is now mostly chopping and trapping?

## Mermaid Template

Use this template when the user asks for a flowchart:

```mermaid
flowchart TD
    A[开始: 当前交易对象是原油<br/>先看最近1到3个交易日] --> B{是否出现突发地缘/政策/供应事件<br/>且价格跳空或单日大涨大跌?}

    B -- 是 --> C{波动率是否明显放大<br/>新闻密集且盘中频繁反转?}
    B -- 否 --> D{市场是否反复围绕同一主线交易<br/>如战争扩大/运输受阻/减产/库存?}

    C -- 是 --> E[阶段1: 突发冲击期<br/>特征: 跳空 强波动 信息不完整]
    C -- 否 --> D

    D -- 是 --> F{利多/利空消息出来后<br/>价格是否仍能顺势创新高/新低?}
    D -- 否 --> G{原来的主线还在<br/>但价格已经不再顺畅延续?}

    F -- 是 --> H[阶段2: 预期发酵期<br/>特征: 主线明确 趋势延续 回撤后仍有资金接]
    F -- 否 --> I{消息仍在兑现<br/>但价格高位/低位宽幅震荡<br/>并频繁出现利多不涨或利空不跌?}

    I -- 是 --> J[阶段3: 预期兑现期<br/>特征: 故事没结束 但定价已走在前面]
    I -- 否 --> H

    G -- 是 --> K{新闻热度下降<br/>价格来回扫损<br/>方向变乱 成交逻辑碎片化?}
    G -- 否 --> D

    K -- 是 --> L[阶段4: 情绪退潮期<br/>特征: 还有波动 但主线钝化 容易反复打脸]
    K -- 否 --> J
```

## Response Template

Use this structure when diagnosing the current market:

1. `当前更像哪个阶段`
2. `我这样判断的关键信号`
3. `这个阶段适合什么，不适合什么`
4. `如果判断错了，最容易错在哪`

## Decision Standard

If two adjacent phases overlap, classify by the market behavior rather than the news intensity:

- Still extending the move after pullbacks: lean `预期发酵期`
- Story intact but extension weakens: lean `预期兑现期`
- Story weakens and price action turns noisy: lean `情绪退潮期`
