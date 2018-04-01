import scipy.io as sio
import time
from sklearn.externals import joblib
from numpy import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

with open("data_train3.txt", "r+") as f:
    X = []
    for line in f.readlines():
        #replace nan with 0.0 values
        X.append(line.replace('nan', '0.0'))
#X (2D) list created that has strings of the float values of matrix
X = [i.strip()[1:-1].split(',') for i in X]

#getting values of scare for the experiment
values_of_y = int(input("What is the value of y in this experiment?"))

#make y a list of integers of [X's columns x 1] matrix
y = [values_of_y for i in range(0,len(X))]

#we split the data set into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y)

"""
NORMALIZING the dataset
"""
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Instance of ANN
mlp = joblib.load('trained_matrix2.pkl')

#Training ANN
mlp.fit(X_train,y_train)


start = time.time()
#Predicting
predictions = mlp.predict(X_test)
end = time.time()

joblib.dump(mlp, 'trained_matrix3.pkl')
# print(X_test)
print("time taken={}".format(end-start) )
print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))