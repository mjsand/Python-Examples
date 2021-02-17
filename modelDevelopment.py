## practice exercise on model development


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#defining data path and creating dataframe
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
display(df.head())

#creating a linear regression model for highway-mpg and price
lm = LinearRegression()
lm
X1 = df[['highway-mpg']]
Y = df['price']
lm.fit(X1,Y)
Yhat_highway_mpg = lm.predict(X1)
print(lm.intercept_)
print(lm.coef_)
#sns.regplot(X1,Y).set_title('Price as a function of Highway Mpg')


#creating new linear regression model
lm2 = LinearRegression()
lm2
X2 = df[['engine-size']]
lm2.fit(X2,Y)
Yhat_engine_size = lm2.predict(X2)
print(lm2.intercept_)
print(lm2.coef_)
#sns.regplot(X2,Y).set_title('Price as a function of Engine Size')

#creating and performing multiple linear regression for better accuracy
lm3 = LinearRegression()
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm3.fit(Z, Y)
Yhat_Z = lm3.predict(Z)
print(lm3.intercept_)
print(lm3.coef_)
ax1 = sns.distplot(df['price'], hist=False, color='r', label='Actual Value')
sns.distplot(Yhat_Z, hist=False, color='b', label='Fitted Values', ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price in Dollars')
plt.ylabel('Proportion of Cars')
plt.show()
plt.close()

#residual plots
'''width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()'''

#polynomial regression plot

def PlotPolly(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    
    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')
    
    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)
PlotPolly(p, x, y, 'highway-mpg')


# Write your code below and press Shift+Enter to execute 
f2 = np.polyfit(x, y, 11)
p2 = np.poly1d(f2)
print(p2)
PlotPolly(p2, x, y, 'Highway-MPG')

pr = PolynomialFeatures(degree=2)
pr
Z_pr = pr.fit_transform(Z)
Z.shape
Z_pr.shape

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
pipe = Pipeline(Input)
pipe
pipe.fit(Z,y)
ypipe = pipe.predict(Z)
ypipe[0:4]


Input2 = [('scale', StandardScaler()), ('model', LinearRegression())]
pipe2 = Pipeline(Input2)
pipe2.fit(Z, y)
ypipe2 = pipe2.predict(Z)
ypipe2[0:10]


#calculating R^2 values
lm.fit(X1,Y)
print('THe R-squared is: ', lm.score(X1, Y))
Yhat = lm.predict(X1)
print('The output of the first four predicted value is: ', Yhat[0:4])


#calculating mean squared error
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)

#fit the model
lm.fit(Z, df['price'])
# calculating the R^2
print('The R-squared is: ', lm.score(Z, df['price']))

#calculate the mean squared error
Y_predict_multifit = lm.predict(Z)
print('The mean squared error of price and predicted value using multifit is: ', mean_squared_error(df['price'], Y_predict_multifit))

#another way of calculating the r^2
from sklearn.metrics import r2_score

r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)

#calculate the mse
mean_squared_error(df['price'], p(x))

#creating a prediction method model
import matplotlib.pyplot as plt
import numpy as np

new_input = np.arange(1, 100, 1).reshape(-1, 1)
lm.fit(X1, Y)

yhat = lm.predict(new_input)
yhat[0:5]
plt.plot(new_input, yhat)
plt.show()

## we can conclude from our plots, R-squared, and MSE values that the multiple linear regression model 
## was the best fit for this dataset at predicting the price of a car


































