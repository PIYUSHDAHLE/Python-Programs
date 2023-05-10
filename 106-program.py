import os
os.system('cls')
num = int(input("Enter the number : "))
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")