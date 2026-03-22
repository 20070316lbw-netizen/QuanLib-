import numpy as np
import pandas as pd

def industry_neutralize(factor: pd.Series, industry: pd.Series) -> pd.Series:
    """
    行业中性化:去除因子在行业间的差异
    
    方法:在每个行业内减去该行业均值
    
    参数:
        factor: 因子值
        industry: 行业分类
    
    返回:
        行业中性化后的因子
    """
    df = pd.DataFrame({'factor': factor, 'industry': industry})
    
    # 每个行业内去均值
    neutralized = df.groupby('industry')['factor'].transform(
        lambda x: x - x.mean()
    )
    
    return neutralized


def industry_neutralize_with_weights(
    factor: pd.Series, 
    industry: pd.Series,
    market_cap: pd.Series
) -> pd.Series:
    """
    加权行业中性化:用市值加权计算行业均值
    
    参数:
        factor: 因子值
        industry: 行业分类
        market_cap: 市值(用于加权)
    
    返回:
        加权行业中性化后的因子
    """
    df = pd.DataFrame({
        'factor': factor,
        'industry': industry,
        'cap': market_cap
    })
    
    # 每个行业内计算加权均值
    def weighted_demean(group):
        weights = group['cap'] / group['cap'].sum()
        industry_mean = (group['factor'] * weights).sum()
        return group['factor'] - industry_mean
    
    neutralized = df.groupby('industry').apply(weighted_demean)['factor']
    
    return neutralized
