#Write a name of list and print hello which start with 'S' 
import os
os.system('cls')
li=['rahul','gopal','sakshi','ram','sheetal','shubham']
for name in li:
   if name.startswith('s'):
    print('Hello '+name)