import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prices_a = [8.70, 8.91, 8.71]
print(prices_a)
print(prices_a[1:])
print(prices_a[:-1])
#list 와 list는 나눌 수 없음

prices_b = np.array([8.70, 8.91, 8.71])
print(prices_b)
print(prices_b[1:])
print(prices_b[:-1])
print(prices_b[1:]/prices_b[-1:])
#array끼리는 나누기 가능, 값이 이상하게 나옴. 8.91/8.71, 8.70/8.91 이렇게 나옴. 이유는?

prices_c = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73],"ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})
print(prices_c)
print(prices_c.iloc[1:])
print(prices_c.iloc[:-1])
print(prices_c.iloc[1:].values/prices_c.iloc[:-1])
print(prices_c.iloc[1:]/prices_c.iloc[:-1].values)

print(prices_c.shift(1))
print(prices_c/prices_c.shift(1))

print(prices_c.pct_change())

prices =pd.read_csv("COURSERA/data/sample_prices.csv")
print(prices)
returns = prices.pct_change()
print(returns)
# prices.plot() # 선 그래프
returns.plot.bar()

plt.show() # 그래프 보기
print(returns.std())
print(returns.mean())
print((((returns+1).prod()-1)*100).round(2))

#annualization
rm = 0.01
print((1+rm)**12-1)
rq = 0.04
print((1+rq)**4-1)
rd = 0.0001
print((1+rd)**252-1)
