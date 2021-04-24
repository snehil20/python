#Encoder and Decoder for NLP or other uses

a=open("C:\\Users\\snehi\\Desktop\\New folder (3)\\words.txt","r") #a text file(container/bag) contains millions of english words
with a as b:
    c=b.read()
c=c.lower()
c=c.split()

c.append("Snehil")
# c.append("Your word") ......add your own words if it is not present in the bag





#encoding

default=c    #load the box of words or statements


encoded=[]
for i in range(len(default)):     #encoding the value of default with the multiple of 2. User can implement their own algo to encode these words
    a=i*2

    encoded.append(a)

UserInput=str(input("Write a statement to encode:"))  #User define string to encode with respective to the default
UserInput=UserInput.split()
encoded2=[]
for i in range(len(UserInput)):
   for j in range(len(default)):
       if UserInput[i]==default[j]:
           encoded2.append(encoded[j])   #encoded value of the user defined input
print("The encoded value of the user define string:",encoded2)


#decoding
decodedList=[]
for i in range(len(encoded2)):        #decoding the user define string to its original format
    for j in range(len(encoded)):
        if encoded2[i]==encoded[j]:

            decodedList.append(default[j])    #storing encoded values to a list







decodedList=" ".join(decodedList)
print("The decoded string :",decodedList)              #Final decoded string
# print("The encoded values of each word for our bag of words(Just for the reference):",encoded)
