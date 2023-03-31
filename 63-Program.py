#Write a multiplation table using for loop
import os
os.system('cls')
n=int(input('Enter the number which multiplication table you want : '))

for i in range(1,11):

 print(n,' * ',i,' = ',n*i)