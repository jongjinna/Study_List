import matplotlib.pyplot as plt #그래프
import numpy as np #행렬 matrix 등등
from scipy import stats #분석(회귀분석)
import pandas as pd #scv파일 가지고오기
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# 선형회귀모형
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#   return slope * x + intercept

# mymodel = list(map(myfunc, x))

# speed=myfunc(10)
# print(speed)
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

# 곡선회기분석

# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
# # x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# # y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel = np.poly1d(np.polyfit(x, y, 3))

# myline = np.linspace(5, 95, 1000)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()

# print(r2_score(y, mymodel(x))) # 정확도? 얼마나 잘 반영하는지

# file_path = 'C:/Users/njjwa/Desktop/Code_Blue/Doing now/W3SCHOOL/py_machine_learning/cars.csv'
# df = pd.read_csv(file_path)

# scale = StandardScaler()

# X = df[['Weight', 'Volume']]
# y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)


# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedCO2 = regr.predict([[2300, 1300]])

# print(predictedCO2)


#print(regr.coef_)

# scaledX = scale.fit_transform(X)
# regr = linear_model.LinearRegression()
# regr.fit(scaledX, y)

# scaled = scale.transform([[2300, 1.3]])

# predictedCO2 = regr.predict([scaled[0]])
# print(predictedCO2)


# Train & Test
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

myline = np.linspace(0, 6, 100)

r2 = r2_score(train_y, mymodel(train_x))

print(r2)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()