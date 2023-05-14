import os 
os.system('cls')

with open('simple4.txt','r') as f :
 a = f.read()
 print(a)

with open('simple.txt','w') as f :
 b= f.write("helloo boss how are you")
 b = f.read()
 print(b)
 