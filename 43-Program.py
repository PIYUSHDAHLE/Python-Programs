import os
os.system('cls')

commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
#your code goes here
user=input()
if (user in commands):
  print("OK")
else:
    print("Not supported")