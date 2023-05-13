import os
os.system('cls')
 
file1 = open('simple.txt')
data = file1.readline()
print(data)

data = file1.readline()
print(data)

data = file1.readline()
print(data)
file1.close()