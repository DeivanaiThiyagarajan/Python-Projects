import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from SVM import SVM

path = 'C:/Users/Aishu/Downloads/Programming in python assignments/Mini Project - 1/tic-tac-toe dataset/Tic tac initial results.csv'
df = pd.read_csv(path,sep=',')
X = df.iloc[:,0:7]
x = X.to_numpy()

Y = df['CLASS']
y = Y.to_numpy()

x = np.where(x=='?',-1,x)
x = x.astype(int)
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        x[i][j] +=1
y = np.where(y=='win',1,-1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)

svm = SVM()

w,b,losses = svm.fit(x_train,y_train)

def predict(x):
    prediction = np.dot(w[0],x)-b
    return np.sign(prediction)

prediction = predict([4,8,0,0,0,0,0])
print([4,8,0,0,0,0,0])
print(prediction)
