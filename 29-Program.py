import os
os.system('cls')
a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
c=int(input("Enter the number 3 : "))

#if-if
if(a!=b):
    print(a,"is not equal to ",b)
if(b!=c):
    print(b,"is not equal to ",c)    
if(c!=a):
    print(c,"is not equal to ",a)


#if-if using and logic operator
if(a>b and a>c):
    print(a," is big")
if(b>a and b>c) :
    print(b," is big")
if(c>a and c>b) :
    print(c," is big")    


    
    
