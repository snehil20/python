# Bag of words: A simple algorithm to find the frequency of each word in a paragraph or in a dataset.
# can be use to feed the data to RNN based machine learning model.


string=str(input("Enter your paragraph:"))   #load your dataset here
checker=string.split()



dict1={}          #Bag/dictionary
for i in range(len(checker)):
    dict1[i]=string.count(checker[i])


for i in range(len(dict1)):
    dict1[checker[i]]=dict1[i]
    del dict1[i]
print("Here is the bag of each word respectively:",dict1)                
