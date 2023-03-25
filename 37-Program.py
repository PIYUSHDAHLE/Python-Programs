#Write a program to find the name is in the list or not
import os
os.system('cls')
name=input("Enter The Name In Capital : ")
names=['PIYUSH','RAHUL','MAYANK','ABHI']
if(name in names):
    print("Yes,",name,"name in the list.")
else:
    print("No,",name,"name is not in the list.")