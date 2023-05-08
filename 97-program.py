import os
os.system('cls')

def max(n1,n2,n3):
    if(n1>n2):
      if(n1>n3):
       return n1
      else:
        return n3
    else:

      if(n2>n3):
       return n2
      else:
        return n3 

n1=input("enter the 1st number :")
n2=input("enter the 2nd number :")
n3=input("enter the 3rd number :")

m=max(n1,n2,n3)
print("The maximun number is "+str(m))