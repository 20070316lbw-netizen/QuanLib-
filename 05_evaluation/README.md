# 评估指标 (05_evaluation)

## 功能说明
本模块提供了从特征/因子评估到初步策略回放验证的基础指标和回测框架。无需引入庞大的生态即可快速校验 Alpha 因子的质量。

## 核心函数
- `calculate_ic()` - 计算 IC, RankIC, ICIR 等绩效评估指标
- `run_simple_backtest()` - 使用构建的简易回测框架验证策略表现情况

## 使用示例
见 `example_usage.py`。
运行方式: `python example_usage.py`

## 测试数据说明
- `example_predictions.csv` - 预先生成的因子预测值 + 未来真实的股票收益率样本数据。

## 依赖
- `numpy`
- `pandas`
