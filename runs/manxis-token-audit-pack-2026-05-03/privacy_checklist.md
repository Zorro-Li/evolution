# ManXis Token Audit Privacy Checklist

## 默认处理方式

| 项目 | 规则 |
|---|---|
| Trace | 优先本地处理或客户侧运行。 |
| Secrets | 客户先移除 API key、cookies、tokens、private keys。 |
| Source code | 支持只提供片段、路径结构、trace 摘要。 |
| Screenshots | 支持打码账单、组织名、客户名。 |
| Report | 默认匿名，只写 task class 和 savings range。 |
| Retention | Pilot 资料默认 7 天内删除，客户可要求即时删除。 |

## 客户提交前自查

- [ ] 已移除 API keys、cookies、tokens、private keys。
- [ ] 已移除客户名称和个人身份信息。
- [ ] 已标注哪些内容允许进入报告。
- [ ] 已标注哪些内容允许用于匿名 case。
- [ ] 已说明是否允许 ManXis 保存优化后的 workflow patch。
- [ ] 已说明是否允许后续复测同类任务。

## 报告披露等级

| 等级 | 含义 |
|---|---|
| Private | 只发给客户，不用于宣传。 |
| Anonymous | 可写成匿名案例，不出现公司、人名、repo。 |
| Public | 可公开公司名、任务类型、结果数字和引用。 |

## 推荐默认

早期 design partner 使用 `local + redacted + anonymous`：本地运行、客户脱敏、报告可匿名引用。
