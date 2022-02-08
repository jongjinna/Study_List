import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

returns = pd.read_csv("COURSERA\data\Portfolios_Formed_on_ME_monthly_EW.csv", header = 0, index_col=0, parse_dates=True, na_values=-99.99)
print(returns)
columns = ["Lo 10", "Hi 10"]
returns = returns[columns]/100 # 퍼센트를 변환 3% -> 0.03
print(returns.head())
returns.columns = ["SmallCap", "LargeCap"]
returns.plot.line()
plt.show()
annualized_vol = returns.std()*np.sqrt(12)
print(annualized_vol)
n_months = returns.shape[0]
return_per_month = (returns+1).prod()**(1/n_months)-1
print(return_per_month)

annualized_return = (return_per_month+1)**12 -1
annualized_return = (returns+1).prod()**(12/n_months)-1 # 둘이 같은 내용
print(annualized_return)
print(annualized_return/annualized_vol)

riskfree_rate = 0.03
excess_return = annualized_return - riskfree_rate
sharpe_ratio = excess_return/annualized_vol
print(sharpe_ratio)