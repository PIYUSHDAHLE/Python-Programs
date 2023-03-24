#Write a program to check the student was fail or pass in 3 subject percentage the passing percentage is 40% and at least 33%
import os
os.system('cls')
sub1=int(input("Enter the subject 1 marks out of 100 :"))
sub2=int(input("Enter the subject 2 marks out of 100 :"))
sub3=int(input("Enter the subject 3 marks out of 100 :"))
per=((sub1+sub2+sub3)/300)*100
if(sub1<33 or sub2<33 or sub3<33):
 print("---fail----\nSorry you are fail in any one or more subject.")
elif(per>=40):
    print("---Pass---- with percentage of ",per,"%")
else:
    print("---Fail---- with percentage of ",per,"%")