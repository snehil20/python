# printing upto 100 without using a single number "not even in range function"

a=format(True,"d")   # for boolean 1 to decimal
b=format(False,"d")  #for boolean 0 to decimal
sA=str(a)
sB=str(b)
string_hun=sA+sB+sB          # string 100
string_hun=int(string_hun)   # 100 string to int value
a=int(a)
string_hun=string_hun+a      # 101 intiger
for i in range(string_hun):
    print(i)
