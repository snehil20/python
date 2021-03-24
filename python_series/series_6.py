#program for series 55555,4444,333,22,1....
tyu=[]
for i in range(1,6):
    a=str(i)            #converting i to string and storing the value in a
    tyu.append(a*i)      #for repetation

tyu.sort(reverse=True)
abc=",".join(tyu)
print(abc)
