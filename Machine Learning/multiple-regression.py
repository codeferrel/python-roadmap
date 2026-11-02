
# Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.
import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2) 
