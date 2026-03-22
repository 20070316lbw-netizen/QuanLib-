import pandas as pd
from date_utils import get_trade_dates, offset_trade_date
from stock_filter import filter_st_stocks, filter_suspended
from logger_config import setup_logger

def main():
    print("=== 初始化日志记录器 ===")
    logger = setup_logger(log_file="quanlib_utils_demo.log", level="DEBUG")
    logger.info("系统启动...")
    
    print("\n=== 日期工具演示 ===")
    start_date = "2024-01-01"
    end_date = "2024-01-10"
    logger.info(f"获取 {start_date} 到 {end_date} 之间的交易日列表:")
    trade_dates = get_trade_dates(start_date, end_date)
    print(trade_dates)
    
    base_date = "2024-01-02"
    offset = -3 # 过去3个工作日
    past_date = offset_trade_date(base_date, offset)
    logger.info(f"日期 {base_date} 往回退 {abs(offset)} 个工作日是: {past_date}")
    print(past_date)
    
    print("\n=== 股票过滤器演示 ===")
    # 1. 过滤 ST 股票
    all_stocks = ['000001.SZ', '000002.SZ', '000001.ST', '600000.SH', '600001.*ST']
    logger.warning("发现一些风险警示股票，正在执行 ST 过滤...")
    clean_stocks = filter_st_stocks(all_stocks)
    print("原始股票池:", all_stocks)
    print("过滤 ST 后:", clean_stocks)
    
    # 2. 过滤停牌股票
    stock_codes = ['000001.SZ', '000002.SZ', '600000.SH', '000333.SZ']
    # 模拟成交量(假设 000002 停牌)
    volumes = pd.Series([150000, 0, 500000, 200000], index=stock_codes)
    logger.warning("正在过滤当日可能停牌(成交量为 0)的股票...")
    active_stocks = filter_suspended(stock_codes, volumes)
    print("\n股票成交量分布:\n", volumes)
    print("剔除停牌股票后剩余:", active_stocks)
    
    logger.success("工具箱的所有演示执行完毕！")

if __name__ == "__main__":
    main()
