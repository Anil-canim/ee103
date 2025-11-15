# finger_practice4
while True:
    N=int(input("give us a positive integer: "))
    epsilon=0.001
    low=0
    high=N
    ans=(low+high)/2
    count=0

    while abs(ans**3-N)>epsilon:
        if ans**3< N:
            low=ans
        else:
            high=ans
        count += 1
        ans=(low+high)/2


    print("count is", count )
    print((ans**3))
    if round(ans)**3==N:
        print(round(ans), "is perfect cube of: ", N)
    else:
        print(ans, "is a cube of ", N, "but unfortunately it's not the perfect cube")
    k=input("do you want to try again?, press x to continue otherwise press any key: ")
    if k=="x":
        continue
    else:
        break