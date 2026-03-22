# 数据质量检查模块 (01_data_quality)

## 功能说明
提供通用的数据健康度检查功能，快速发现金融时序数据中的缺失、跳变等异常。本模块代码设计参考了 Microsoft QLib 的 `check_data_health.py`。

## 核心函数/类
`DataHealthChecker`：
- `check_ohlcv_columns()` - 检查必需的 OHLCV 列是否存在
- `check_missing_data()` - 统计各字段缺失值数量
- `check_price_jumps()` - 检查价格是否出现极大异常跳变 (默认>50%)
- `check_volume_jumps()` - 检查成交量极度异常跳变 (默认>3倍)
- `run_all_checks()` - 运行所有检查并返回综合报告字典

## 使用示例
见 `example_usage.py`。
运行方式: `python example_usage.py`

## 测试数据说明
- `example_dirty_data.csv` - 包含缺失值（如第二个样本的 high 缺失）、价格异常跳变和成交量异常跳变的虚构测试集。

## 依赖
- `pandas`
- `numpy`
- `loguru`
