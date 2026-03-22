import pandas as pd
import numpy as np

def realized_volatility(returns: pd.DataFrame, window: int = 20) -> pd.Series:
    """
    已实现波动率
    
    参数:
        returns: DataFrame,日收益率
        window: 滚动窗口(天数)
    
    返回:
        Series,波动率(年化)
    """
    vol = returns.rolling(window=window).std() * np.sqrt(252)
    return vol.iloc[-1]


def downside_volatility(returns: pd.DataFrame, window: int = 20) -> pd.Series:
    """
    下行波动率(只计算负收益的波动)
    
    返回:
        Series,下行波动率
    """
    negative_returns = returns.copy()
    negative_returns[negative_returns > 0] = 0  # 正收益置零
    
    downside_vol = negative_returns.rolling(window=window).std() * np.sqrt(252)
    return downside_vol.iloc[-1]
