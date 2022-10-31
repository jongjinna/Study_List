
import edhec_risk_kit as erk

returns = erk.get_ffme_returns()

print(returns.head())
print(erk.drawdown(returns["SmallCap"])["Drawdown"].min())
print(erk.drawdown(returns["1975":]["SmallCap"])["Drawdown"].min())
