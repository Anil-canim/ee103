import random
ramdom_number= random.randint(0,20)
user_number=int(input("sayı gir: "))
if type(user_number)== int:
    while user_number!=ramdom_number:
        if user_number>ramdom_number:
            print("sayın çok büyük")
        else:
            print("sayın çok küçük")
        user_number=int(input("sayını gir: "))
else:
    print("geçerli bi sayı gir")
