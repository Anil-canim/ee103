# def div(a,b):
#     if (b/a)%2==0:
#         return  True
#     else:
#         return False
    
# c=div(5,50)
# print(c)

# def sum_odd(a,b):
#     x=0
#     for i in range(a,b):
#         if i %2==0:
#            pass
#         else:
#             x+=(i)
#     print((x))

# sum_odd(10,20)

def bisection_root(i):
    low=0
    high=i
    ans=(low+high)/2
    epsilon=0.001
    while abs(ans**3-i)>=epsilon:
        if ans**3<i:
            low=ans
        else:
            high=ans
        ans=(low+high)/2
    return(ans)

def count_nums_with_sqt_close_to(n,epsilon):
    for i in range(n):
        sqrt=bisection_root(i)
        print(sqrt)

count_nums_with_sqt_close_to(20,0.001)
print(sqrt)
