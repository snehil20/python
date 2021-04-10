%tensorflow_version 2.x
!pip install tensorflow_probability==0.8.0rc0 --user --upgrade    #use if tensorflow_probability library doesn't work
import tensorflow_probability as tfp
import tensorflow as tf
tfd = tfp.distributions                        #up      #down
initial_distribution = tfd.Categorical(probs=[0.5439, 0.4561])  #creating a list of percentage of stocks go up and down down
transition_distribution = tfd.Categorical(probs=[[0.4776, 0.5224], #for stocks going up     #storing percentage of stocks that will go up or down based on the previous stocks
                                                 [0.4287,0.5713]])  #for stocks going down
observation_distribution = tfd.Normal(loc=[168.75, 168.33], scale=[2.19, 2.07])  # the loc argument represents the mean and the scale is the standard devitation
 #168.75 is the mean of all stocks that go up and 168.33 is the mean of all stocks that go down. 2.19 and 2.07 is the standard deviation respectively

model = tfd.HiddenMarkovModel(                             #sub method of distribution module in tensorflow_probability library which is use for the creation of HMM
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=7)
mean = model.mean()          #mean() is use to extract the predicted mean value from our model


# from within a session to see the value of this tensor

# in the new version of tensorflow we need to use tf.compat.v1.Session() rather than just tf.Session()
with tf.compat.v1.Session() as sess:
  
  b=", ".join(map(str,mean.numpy()))
  print("Predicted list of future stocks:",'\033[92m'+ b)                                     #printing an output  of our predicted stocks value
