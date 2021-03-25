# simple bubble sort
ls=[1,2,3,7,10,9,8,5,5,7,8,7,9]
for i in range(7):               #for no of times of filteration or comparision
    for i in range(len(ls)-1):
        if ls[i]>ls[i+1]:
            a=ls[i+1]
            b=ls[i]              #interchanging the values of ls[i] wth its next element
            ls[i]=a
            ls[i+1]=b


print(ls)
