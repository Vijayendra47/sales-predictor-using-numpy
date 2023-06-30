import numpy as numpy
from sklearn.linear_model
import linearRegression

#Training data
X_train=np.array([50][150][200][250][300][350][400]])
#Advertising expenditure
y_train=np.array([30,60,80,100,150])
#sales

#Create and train the linear_modelmodel=linearRegression()
model.fit(X_train,y_train)

#test data
X_test=np.array([[480][580]])
#Adverstising expenditure for prediction

#Make predictions
y_pred=model.predict(X_train)

#print the predicted sales for i in range (len ( X_test ) ):
print("predicted salesvfor advertising expenditure $", X_test[i][0],":",y_pred)


