# -*- coding: utf-8 -*-
"""Project_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1brmhKRC3yc02jbfOL7Q_oSfzr5D-0ErW
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/annual_temp.csv')
df

df1 = df[df['Source'] == 'GCAG']
df1

df2 = df[df['Source'] == 'GISTEMP']
df2

duplicate_records = df.duplicated().sum()
print("Duplicate Records:\n", duplicate_records)

#GCAG
X = df1.iloc[:, 1:2].values
y = df1.iloc[:, -1].values

#GISTEMP
X1 = df2.iloc[:, 1:2].values
y1 = df2.iloc[:, -1].values

X

y

#SPLITTING FOR GCAG
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#SPLITTING FOR GISTEMP
from sklearn.model_selection import train_test_split
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size = 0.2, random_state = 0)

# Linear regression GCAG
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Linear regression GISTEMP
from sklearn.linear_model import LinearRegression
lin_reg1 = LinearRegression()
lin_reg1.fit(X_train1, y_train1)

#visualization GCAG
import matplotlib.pyplot as plt

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, lin_reg.predict(X_train), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

#visualization GISTEMP
import matplotlib.pyplot as plt

plt.scatter(X_train1, y_train1, color='red')
plt.plot(X_train1, lin_reg.predict(X_train1), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

# Predicting result for GCAG
print(lin_reg.predict([[2016]]))

print(lin_reg.predict([[2017]]))

# Predicting Result for GISTEMP
print(lin_reg1.predict([[2016]]))

# Predict
print(lin_reg1.predict([[2017]]))

"""**POLYNOMIAL REGRESSION**"""

# POLYNOMMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =4)
X_poly = poly_reg.fit_transform(X)
lin_reg3 = LinearRegression()
lin_reg3.fit(X_poly, y)

# POLYNOMMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
poly_reg1 = PolynomialFeatures(degree =4)
X_poly1 = poly_reg.fit_transform(X1)
lin_reg4 = LinearRegression()
lin_reg4.fit(X_poly, y1)

# VISUALIZATION
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg3.predict(poly_reg.fit_transform(X)))
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

# VISUALIZATION
plt.scatter(X1, y1, color = 'red')
plt.plot(X1, lin_reg4.predict(poly_reg.fit_transform(X1)))
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

#Predict
print(lin_reg3.predict(poly_reg.fit_transform([[2016]])))

print(lin_reg3.predict(poly_reg.fit_transform([[2017]])))

print(lin_reg4.predict(poly_reg.fit_transform([[2016]])))

print(lin_reg4.predict(poly_reg.fit_transform([[2017]])))

"""**RANDOM FOREST**"""

#RANDOM FOREST FOR CGAC
from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor1.fit(X, y)

#RANDOM FOREST FOR GSTEMP
from sklearn.ensemble import RandomForestRegressor
regressor2 = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor2.fit(X1, y1)

#VISUALIZATION  CGAC
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor1.predict(X), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

#VISUALIZATION GSTEMP
plt.scatter(X1, y1, color = 'red')
plt.plot(X1, regressor2.predict(X1), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show()

#Predict
print(regressor1.predict([[2016]]))

print(regressor1.predict([[2017]]))

print(regressor2.predict([[2016]]))

print(regressor2.predict([[2017]]))

"""**DECISION TREE**"""

#DECISION TREE
from sklearn.tree import DecisionTreeRegressor
regressor3 = DecisionTreeRegressor(random_state = 0)
regressor3.fit(X, y)

from sklearn.tree import DecisionTreeRegressor
regressor4 = DecisionTreeRegressor(random_state = 0)
regressor4.fit(X1, y1)

#VISUALIZATION
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor3.predict(X), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show

plt.scatter(X1, y1, color = 'red')
plt.plot(X1, regressor4.predict(X1), color = 'blue')
plt.title('YEAR VS MEAN')
plt.xlabel('Years')
plt.ylabel('Mean')
plt.show

#Predict
print(regressor3.predict([[2016]]))

print(regressor3.predict([[2017]]))

print(regressor4.predict([[2016]]))

print(regressor4.predict([[2017]]))