import os
os.system('cls')
a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
c=int(input("Enter the number 3 : "))

#if-else-if-else statement else-if(elif)
if(a>b and a>c):
    print(a," is the largest number ")
elif(b>a and b>c) :
    print(b," is the largest number ")
elif(c>a and c>b) :
    print(c," is the largest number ")