import pandas as pd
import matplotlib.pyplot as plt
import edhec_risk_kit as erk

ind = erk.get_ind_returns()
# erk.drawdown(ind["Food"])["Drawdown"].plot.line(figsize=(12,6))
# cols_of_interest = ["Food", "Smoke", "Coal", "Beer", "Fin"]
# print(erk.var_gaussian(ind[cols_of_interest],modified = True))
# print(erk.var_gaussian(ind,modified = True).sort_values().tail())
# print(erk.var_gaussian(ind,modified = True).sort_values().head())
# erk.var_gaussian(ind,modified = True).sort_values().plot.bar()
erk.sharpe_ratio(ind["2000":], 0.03,12).sort_values().plot.bar(title = "Industry Sharp Ratio 1926-2018", figsize=(12,5) ,color="goldenrod")
plt.show()
cov = ind["1995":"2000"].cov()
print(cov)