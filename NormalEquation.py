import pandas as pd
import numpy as np
import os 

curDir = os.getcwd()
os.chdir(curDir)

dataSet = pd.read_csv('MarketData.csv')
AfterDrop = dataSet.drop('sales', axis =1 )
np_array = AfterDrop.to_numpy()

y  = dataSet['sales']
x1 = dataSet['youtube']
x2 = dataSet['facebook']
x3 = dataSet['newspaper']

length = len(x1)      
xAdded = np.ones((length, 1))
xAppend = np.append(xAdded ,np_array, axis = 1) 

xTrans = np.transpose(xAppend)
xTransDotX = xTrans.dot(xAppend)
xTransInv = np.linalg.inv(xTransDotX)
xTransInvDotY = xTrans.dot(y)
theta = xTransInv.dot(xTransInvDotY)

theta_0 = theta[0]
print(theta_0)

theta_1 = theta[1]
print(theta_1)

theta_2 = theta[2]
print(theta_2)

theta_3 = theta[3]
print(theta_3)

def pred_values(theta_0, theta_1, theta_2, theta_3, youtube, facebook, newspaper) :
    predicted_value = theta_0 + (youtube * theta_1) + (facebook * theta_2) + (newspaper * theta_3)
    return predicted_value

youtube = 84.72
facebook = 19.20
newspaper = 48.96
print(pred_values(theta_0,theta_1,theta_2,theta_3,youtube,facebook,newspaper))

youtube =351.48
facebook = 33.96
newspaper = 51.84
print(pred_values(theta_0,theta_1,theta_2,theta_3,youtube,facebook,newspaper))

youtube = 29
facebook = 93
newspaper = 96
print(pred_values(theta_0,theta_1,theta_2,theta_3,youtube,facebook,newspaper))