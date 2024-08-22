import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

curDir = os.getcwd()
os.chdir(curDir)

dataSet = pd.read_csv('PositionSalaries.csv')
x = dataSet.iloc[: , 1:2].values
y = dataSet.iloc[: , 2].values

LinearResgression = LinearRegression()
LinearResgression.fit(x, y)
yPred = LinearResgression.predict(x)

plt.scatter(x, y, color = 'red')
plt.plot(x, yPred, color = 'blue')
plt.title('(Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

polyRegression = PolynomialFeatures(degree = 4)
xPoly = polyRegression.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(xPoly, y)
X_poly_pred = lin_reg_2.predict(xPoly)

plt.scatter(x, y, color = 'red')
plt.plot(x, X_poly_pred, color = 'blue')
plt.title('(Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()