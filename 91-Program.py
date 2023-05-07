import os
os.system('cls')

def per(marks):
 p =((sum(marks)/500)*100) 
 return p    

marks = [85,95,88,99,100]
percentage=per(marks)
print(percentage)

marks2 = [55,65,78,89,66]
percentage2=per(marks2)
print(percentage2)