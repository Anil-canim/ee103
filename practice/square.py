x=0
c=int(input("bir sayı giriniz: "))
while x**2<=c:
    print(x,"s square is",{x**2})
    x+=1
    if x**2>c:
       print("döngü bitti") 
       break
    else:
        print("devamke")
         
    
    