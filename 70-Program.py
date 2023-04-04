#write a program to print the factorial number.
#5!=1*2*3*4*5
import os
os.system('cls')
n=int(input("Enter the number : "))
fa = 1
for i in range(1,n+1):
    fa = fa * i
    print(f"The factorial is {fa}")
