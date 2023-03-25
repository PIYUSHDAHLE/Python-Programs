#Write a program to calculate the grade of the student A+, A, B+,...etc
import os
os.system('cls')
marks=int(input("Enter the marks of student : "))
if(90<marks<=100):
    print("A+ Grade")
elif(80<marks<=90):
    print("A Grade")
elif(70<marks<=80):
    print("B+ Grade")
elif(60<marks<=70):
    print("B Grade")
elif(50<marks<=60):
    print("C+ Grade")    
elif(40<marks<=50):
    print("C Grade")
elif(marks<40):
    print("D Grade")    
