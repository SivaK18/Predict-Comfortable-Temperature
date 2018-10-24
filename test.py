
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import numpy as np
x = np.array([24,30,15,20])
model = load_model('my_model.h5')
y = model.predict(x)
for i in y :
    print(i*2+7)
