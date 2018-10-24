
from keras.models import load_model
import sys
def warn(*args, **kwargs):
    pass
import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
warnings.warn = warn
k=sys.argv[1]
x = np.array([k])
model = load_model('my_model2.h5')
y = model.predict(x)
for i in y :

    print("The keras model prediction using tensorflow is .. ",i*1.38+12.2)
