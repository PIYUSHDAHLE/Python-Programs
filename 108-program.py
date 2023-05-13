import os
os.system('cls')

f=open("simple.txt","r")
data=f.read() 
print(data)
f.close()

f2=open("simple2.txt","r")
data2=f2.read(5) #read only char of text file
print(data2)
f2.close()