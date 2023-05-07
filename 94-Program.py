import os
os.system('cls')
num = input("Enter the number : ")
num=int(num)
fact = 1
# Factorial of negative number doesn't exist
if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i

if num > 0: 
 print("Factorial of", num, "is", fact)
# Time complexity: O(N)
# Space complexity: O(1)