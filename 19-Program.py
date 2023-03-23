#Write a program tp display the dictionary of hindi word with the value of its english word
import os
os.system('cls')
dist={"Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"}
ua={"Namste":"Hello"}
dist.update(ua)
print(dist)
a=input("Enter the Hindi word : ")
print("The meaning of this hindi word in english is : ",dist.get(a))

