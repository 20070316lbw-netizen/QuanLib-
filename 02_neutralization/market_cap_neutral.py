import numpy as np
import pandas as pd

def market_cap_neutralize(factor: pd.Series, market_cap: pd.Series) -> pd.Series:
    """
    市值中性化:去除因子与市值的线性关系
    
    方法:对 ln(market_cap) 做回归,取残差
    
    参数:
        factor: 因子值
        market_cap: 市值
    
    返回:
        市值中性化后的因子
    """
    # 取对数(避免极端值)
    log_cap = np.log(market_cap)
    
    # 标准化
    log_cap_std = (log_cap - log_cap.mean()) / log_cap.std()
    
    # OLS 回归: factor = β * log_cap + residual
    X = log_cap_std.values.reshape(-1, 1)
    y = factor.values
    
    # β = (X'X)⁻¹ X'y
    # 使用 np.linalg.inv 并且确保使用矩阵乘法 @ 而不是 *
    # 提前将 y 调整为列向量保证运算形状对齐
    y = factor.values.reshape(-1, 1)
    
    beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
    
    # residual = y - Xβ
    residual = y - X @ beta
    
    return pd.Series(residual.flatten(), index=factor.index)
