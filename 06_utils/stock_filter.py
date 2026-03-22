import pandas as pd
from typing import List

def filter_st_stocks(stock_codes: List[str]) -> List[str]:
    """
    过滤 ST 股票
    
    参数:
        stock_codes: 股票代码列表
    
    返回:
        过滤后的股票列表
    """
    # 简化判断:股票名称包含 'ST' 的排除
    return [code for code in stock_codes if 'ST' not in code]


def filter_suspended(
    stock_codes: List[str],
    trade_volumes: pd.Series
) -> List[str]:
    """
    过滤停牌股票(成交量为0)
    
    参数:
        stock_codes: 股票代码列表
        trade_volumes: 成交量 Series
    
    返回:
        过滤后的股票列表
    """
    valid = trade_volumes[trade_volumes > 0].index.tolist()
    return [code for code in stock_codes if code in valid]
