ajh=int(input("bir sayı giriniz: "))
kejh=int(input("başka bir sayı giriniz: "))
for i in range(1,ajh+1):
    if ajh<kejh:
        print(ajh,"sayısı",kejh,"sayısından küçüktür")
        print("= ",i,"+",ajh)
        ajh += i
        print("başarısız")
    elif ajh>=kejh:
        print(ajh,"sayısı",kejh,"sayısından büyüktür veya eşittir")
        break
        