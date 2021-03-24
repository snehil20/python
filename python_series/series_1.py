# program for the following series 5,54,543,5432.....
ste=[]
vgq=[]
for i in range(11):
   ste.append(i)                             

for i in range(11):
       a=str(ste[i:])
       g=a.strip('[').strip(']')      #for removing bracets and commas from the converted string
       b=g.replace(',','')
       
       vgq.append(b)
vgq.sort(reverse=True)        #for reverse order of numbers
t=" ,".join(vgq)
print(t)
