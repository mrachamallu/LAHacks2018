import scipy.io as sio
import time
from numpy import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix


trained_matrix = open("trained_matrix", "w+")

with open("data_train1.txt", "r+") as f:
    X = []
    for line in f.readlines():
        #line.replace('nan,', '0.0')
        X.append(line.replace('nan', '0.0'))

X = [i.strip()[1:-1].split(',') for i in X]



#is it a scary activity or not
values_of_y = int(input("What is the value of y in this experiment?"))
#make y a list of integers of X's columns by 1

y = [values_of_y for i in range(0,len(X))]
print("length o fX", len(X), y)

X = array(X)

# where_are_NaNs = isnan(X)
# X[where_are_NaNs] = 0
for i in range(0,len(X)-1):
    X[i] = array(X[i])
    X[i] = nan_to_num([float(j) for j in X[i]])

# print(X)
"""
import the X dataset
import the y dataset
"""

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
mlp = MLPClassifier(hidden_layer_sizes=(30,30,30))

#Training ANN
mlp.fit(X_train,y_train)

start = time.time()
#Predicting
predictions = mlp.predict(X_test)
end = time.time()
# print(X_test)
print("time taken={}".format(end-start) )
print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))