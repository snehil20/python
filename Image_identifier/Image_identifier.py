%tensorflow_version 2.x  # this line is not required unless you are in a notebook
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist  # load dataset (using a default keras image datashit which contains 60000 various images)

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # split into tetsing and training

 
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',              #creating a class for the different names of the images
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # input layer (1)
    keras.layers.Dense(128, activation='relu'),  # hidden layer (2)    # I used Relu (Rectified Linear Unit) activation function here to eliminate all -ve values 
    keras.layers.Dense(10, activation='softmax') # output layer (3)    
])

model.compile(optimizer='adam',                                            #we can use different optimizers to update the values of biases and weights to get the least value for our loss
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=3)  # we pass the data, labels and epochs to train the model. We can set different values for epocs to make model more accurate
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1)    #passing our test data and labels to check accuracy of the model in the func evaluate()

print('our model accuracy:', test_acc)

imp=int(input("choose a position of image  to predict:"))       #taking the location of the image to predict it's class

predictions = model.predict(train_images)


p=np.argmax(predictions[imp])             #predicting the index for the image class

for i in range(len(class_names)):
  if i==p:                                                    
    print("The predicted image is:",class_names[i])
    break


plt.figure()                                               #displaying the predicted image name and the input image
plt.imshow(train_images[imp])
plt.colorbar()
plt.grid(False)
plt.show()



