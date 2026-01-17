# sozler = ["baba", "akü", "yok", "baba", "akü", "yok", "şarj", "bitti"]
# frekanslar = {}

# for i in sozler:
#     if i not in frekanslar:
#         frekanslar.update({i:1})
#     else:
#         frekanslar[i]+=1

# print(frekanslar)



# Başlangıç değerlerini sözlüğe koyuyoruz (Base cases)
# memo = {0: 0, 1: 1}

# def fib_efficient(n, d):
#     # 1. ADIM: Eğer 'n' zaten 'd' sözlüğünde varsa, hesaplama yapma!
#     # Direkt sözlükteki değeri döndür.
#     if n in d:
#         return d[n]
    
#     # 2. ADIM: Eğer yoksa, hesapla.
#     else:
#         # Formül: f(n-1) + f(n-2). Ama recursive çağrıda sözlüğü de gönder!
#         sonuc = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        
#         # 3. ADIM: Bulduğun sonucu sözlüğe ('d') kaydet ki sonra tekrar hesaplama.
#         # BURAYI SEN DOLDURACAKSIN
#         memo[n]=sonuc
        
#         return sonuc

# print(fib_efficient(35, memo)

# devre = {"R1": 100, "R2": 200, "R3": 300}
# devre_copy=devre.copy()

# # listler olmadığı için copy kullanıcam boşuna deepcopy e gerek yok
# for keys in devre_copy.keys():
#     devre_copy[keys]=devre_copy[keys]*110/100

# print(devre_copy)

# devre = {"R1": 100, "R2": 200, "R3": 300, "R4": 150}

# print(sum(devre.values()))


devre = {"R1":10, "R2":15, "R3": 12, "R4": 0}

# Gözünü buraya dik:
# 1. (G := sum(...)) -> Önce toplamı hesapla ve 'G' (Conductance) değişkenine ata.
# 2. if G > 0        -> Eğer bu G sayısı 0'dan büyükse...
# 3. 1 / G           -> ...Tersini alıp yazdır.
# 4. else 0          -> ...Değilse (yani hepsi 0 ise) ekrana 0 bas.

print(1 / G if (G := sum(1/r for r in devre.values() if r > 0)) > 0 else 0)

