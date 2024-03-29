#Linear Regression for predicting salaries based on years of experience

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

#Import the input data with 'Years of Experience' and 'Salary'
inputdata = pd.read_csv('Salary_Data.csv')

#Years of experience: independent variable
x = inputdata.iloc[:,:-1].values  

#Salary: dependent variable
y = inputdata.iloc[:,-1].values  


#Split data into train and test set

x_train, x_test, y_train, y_test = train_test_split(x , y, test_size = 0.33, random_state = 42)
#x_train, y_train is train set and x_test, y_test is test set


#Linear Regression

regressor = LinearRegression()
regressor.fit(x_train, y_train)    #Training the algorithm


#Predict the outcome of test sets
y_predicted = regressor.predict(x_test)
print("\nPredicted salary : ", y_predicted)


#Compare actual and predicted salaries

print("Actual Salary:\n ", y_test)
print("Predicted Salary:\n ", y_predicted)


#Calculating the accuracy of predictions. Library metrics is used.

print("Prediction Accuracy: ", metrics.r2_score(y_test, y_predicted))

#To get the intercept
print(regressor.intercept_)

#To get the slope
print(regressor.coef_)



#Calculating the difference between actual and predicted salaries

print("Difference :\n", y_predicted-y_test)

#Actual vs Predicted salaries visualization

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_predicted.flatten()})
df1 = df.head(20)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
plt.savefig('Salary Prediction.png')



#Straight line with test data

plt.scatter(x_test, y_test,  color='gray')
plt.plot(x_test, y_predicted, color='red', linewidth=2)
plt.show()
plt.savefig('Regression.png')
