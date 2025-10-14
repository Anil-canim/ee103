import random
ramdom_number= random.randint(0,100)
user_number=int(input("enter your number: "))
if type(user_number)== int:
    while user_number!=ramdom_number:
        if user_number>ramdom_number:
            print("your number is too high")
        else:
            print("your number is too small")
        user_number=int(input("enter your number: "))
else:
    print("enter a valid number")