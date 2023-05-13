import os 
os.system('cls')

f = open('simple.txt','r')
t = f.read()
if 'piyush' in t:
    print("piyush word in file")
else:
    print("piyush word are not in file")
f.close()