import os
os.system('cls')

nums = [10, 9, 8, 7, 6, 5]
print('Before list : ',nums)
nums[0] = nums[1] - 5
print('After list : ',nums)
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])