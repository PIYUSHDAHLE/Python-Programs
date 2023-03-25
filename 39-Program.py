#Write a program to find out whether a given post is talking about "Piyush" or not.
import os
os.system('cls')
post=input("Enter The Post :\n")

if("Piyush" in post or "PIYUSH" in post or "piyush" in post):
    print('Yes, in this post is talking about Piyush ')
else:
      print('NO, in this post is not talking about Piyush ')