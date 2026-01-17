def remove_and_sort(Lin, k):
 """ Lin is a list of ints
 k is an int >= 0
 Mutates Lin to remove the first k elements in Lin and
then sorts the remaining elements in ascending order.
 If you run out of items to remove, Lin is mutated to an empty list.
 Does not return anything.
 """
 # Your code here
 if k in Lin:
  for i in Lin:
   if i==k:
    Lin.remove(i)
  Lin.sort()
 else:
  return Lin.sort()
    


# Examples:
L = [1,6,3]
k = 2
remove_and_sort(L, k)
print(L) # prints the list [3, 6]