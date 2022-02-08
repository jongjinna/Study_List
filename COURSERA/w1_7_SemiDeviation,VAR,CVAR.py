import pandas as pd
import edhec_risk_kit as erk
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

hfi = erk.get_hfi_returns()
print(hfi.std(ddof=0))
print(hfi[hfi<0].std(ddof=0))
print(erk.semideviation(hfi))
print(np.percentile(hfi, 5, axis=0))

def var_historic(r, level = 5):
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level = level)
    elif isinstance(r, pd.Series):
        return np.percentile(r, level)
    else:
        raise TypeError("Expected r to be Series or DataFrame")

print(var_historic(hfi))
print(erk.var_historic(hfi))

print(erk.var_gaussian(hfi))
var_list = [erk.var_gaussian(hfi), erk.var_gaussian(hfi, modified = True), erk.var_historic(hfi)]
comparison = pd.concat(var_list, axis=1)
comparison.columns = ["Gaussian", "Cornish-Fisher", "Historic"]
comparison.plot.bar(title="EDHEC Hedge Fund Indices: VaR")
plt.show()

print(erk.cvar_historic(hfi))