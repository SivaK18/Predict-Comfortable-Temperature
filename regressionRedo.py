import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle
import sys
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
k=sys.argv[1]
filename = 'finalized_model.sav'
X=np.array([24,30,15,20])
Y=X[0:1]
i=float(k)
#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)
loaded_model = pickle.load(open(filename, 'rb'))
#warnings.filterwarnings("ignore", category=DeprecationWarning)
result = loaded_model.predict([[i]])
print("The LinearRegression predicted value is.. ",result)
