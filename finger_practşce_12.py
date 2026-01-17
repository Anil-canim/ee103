def count_sqrts(nums_list):
 """
 nums_list: a list
 Assumes that nums_list only contains positive numbers and that there are no duplicates.
 Returns how many elements in nums_list are exact squares of elements in the same list, including
"""
 # Your code here
 import copy
 shallow_copy=copy.copy(nums_list)
 for i in shallow_copy:
  if i **2 in shallow_copy:
   nums_list.remove(i**2)
  else:
   pass
 return len(shallow_copy)-len(nums_list)

  
# Examples:
print(count_sqrts([3,4,2,1,9,25])) # prints 3