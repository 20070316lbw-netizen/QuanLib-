import pandas as pd
import numpy as np

def momentum_12_1(prices: pd.DataFrame, window: int = 12, lag: int = 1) -> pd.Series:
    """
    12-1 动量因子
    
    计算过去12个月收益率,但跳过最近1个月(避免短期反转)
    
    参数:
        prices: DataFrame,索引为日期,列为股票代码,值为收盘价
        window: 回看窗口(月数)
        lag: 跳过的最近月数
    
    返回:
        Series,每只股票的动量因子值
    """
    # 计算 t-1 到 t-12 的收益率
    # return = (P_t-1 / P_t-12) - 1
    momentum = prices.shift(lag) / prices.shift(window + lag) - 1
    
    return momentum.iloc[-1]  # 返回最新截面


def reversal_1month(prices: pd.DataFrame) -> pd.Series:
    """
    短期反转因子
    
    计算最近1个月收益率,取负值(反转)
    
    返回:
        Series,反转因子值(负的短期收益)
    """
    ret_1m = prices.pct_change(periods=20)  # 假设1月=20个交易日
    reversal = -ret_1m.iloc[-1]  # 取负
    
    return reversal
