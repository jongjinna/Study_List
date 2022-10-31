import pandas as pd
import scipy.stats
import numpy as np
import edhec_risk_kit as erk

hfi = erk.get_hfi_returns()
print(pd.concat([hfi.mean(), hfi.median(), hfi.mean()>hfi.median()], axis=1))
print(erk.skewness(hfi).sort_values())
print(scipy.stats.skew(hfi))
print(scipy.stats.kurtosis(hfi))
print(erk.skewness(hfi))
print(erk.kurtosis(hfi).sort_values())
normal_rets = np.random.normal(0, .15, size = (26300,1))
print(erk.skewness(normal_rets))
print(erk.kurtosis(normal_rets))
print(scipy.stats.skew(normal_rets))
print(scipy.stats.kurtosis(normal_rets))

print(scipy.stats.jarque_bera(normal_rets))
print(scipy.stats.jarque_bera(hfi))

print(erk.is_normal(normal_rets))
print(hfi.aggregate(erk.is_normal))

ffme = erk.get_ffme_returns()
print(ffme)
print(erk.skewness(ffme))
print(ffme.aggregate(erk.skewness))
print(erk.kurtosis(ffme))
print(ffme.aggregate(erk.kurtosis))
print(ffme.aggregate(erk.is_normal))