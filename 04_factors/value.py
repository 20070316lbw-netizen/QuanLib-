import pandas as pd

def book_to_price(book_value: pd.Series, market_cap: pd.Series) -> pd.Series:
    """
    账面市值比 (BP)
    
    参数:
        book_value: 账面价值(净资产)
        market_cap: 市值
    
    返回:
        BP 因子
    """
    return book_value / market_cap


def earnings_to_price(earnings: pd.Series, market_cap: pd.Series) -> pd.Series:
    """
    盈利市值比 (EP)
    
    参数:
        earnings: 净利润
        market_cap: 市值
    
    返回:
        EP 因子
    """
    return earnings / market_cap
