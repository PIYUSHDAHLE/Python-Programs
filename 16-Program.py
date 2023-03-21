#Write a program to add the list element
import os
os.system('cls')
n1=int(input("ENTER NUMBER 1 : ")) 
n2=int(input("ENTER NUMBER 2 : ")) 
n3=int(input("ENTER NUMBER 3 : ")) 
n4=int(input("ENTER NUMBER 4 : ")) 
n5=int(input("ENTER NUMBER 5 : ")) 
list=[n1,n2,n3,n4,n5]
#1st way to add the list
print(list[0] + list[1] + list[2])
#2nd way to add the list
print(sum(list))
