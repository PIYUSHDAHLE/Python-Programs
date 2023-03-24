#Write a program to enter the 4 student marks and then print the highest marks in maths
import os
os.system('cls')
print("Enter the 4 student marks in maths out of 100\n")

s1=int(input("Enter the student 1 marks : "))
s2=int(input("Enter the student 2 marks : "))
s3=int(input("Enter the student 3 marks : "))
s4=int(input("Enter the student 4 marks : "))

if(s1>s2 and s1>s3 and s1>s4) :
    print(s1,"is the highest marks of student 1")
elif(s2>s1 and s2>s3 and s2>s4) :
    print(s2,"is the highest marks of student 2")
elif(s3>s2 and s3>s1 and s3>s4) :
    print(s3,"is the highest marks of student 3")
elif(s4>s2 and s4>s3 and s4>s1) :
    print(s4,"is the highest marks of student 4")    

#other way to code 
if(s1>s2):
    f1=s1
else:
    f1=s2
    
if(s3>s4):
    f2=s3
else :
    f2=s4
        
    if(f1>f2):
        print(f1," is the highest marks")    
    else:
        print(f2," is the highest marks")



