import scipy.io as sio
import time
from sklearn.externals import joblib
from numpy import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

"""
function fear_factor gives a value between 0 and 1 on how scared the person is
@parameter matrix is a list of alpha-theta waves
@returns a float between 0 and 1
"""
def fear_factor(matrix):#the matrix has some nan values. this needs to be fixed first
	#convert the matrix into string and replace all nan strings with 0.0
	matrix = str(matrix)
	matrix = matrix.replace('nan', '0.0')
	
	#X (1D) list created that has strings of the float values of matrix
	X = matrix[1:-1].split(',')
	#X is converted to a list of floats
	X=list(map(float, X))
	
	#import the trained ANN
	mlp = joblib.load('trained_matrix1.pkl')

	#converting X to a 2D matrix and predicting the value of fear
	predictions = mlp.predict([X])

	#return the values of fear as a float to keep conversion safe
	return float(predictions[0])
 