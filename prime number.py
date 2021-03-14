def abc():
 global n
 n=int(input("choose a number to check prime or not: "))
 for i in range(2,n):
                   if n%2==0:
                            return True
                            break
                   elif n%i==0:
                             return True
                             break

if abc()==True:
             print("not prime")
elif n==1 or n==0:
                 print("not prime")
elif n==2:
         print("prime")

else:
    print("prime")
                