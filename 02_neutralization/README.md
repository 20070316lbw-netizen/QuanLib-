# 中性化模块 (02_neutralization)

## 功能说明
此模块主要提供量化预处理中常见的正交化/中性化操作资源，帮助去除因子对行业和市值的共线性，提取纯正的 Alpha。

## 核心函数
- `industry_neutral()` - 行业中性化 (通常通过哑变量剔除行业均值)
- `market_cap_neutral()` - 市值中性化 (通常对数市值进行线性回归)
- `ols_matrix()` - 执行批量 OLS 回归的基础矩阵推导抽象

## 使用示例
见 `example_usage.py`。
运行方式: `python example_usage.py`

## 测试数据说明
- `example_data.csv` - 包含带有所需的对应行业标签(分类)和市值暴露的模拟因子预处理数据。

## 依赖
- `numpy`
- `pandas`
- `scipy`
