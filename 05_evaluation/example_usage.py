import pandas as pd
from ic_metrics import information_coefficient, rank_ic, icir
from backtest_simple import run_simple_backtest

def main():
    print("=== 加载预测数据 ===")
    df = pd.read_csv("example_predictions.csv", parse_dates=["date"])
    print(df.head())
    
    # 为了方便横截面操作和简易回测，设置为双层索引 (date, stock_code)
    df.set_index(['date', 'stock_code'], inplace=True)
    
    preds = df['prediction']
    rets = df['future_return']
    
    print("\n=== 计算 IC 指标 ===")
    
    # 按照横截面(date)计算每天的 IC 和 Rank IC
    daily_ic = df.groupby(level='date').apply(
        lambda x: information_coefficient(x['prediction'], x['future_return'])
    )
    
    daily_rank_ic = df.groupby(level='date').apply(
        lambda x: rank_ic(x['prediction'], x['future_return'])
    )
    
    print("每日 IC:")
    print(daily_ic)
    
    print("\n每日 Rank IC:")
    print(daily_rank_ic)
    
    # 计算整体的 ICIR
    print(f"\n整体 ICIR      : {icir(daily_ic):.4f}")
    print(f"整体 Rank ICIR : {icir(daily_rank_ic):.4f}")
    
    print("\n=== 运行简易分层回测 (分3组演示) ===")
    # 因为股票数量少，所以分为3组进行演示
    group_returns = run_simple_backtest(preds, rets, n_groups=3)
    
    print("各分组日均收益率:")
    print(group_returns)
    
    # 计算累计收益率
    cum_returns = (1 + group_returns).cumprod() - 1
    print("\n各分组累计收益率:")
    print(cum_returns)

if __name__ == "__main__":
    main()
