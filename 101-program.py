import os
os.system('cls')

def addition(n) :
 if(n==1 or n==0):
     return 1
 return n + addition(n-1)
n1=input("Enter the number : ")
n1=int(n1) 
a = addition(n1)
print("The sum of factorial number ",n1," is ",a)