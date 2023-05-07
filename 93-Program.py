# n! = 1*2*3*4..........*n
import os
os.system('cls')
n = input("Enter the number : ")
n=int(n)
pro = 1
for i in range(n):
 pro = pro *(i+1)
 print(pro)

 