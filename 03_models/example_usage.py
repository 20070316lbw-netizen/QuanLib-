from simple_gbdt import SimpleGBDT
import pandas as pd
import numpy as np
from loguru import logger

def main():
    logger.info("验证 SimpleGBDT 模型...")
    
    # 1. 记载示例数据
    df = pd.read_csv("example_stock_data.csv")
    
    # 2. 准备特征和标签
    feature_cols = ["f1", "f2", "f3", "f4", "f5"]
    X = df[feature_cols].values
    y = df["label"].values
    
    # 3. 划分简单的训练集和测试集
    split_idx = int(len(df) * 0.8)
    X_train, y_train = X[:split_idx], y[:split_idx]
    X_test, y_test = X[split_idx:], y[split_idx:]
    
    # 4. 初始化模型
    logger.info(f"初始化模型参数: n_trees=50, max_depth=3, lr=0.1, min_samples=2")
    model = SimpleGBDT(n_trees=50, max_depth=3, lr=0.1, min_samples=2)
    
    # 5. 训练
    logger.info("开始训练模型...")
    model.fit(X_train, y_train)
    logger.info("模型训练完成。")
    
    # 6. 预测与评估
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    train_mse = np.mean((y_train - y_train_pred)**2)
    test_mse = np.mean((y_test - y_test_pred)**2)
    
    print("\n" + "="*40)
    print("训练结果:")
    print(f"Train MSE: {train_mse:.4f}")
    print(f"Test MSE:  {test_mse:.4f}")
    
    # 对比几个真实值和预测值
    print("\n部分测试集预测展示:")
    for i in range(5):
        print(f"真实值: {y_test[i]:.4f} | 预测值: {y_test_pred[i]:.4f}")
    print("="*40)

if __name__ == "__main__":
    main()
