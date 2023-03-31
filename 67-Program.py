#Write a program to print the first n natural number using while loop
import os
os.system('cls')
n=int(input('Enter the nth natural number :'))
sum=0
while n>0:
    sum=sum+n
    n=n-1
    print(sum)