lstparent=[]
lstson = []
n=int(input(" add no of parents and sons to analyse : "))                 #for 2 parents and their 2 sons n will be 2
for i in range(n//2):
    parent=str(input("add father first name :"))
    parentlast = str(input("add father last name :"))

    lstparent.append(parent)
    lstparent.append(parentlast)

for t in range(n//2):
    son = str(input("add son first name:"))
    sonlast = str(input("add son last name:"))
    lstson.append(son)
    lstson.append(sonlast)


for f in range(1,n,2):                                                            #this script will check for the surname of the father and the son
    if lstparent[f]==lstson[f]:
        print(lstparent[f-1],lstparent[f],"is father of",lstson[f-1],lstson[f])

