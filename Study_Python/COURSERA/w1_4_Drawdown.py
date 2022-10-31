import pandas as pd
import matplotlib.pyplot as plt

me_m = pd.read_csv("COURSERA\data\Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0, parse_dates=True, na_values=-99.99)
rets = me_m[["Lo 10", "Hi 10"]]
rets.columns = ["SmallCap", "LargeCap"]
rets = rets/100
# rets.plot.line()
# plt.show()
rets.index = pd.to_datetime(rets.index, format="%Y%m") # dtype = 'datetime64[ns]'로 나오고 1926-07-01처럼 일도 나옴
rets.index = rets.index.to_period("M") # dtype='period[M]'으로 나오고 1926-07까지 나옴 / to_period를 쓰기 위해서 to_datetime으로 바꾼 뒤 사용
print(rets.head())
print(rets["1975"]) #period로 했을 경우 특정 년도를 볼 수 있음
print(rets.info())

wealth_index = 1000*(1+rets["LargeCap"]).cumprod()
print(wealth_index.head())
# wealth_index.plot.line()
# plt.show()
previous_peaks = wealth_index.cummax()
print(previous_peaks)
# previous_peaks.plot.line()
# plt.show()
drawdown = (wealth_index - previous_peaks)/previous_peaks
drawdown.plot()
plt.show()

print(drawdown.head())
print(drawdown.min())
print(drawdown["1975":].idxmin())
print(drawdown.idxmin())

def drawdown(return_series: pd.Series):
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index, "Peaks": previous_peaks, "Drawdown": drawdowns})

print(drawdown(rets["LargeCap"]).head())
print(drawdown(rets["LargeCap"])[["Wealth", "Peaks"]])
# drawdown(rets["LargeCap"])[["Wealth", "Peaks"]].plot()
# plt.show()
# drawdown(rets[:"1950"]["LargeCap"])[["Wealth", "Peaks"]].plot()
# plt.show()
print(drawdown(rets["LargeCap"])["Drawdown"].min())
print(drawdown(rets["SmallCap"])["Drawdown"].min())
print(drawdown(rets["LargeCap"])["Drawdown"].idxmin())
print(drawdown(rets["SmallCap"])["Drawdown"].idxmin())
print(drawdown(rets["1975":]["LargeCap"])["Drawdown"].min())
print(drawdown(rets["1975":]["LargeCap"])["Drawdown"].idxmin())
print(drawdown(rets["1975":]["SmallCap"])["Drawdown"].min())
print(drawdown(rets["1975":]["SmallCap"])["Drawdown"].idxmin())