from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("dataFinal.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0]
Y = dataset[:,1]
#labels = numpy.random.randint(2, size=(1000, 1))
#print(labels)
# create model
model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
model.add(Dense(1, activation='relu'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=15000, batch_size=100)
# calculate predictions
predictions = model.predict(X)
# round prediction
for i in range(0,770):
    print(predictions[i]*3,' is predicted for ',X[i])

model.save('my_model2.h5')  # creates a HDF5 file 'my_model.h5'
del model
