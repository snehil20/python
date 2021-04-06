# MAHINDRA INTERVIEW  PROGRAMMING Question 2021 : Convert a list of inches to feet and returns sum of all feet:
# Sample Input: 4(size of list), [24,45,67,89]
#24-->2 feet, 45-->3 feet, 67--->5 feet, 89--->7feet
#output: 2+3+5+7=17feet

#Sollusion
n=int(input())   #user input for size/length of list
a=[]             #declairing empty list of inches
for i in range(n):       #user input for the list of inches
    inp=int(input())
    a.append(inp)




inch=[]             #list of range of all posibble values for inches
for i in range(12,156,12):
    inch.append(i)

#inch
feet=[]        #declairing list of output for feet
for i in range(len(a)):
    for j in range(len(inch)):
        if a[i]>=inch[j] and a[i]<inch[j+1]:
                                    #compairing each element of inches list(a) to all posible values for inches of the list(inch)
            feet.append(j+1)        #storring the value of feet in the list feet
        elif a[i]<12:
            feet.append(0)
            break



for i in range(len(feet)-1):    #for caluculating the sum of all elements in the list(feet)
    s=feet[i]+feet[i+1]
    feet[i+1]=s
print(s)
