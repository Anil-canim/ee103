a=input("what is your name? ")
b=(input("enter a number? "))
for i in range(len(b)):
    if int(b[i])%2==0:
        total=len(b[i])
last_digit=total%10
print(a*last_digit)
        
    



