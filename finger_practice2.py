#finger_practice.2
while True:
    num=int(input("give us a number: "))

    if num>0:
        print(num,"is positive")
    elif num<0:
        print(num,"is negative")
    else:
        print(num,"is neutral")
    ans=input("do you want to continue?,so press x: ")
    if ans=="x":
        continue
    else:
        break