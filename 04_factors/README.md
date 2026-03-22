# 因子计算库 (04_factors)

## 功能说明
这个模块包含了通用截面 Alpha 因子的可复用快速计算逻辑，主要覆盖量价与基本面领域的经典大类。

## 核心函数
- `momentum_factor()` - 动量因子 (如 12-1 动量，反转效应 reversal)
- `volatility_factor()` - 波动率因子计算
- `value_factor()` - 估值因子计算 (BP, EP)

## 使用示例
见 `example_usage.py`。
运行方式: `python example_usage.py`

## 测试数据说明
- `example_price_data.csv` - 提供了模拟的 OHLCV 价量数据以及可能的财务基本面字段用于因子构建。

## 依赖
- `numpy`
- `pandas`
