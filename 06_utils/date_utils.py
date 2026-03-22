import pandas as pd
from typing import List

def get_trade_dates(start: str, end: str) -> List[str]:
    """
    获取交易日列表(简化版,实际应该用 tushare 或 akshare)
    
    参数:
        start: 开始日期 'YYYY-MM-DD'
        end: 结束日期 'YYYY-MM-DD'
    
    返回:
        交易日列表
    """
    # 生成日期范围,排除周末
    dates = pd.bdate_range(start=start, end=end)
    return dates.strftime('%Y-%m-%d').tolist()


def offset_trade_date(date: str, offset: int) -> str:
    """
    交易日偏移
    
    参数:
        date: 基准日期
        offset: 偏移量(正数=未来,负数=过去)
    
    返回:
        偏移后的交易日
    """
    base = pd.to_datetime(date)
    target = base + pd.offsets.BDay(offset)
    return target.strftime('%Y-%m-%d')
