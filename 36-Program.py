#Write a program to find a given username contains less then 10 char or not.
import os
os.system('cls')
un=input("Enter You Username : ")
print("Characters : ",len(un))
if(len(un)<10):
    print("Username containing less then 10 characters.")
else:
    print("Username containing more then 10 characters.")