# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# importing the dataset
dataset = pd.read_csv('dataFinal.csv')

#Taking 100 values
x = dataset.iloc[:19700, 0:1].values   # independent - Price
y = dataset.iloc[:19700, -1].values  # dependent - Change

# split into training dataset and test dataset
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
print(y_pred)
filename = 'finalized_model.sav'
pickle.dump(regressor, open(filename, 'wb'))
