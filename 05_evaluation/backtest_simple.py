import numpy as np
import pandas as pd

def run_simple_backtest(
    predictions: pd.Series,
    returns: pd.Series,
    n_groups: int = 5
) -> pd.DataFrame:
    """
    简易的分层回测框架
    
    根据因子预测值将股票分成 n 组，计算每组的平均收益率 (等权)
    
    参数:
        predictions: 因子预测值 (多层MultiIndex: date, stock_code)
        returns: 未来一期真实收益率 (多层MultiIndex: date, stock_code)
        n_groups: 分组数量，默认为5(五分位)
        
    返回:
        DataFrame, 每组在各个时间截面的平均收益率
    """
    df = pd.DataFrame({'pred': predictions, 'ret': returns}).dropna()
    
    # 在每个横截面(date)按因子值分组
    def assign_group(group_df):
        # qcut 要求数据具备一定的多样性，为了防止相同的预测值导致分位数重叠，加入微小扰动
        preds = group_df['pred'] + np.random.randn(len(group_df)) * 1e-10
        try:
            return pd.qcut(preds, q=n_groups, labels=False, duplicates='drop') + 1
        except ValueError:
            return np.nan

    # 按第一层索引(通常是date)进行groupby
    df['group'] = df.groupby(level=0, group_keys=False).apply(assign_group)
    df = df.dropna(subset=['group'])
    
    # 计算每个横截面每组的平均收益
    group_returns = df.groupby([df.index.get_level_values(0), 'group'])['ret'].mean().unstack()
    group_returns.columns = [f"Group_{int(g)}" for g in group_returns.columns]
    
    # 额外计算多空组合收益 (最高组 - 最低组)
    if not group_returns.empty and len(group_returns.columns) > 1:
        top_group = group_returns.columns[-1]
        bottom_group = group_returns.columns[0]
        group_returns['Long_Short'] = group_returns[top_group] - group_returns[bottom_group]
        
    return group_returns
