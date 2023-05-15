#Write a program to fill in the letter template
# given below will name and date
# letter ='''Dear <|NAME|>
#             You are selected. 
#             Date <|DATE|> '''
import os
os.system('cls')
name=input("Enter Your Name : \n")
date=input("Enter Date : \n")
letter =''' \t Dear <|NAME|>
             You are selected,Off campus of the TCS.
             welocome to the team.
              
             Date <|DATE|> '''
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
