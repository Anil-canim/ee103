def flatten(L):
 # Your code here 
    empty_list=[]
    for i in L:
        if type(i)==list:
            empty_list.extend(flatten(i))
        else:
            empty_list.append(i)
    return empty_list


L = [[1,4,[6],2],[[[3]],2],4,5]

print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]