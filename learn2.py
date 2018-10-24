# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("check1.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0]
Y = dataset[:,1]
# create model

model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
model.add(Dense(1, activation='relu'))
# Compile model
model.compile( loss = "binary_crossentropy",optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]))
