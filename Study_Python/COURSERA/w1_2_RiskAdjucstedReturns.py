import pandas as pd
import numpy as np

prices = pd.read_csv("COURSERA\data\sample_prices.csv")
returns = prices.pct_change()
returns = returns.dropna()
print(returns)
print(returns.std())
# 표준편차 구해보기
deviations = returns - returns.mean()
squared_deviations = deviations**2
number_of_ob = returns.shape[0]
variance = squared_deviations.sum() / (number_of_ob-1)
volatility = np.sqrt(variance)
print(volatility)

print(returns.std()*np.sqrt(12))