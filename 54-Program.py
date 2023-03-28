#Multiplication table 
import os
os.system('cls')
n=int(input("Enter the number :"))
table=0
while table<10:
    table+=1
    print(n," * ",table," = ",n*table)