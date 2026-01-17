x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0.0
high =x
ans =(low+high)/2

while abs(ans**4-x) > epsilon:
    
    if ans**4<x:
        low=ans
    else:
        high=ans
    ans =(low+high)/2
print(ans)