# main-retail-funds

## 原始数据录入原则

- 原始文件只录当天数据，不补历史数据。
- 原始文件不录价格。
- 价格由技能目录 [fetch-futures-daily-data](/Users/zxxk/ysd/ysdproject/notes/skills/fetch-futures-daily-data/SKILL.md) 补充。
- 录入顺序按看盘习惯组织：先按板块，再先录主力资金，后录散户资金。

## 原始文件格式

原始示例见 [raw-data-example.md](/Users/zxxk/ysd/ysdproject/notes/main-retail-funds/raw-data-example.md)。

格式约束如下：

- 顶部标题使用 `# YYYY-MM-DD`
- 板块使用 `## 黑色`、`## 有色`、`## 贵金属`
- 资金分类固定为 `### 主力资金` 和 `### 散户资金`
- 每条记录格式固定为 `- 品种: 数值`
- 数值只写数字，可正可负
- 暂时未录入的品种可以先写成 `- 品种:`
- 品种名称后续尽量保持一致，不混用别名

## 后续处理

- 你录完原始文件后，由 Codex 读取并整理数据。
- Codex 再结合价格接口数据，生成结构化 JSON。
- HTML 页面只读取 JSON，不直接解析手工录入文件。
