# 手写模型库 (03_models)

## 功能说明
这个模块包含了从头手写实现的经典机器学习模型框架，目前包含一个基础的 GBDT (`SimpleGBDT`)。适合用来作为深入理解模型内部机制、修改分裂条件或者扩展自定义损失函数的底座。

## 核心算法
- `SimpleGBDT` - 回归树的梯度提升算法实现，基于 MSE 损失函数计算一阶和二阶梯度。内含 `TreeNode`。

## 使用示例
见 `example_usage.py`。演示了如何将 pandas DataFrame 转为特征矩阵 `X` 和标签向量 `y`，并用其进行前向拟合与预测评估。
运行方式: `python example_usage.py`

## 测试数据说明
- `example_stock_data.csv` - 包含 100 行样本，5 个特征列 (f1~f5) 和 1 个标签列 (label) 的合成数据集。

## 依赖
- `numpy`
- `pandas`
- `loguru`
