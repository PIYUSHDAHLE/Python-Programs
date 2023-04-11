import os
os.system('cls')

def percent(marks):
    return ((sum(marks)/500)*100)
        
marks1=[65,75,86,98,77]
p=percent(marks1)
marks2=[76,78,98,68,99]
q=percent(marks2)

s=["Piyush","Harry"]
sub=["Hindi","English","Physics","Chemistry","Maths"]

print("Student Name : ",s[1])
print(sub[0],"     : ",marks1[0])
print(sub[1],"   : ",marks1[1])
print(sub[2],"   : ",marks1[2])
print(sub[3]," : ",marks1[3])
print(sub[4],"     : ",marks1[4])
print("Percentage : ",p,"%")

print("Student Name : ",s[0])
print(sub[0],"     : ",marks2[0])
print(sub[1],"   : ",marks2[1])
print(sub[2],"   : ",marks2[2])
print(sub[3]," : ",marks2[3])
print(sub[4],"     : ",marks2[4])
print("Percentage : ",q,"%")
