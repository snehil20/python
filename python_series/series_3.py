#program for series 1,101,1010.......
ghj=[]
lkj=[]
for i in range(11):
   ghj.append(1)                       #creating a list for series 1010101...           
   ghj.append(0)
   b="".join(map(str,ghj))
for i in range(11):
   lkj.append(b[0:i])           #slicing list from 1st to last element of the list.
   t=",".join(lkj)
print(t)
