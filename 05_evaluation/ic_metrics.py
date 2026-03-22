import numpy as np
import pandas as pd
from scipy.stats import spearmanr

def information_coefficient(
    predictions: pd.Series, 
    returns: pd.Series
) -> float:
    """
    计算 IC (Information Coefficient)
    
    IC = corr(预测值, 真实收益)
    
    参数:
        predictions: 因子预测值
        returns: 未来收益率
    
    返回:
        IC 值
    """
    # 去除缺失值
    valid = pd.DataFrame({'pred': predictions, 'ret': returns}).dropna()
    
    if len(valid) < 2:
        return np.nan
    
    ic = valid['pred'].corr(valid['ret'])
    return ic


def rank_ic(predictions: pd.Series, returns: pd.Series) -> float:
    """
    计算 Rank IC (Spearman 相关系数)
    
    参数:
        predictions: 因子预测值
        returns: 未来收益率
    
    返回:
        Rank IC 值
    """
    valid = pd.DataFrame({'pred': predictions, 'ret': returns}).dropna()
    
    if len(valid) < 2:
        return np.nan
    
    rank_ic, _ = spearmanr(valid['pred'], valid['ret'])
    return rank_ic


def icir(ic_series: pd.Series) -> float:
    """
    计算 ICIR (Information Coefficient Information Ratio)
    
    ICIR = mean(IC) / std(IC)
    
    参数:
        ic_series: IC 时间序列
    
    返回:
        ICIR 值
    """
    if ic_series.std() == 0:
        return np.nan
    return ic_series.mean() / ic_series.std()
