import scipy.io as sio
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

mat_contents = sio.loadmat('ex4data1.mat')

X = mat_contents['X']
y = mat_contents['y']


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
#
print("time taken={}".format(end-start) )
print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))