# 工具函数 (06_utils)

## 功能说明
此模块提供量化操作日常使用的杂项工具集合，包括日历维护、股票清洗、以及统一的日志管理。

## 核心函数
- `get_trading_days()` - 交易日历处理与对其操作
- `filter_stock_pool()` - 过滤非正常交易状态的股票(例如 ST 股票、今日/长期停牌股)
- `setup_logger()` - 提供标准化的 `loguru` 配置模板

## 使用示例
见 `example_usage.py`。
运行方式: `python example_usage.py`

## 测试数据说明
无需特殊测试数据，或者随代码提供小的演示内存数据供使用测试。

## 依赖
- `pandas`
- `loguru`
