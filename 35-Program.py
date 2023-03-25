#A spam comment is definded as a text containing following keywords: "make a lot of money","buy now", "subscribe this"and "click this" write a program to detect these spams.
import os
os.system('cls')
text = input("Enter the text :")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False
    
if(spam):
    print("This text is spam.")
else:
    print("This text not is spam.")