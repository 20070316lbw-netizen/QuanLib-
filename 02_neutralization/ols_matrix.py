import numpy as np
import pandas as pd
from typing import Tuple

class OLSNeutralization:
    """
    OLS 矩阵回归中性化
    
    数学推导:
    给定因子 f (n×1), 控制变量 X (n×k)
    目标: residual = f - X·β
    
    求解 β:
    Loss = (f - Xβ)ᵀ(f - Xβ)
    ∂Loss/∂β = -2Xᵀf + 2XᵀXβ = 0
    => XᵀXβ = Xᵀf
    => β = (XᵀX)⁻¹Xᵀf  ← 核心公式
    
    residual = f - Xβ = f - X(XᵀX)⁻¹Xᵀf
             = (I - X(XᵀX)⁻¹Xᵀ)f
             = Mf
    其中 M = I - H, H = X(XᵀX)⁻¹Xᵀ 称为帽子矩阵(Hat Matrix)
    """
    
    def __init__(self):
        self.beta = None
        self.fitted = False
    
    def fit(self, factor: np.ndarray, controls: np.ndarray) -> 'OLSNeutralization':
        """
        拟合 OLS 回归系数
        
        参数:
            factor: (n,) 或 (n, 1) - 待中性化的因子
            controls: (n, k) - 控制变量矩阵(如行业哑变量、市值)
        
        返回:
            self
        """
        # 确保是列向量
        if factor.ndim == 1:
            factor = factor.reshape(-1, 1)
        
        # β = (X'X)⁻¹X'y
        XtX = controls.T @ controls  # (k, k)
        Xty = controls.T @ factor     # (k, 1)
        
        # 求逆(实际中应该用更稳定的方法,如 np.linalg.lstsq)
        self.beta = np.linalg.solve(XtX, Xty)  # (k, 1)
        self.fitted = True
        return self
    
    def transform(self, factor: np.ndarray, controls: np.ndarray) -> np.ndarray:
        """
        计算中性化残差
        
        返回:
            residual = f - Xβ
        """
        if not self.fitted:
            raise ValueError("必须先调用 fit() 拟合模型")
        
        if factor.ndim == 1:
            factor = factor.reshape(-1, 1)
        
        # residual = f - Xβ
        predictions = controls @ self.beta
        residual = factor - predictions
        
        return residual.flatten()
    
    def fit_transform(self, factor: np.ndarray, controls: np.ndarray) -> np.ndarray:
        """一步完成拟合和转换"""
        self.fit(factor, controls)
        return self.transform(factor, controls)


def neutralize_factor(
    factor: pd.Series,
    industry: pd.Series,
    market_cap: pd.Series = None
) -> pd.Series:
    """
    便捷函数:对因子进行行业和市值中性化
    
    参数:
        factor: 因子值
        industry: 行业分类(字符串)
        market_cap: 市值(可选)
    
    返回:
        中性化后的因子
    """
    # 构造控制变量矩阵
    # 1. 行业哑变量
    industry_dummies = pd.get_dummies(industry, drop_first=True)
    
    X = industry_dummies.values
    
    # 2. 添加市值(如果提供)
    if market_cap is not None:
        # 标准化市值
        market_cap_std = (market_cap - market_cap.mean()) / market_cap.std()
        X = np.column_stack([X, market_cap_std.values])
    
    # 3. OLS 中性化
    ols = OLSNeutralization()
    residual = ols.fit_transform(factor.values, X)
    
    return pd.Series(residual, index=factor.index)
