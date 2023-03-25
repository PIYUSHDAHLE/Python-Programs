# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

import math
import os
import random
import re
import sys

n=int(input())
if(n%2!=0):
    print("Weird")
elif(2<=n<=5):
    print("Not Weird")
elif(6<=n<=20):    
    print("Weitd")
elif(n>20):
    print("Not Weird")    