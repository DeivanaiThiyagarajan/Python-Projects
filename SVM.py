from sklearn.svm import SVC
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class SVM():
    def __init__(self):
        self.w = 0
        self.b = 0
    def hinge_loss(self,w,b,x,y):
        summ=0
        for i in range(x.shape[0]):
            #print(x[i].shape,y[i],w.shape)
            reg = y[i]*(np.dot(w,x[i])-b)
            loss = max(0,1-reg)
            summ+=loss
        return loss/x.shape[0]
    def fit(self,x,y,learning_rate = 0.01):
        epochs = 10
        batch_size = 100
        total_samples = x.shape[0]
        total_features = x.shape[1]
        w=np.zeros((1,total_features))
        b=0
        losses=[]
        for i in range(epochs):
            loss = self.hinge_loss(w,b,x,y)
            losses.append(loss)
            for j in range(0,total_samples,batch_size):
                gradw = 0
                gradb = 0
                for k in range(j,batch_size):
                    if(k<total_samples):
                        ti = y[k]*(np.dot(w,x[k])-b)

                        if(ti>1):
                            gradw +=0
                            gradb +=0
                        else:
                            gradw += y[k]*x[k]
                            gradb += y[k]
                w = w - learning_rate*w+learning_rate*gradw
                b = b + learning_rate * gradb
            print('Epoch-1 Done')
        self.w = w
        self.b = b
        return self.w,self.b,losses

