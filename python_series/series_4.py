# program for series ......1357,135,13,1
stu=[]
ghj=[]
for i in range(1,11):                                        
   if i%2!=0:
    stu.append(i)                                   #for list of odd numbers 1,3,5,7...
for i in range(6):
   a=str(stu[:i])                                   #slicing through the list till the last element
   b=a.replace('[','').replace(']','').replace(',','')    #removing commas and brackets from the slicesed list element
   ghj.append(b)
   ghj.sort(reverse=True)              #for reverse order
   q=",".join(ghj)
print(q)
