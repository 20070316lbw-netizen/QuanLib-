import pandas as pd
from momentum import momentum_12_1, reversal_1month
from volatility import realized_volatility, downside_volatility
from value import book_to_price, earnings_to_price

def main():
    print("=== 加载测试数据 ===")
    df = pd.read_csv("example_price_data.csv", parse_dates=["date"])
    print(df.head())

    # 转换数据格式以适应因子函数: 索引为日期,列为股票代码
    prices = df.pivot(index="date", columns="stock_code", values="close")
    returns = prices.pct_change()
    
    print("\n=== 计算动量因子 ===")
    # 这里用 window=20, lag=1 仅做演示 (假设20天为1个月，原本12个月需要长达250天以上数据)
    mom_12_1 = momentum_12_1(prices, window=20, lag=1)
    print("20天动量因子(跳过最近1天):")
    print(mom_12_1)
    
    rev_1m = reversal_1month(prices)
    print("\n1个月反转因子:")
    print(rev_1m)

    print("\n=== 计算波动率因子 ===")
    real_vol = realized_volatility(returns, window=20)
    print("20天已实现波动率(年化):")
    print(real_vol)
    
    down_vol = downside_volatility(returns, window=20)
    print("\n20天下行波动率(年化):")
    print(down_vol)

    print("\n=== 计算估值因子 ===")
    # 取截面最新一天的数据
    latest_df = df[df["date"] == df["date"].max()].set_index("stock_code")
    
    bp = book_to_price(latest_df["book_value"], latest_df["market_cap"])
    print("截面 BP 因子 (账面市值比):")
    print(bp)
    
    ep = earnings_to_price(latest_df["earnings"], latest_df["market_cap"])
    print("\n截面 EP 因子 (盈利市值比):")
    print(ep)

if __name__ == "__main__":
    main()
