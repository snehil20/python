print("List of the planets:\n1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune")
n=int(input("choose a planet from the list to find its gravitational force from the sun :"))
planets={1:"Mercury",2:"Venus",3:"Earth",4:"Mars",5:"Jupiter",6:"Saturn",7:"Uranus",8:"Neptune"}
g=6.673/(10**11)
m1=1.989*(10**30)


if n==1:

       m2= 0.33*(10**24)
       d=70*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff="{:.1f}".format(f)
       print("Gravitational force between sun and", planets[1], "is :",ff,"N")
elif n==2:

       m2=4.867*(10**24)
       d=109*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[2], "is :",ff,"N")
elif n==3:

       m2=5.972*(10**24)
       d=152*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[3], "is :",ff,"N")
elif n==4:

       m2=0.65*(10**24)
       d=249*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[4], "is :",ff,"N")
elif n==5:

       m2=1900*(10**24)
       d=817*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[5], "is :",ff,"N")
elif n==6:

       m2=570*(10**24)
       d=1510*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[6], "is :",ff,"N")
elif n==7:

       m2=87*(10**24)
       d=3000*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.1f}".format(f)
       print("Gravitational force between sun and", planets[7], "is :",ff,"N")
elif n==8:

       m2=100*(10**24)
       d=4550*(10**6)
       f = (g * m1 * m2) / (d ** 2)
       ff = "{:.f}".format(f)
       print("Gravitational force between sun and", planets[8], "is :",ff,"N")
else:
    print("invalid selection")

print("Here 'N' is newton")

