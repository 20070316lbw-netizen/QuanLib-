import pandas as pd
from ols_matrix import neutralize_factor
from industry_neutral import industry_neutralize
from market_cap_neutral import market_cap_neutralize

# 加载数据
df = pd.read_csv('example_data.csv')

print("=== 原始因子 ===")
print(df[['stock_code', 'factor', 'industry']])

# 1. 行业中性化
df['factor_ind_neutral'] = industry_neutralize(
    df['factor'], 
    df['industry']
)

print("\n=== 行业中性化后 ===")
print(df[['stock_code', 'factor_ind_neutral', 'industry']])

# 2. 市值中性化
df['factor_cap_neutral'] = market_cap_neutralize(
    df['factor'],
    df['market_cap']
)

print("\n=== 市值中性化后 ===")
print(df[['stock_code', 'factor_cap_neutral']])

# 3. 同时行业+市值中性化
df['factor_full_neutral'] = neutralize_factor(
    df['factor'],
    df['industry'],
    df['market_cap']
)

print("\n=== 行业+市值中性化后 ===")
print(df[['stock_code', 'factor_full_neutral']])
