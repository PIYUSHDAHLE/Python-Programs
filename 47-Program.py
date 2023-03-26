# A group of buildings have restrooms on every 5th floor.
# For example, a building with 12 floors has restrooms on the 5th and 10th floors.

# Create a program that takes the total number of floors as input and outputs the floors that have restrooms.

# Sample Input
# 23

# Sample Output
# 5
# 10
# 15
# 20

n = int(input())

num = list(range(5,n,5))
for x in num:
    print(x)