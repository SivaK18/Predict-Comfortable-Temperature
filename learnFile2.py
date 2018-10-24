import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
dataframe = pandas.read_csv('dataFinal.csv')
array = dataframe.values
X = array[:,0:1]
Y = array[:,1]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on 33%
model = LogisticRegression()
model.fit(X_train, Y_train)
# save the model to disk
predictions=model.predict(X_test)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
