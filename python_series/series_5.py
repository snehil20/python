#program for series 1,12,123,1234....
tyu=[]  
ghj=[]
for i in range(1,10):            
   tyu.append(i)
   t=str(tyu[:i])           #slicing the list
   t=t.strip('[').strip(']')              
   t=t.replace(',','')
   ghj.append(t)            #storring the sliced elements inside the list
   gh=" , ".join(map(str,ghj))

print(gh)
