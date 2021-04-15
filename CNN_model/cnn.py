%tensorflow_version 2.x  # this line is not required unless you are in a notebook

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

#  LOAD AND SPLIT DATASET
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data() 
#using CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

   

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',               #declairing the list of the names of various image clases
               'dog', 'frog', 'horse', 'ship', 'truck']


#building model
model = models.Sequential()                                                       #declairing various convolutional layer in our model.
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))                           #using rectifier linear function as an activation function
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))                           

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.summary()                                        #shows how many paterns are predicted through each convolutional layers 


model.compile(optimizer='adam',                                                          #compiling the model
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=4,                    #training the model. change the no of epocs to create more accurate model
                    validation_data=(test_images, test_labels))
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_acc)                                                              #printing the accuracy of our model

import numpy as np

image_selection=int(input("Select the position of the image from the dataset to predict :"))   #tanking the position of the image to predict from the user

predictions = model.predict(test_images)               
b=np.argmax(predictions[image_selection])          #for the maximum predicted index value 

print("The predicted image is: ", class_names[b]) #returning the index value to our class_names list 


plt.imshow(test_images[image_selection] ,cmap=plt.cm.binary) #displaying our selected image

plt.show()
print("The image is in a very low poly format because of 32 x 32 dimension")
