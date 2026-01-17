a=input("enter a name: ")
b=input("enter a number: ")

c=([int(x) for x in b if int(x) % 2 == 0])
total=(f'{sum(c)}')

ld_total=int(total[-1])

print((a+f"\n")*ld_total)