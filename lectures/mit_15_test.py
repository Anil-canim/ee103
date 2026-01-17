# def mult_recur_verbose(a, b):
#     if b == 1:
#         print("call with",a,b)
#         return a
#     else:
#         print("call with",a,b)
#         calc = mult_recur_verbose(a, b-1)
#         print(f"returning {a}+{calc} for call with {a} and {b}")
#         return a + calc
# print(mult_recur_verbose(5,4))


# def power_recur(n, p):
#     if p==0 :
#         return 1
#     elif p==1:
#         return n
#     else:
#         return n*power_recur(n,p-1)
    
# print(power_recur(2,3))  # prints 8
# def factorial_iter_recur(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_iter_recur(n-1)
    
# print(factorial_iter_recur(3))


# ## factorial iterative
# def factorial_iter(n):
#     print(f'this is fact({n})')
#     prod = 1
#     for i in range(1,n+1):
#         prod *= i
#     return prod

# print(factorial_iter(5))




# def fibonacci_recur(n):

#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         result = fibonacci_recur(n-1) + fibonacci_recur(n-2)
      
#         return result
    

# print(fibonacci_recur(5))

# computed={0:0, 1:1}
# def fibonacci_efficient(n, computed=computed):
#     if n not in computed:
#         computed[n] = fibonacci_efficient(n-1, computed) + fibonacci_efficient(n-2, computed)
#     return computed[n]


# print(fibonacci_efficient(5))
# print(fibonacci_efficient(50))
# print(computed)

# def recur_power(base, exp):
#  """
#  base: int or float.
#  exp: int >= 0
#  Returns base to the power of exp using recursion.
#  Hint: Base case is when exp = 0. Otherwise, in the recursive
#  case you return base * base^(exp-1).
#  """
#  # Your code here
#  if exp==0:
#     return 1
#  else:
#     return base*recur_power(base,exp-1)
     
    
# # Examples:
# print(recur_power(2,5)) # prints 32



# def hanoi(n, kaynak, hedef, yardimci):
#     # Base Case: Sadece 1 disk varsa direkt hedefe taşı
#     if n == 1:
#         print(f"Diski {kaynak} -> {hedef} taşı")
#         return

#     # Recursive Step 1: n-1 diski, Hedef'i aracı olarak kullanarak Yardımcı'ya taşı
#     hanoi(n - 1, kaynak, yardimci, hedef)

    
#     # Step 2: En büyük diski (n. disk) Kaynak'tan Hedef'e taşı
#     print(f"Diski {kaynak} -> {hedef} taşı")
    
#     # Recursive Step 3: Yardımcı'daki n-1 diski, Kaynak'ı aracı kullanarak Hedef'e taşı
#     hanoi(n - 1, yardimci, hedef, kaynak)

# # Test: 3 Disk için
# hanoi(3, 'A', 'C', 'B')



# def is_palindrome(s):
#     """
#     Bu fonksiyon recursive olarak string'in palindrom olup olmadığını kontrol eder.
    
#     Kurallar:
#     1. Döngü (for/while) KULLANILAMAZ.
#     2. s[::-1] gibi ters çevirme hileleri YASAK.
#     3. Sadece string slicing (s[1:-1] vb.) ve recursion kullanılacak.
    
#     Input: s (str) -> Örn: "kabak"
#     Output: True veya False
#     """

#     # 1. BASE CASE: String uzunluğu 0 veya 1 ise nedir?
#     # Buraya yaz...
#     if len(s)==0:
#         return True
    
#     if s[0]==s[-1]:
#        is_palindrome(s[1:-1])
    
        
#     else:
#         return False
        
#     # 2. RECURSIVE STEP: 
#     # İlk ve son harf eşitse, iç kısmı (s[1:-1]) fonksiyona tekrar gönder.
#     # Değilse False döndür.
#     # Buraya yaz...
#     # Kodu yazınca bunu sil

# def deep_sum(L):
#     """
#     Bu fonksiyon iç içe geçmiş listelerin (nested lists) içindeki
#     TÜM sayıların toplamını bulur.
    
#     Input: L (list) -> Örn: [1, [2, 3], [4, [5]]]
#     Output: int (Toplam)
#     """
#     total = 0
    
#     # Listeyi gez (for döngüsü kullanabilirsin, elemanları kontrol etmek için)
#     for element in L:
#         # EĞER eleman bir sayıysa (int):
#         if isinstance(element, int):
#             total+=element
#             # Doldur burayı
            
#         # EĞER eleman bir listeyse (list):
#         elif isinstance(element, list):
#             total+=deep_sum(element)# ! RECURSION BURADA !
#             # Bu alt listeyi deep_sum'a gönder, gelen sonucu toplama ekle.
#             # Doldur burayı
            
#     return total

# # --- TEST KODLARI (Buralara dokunma, sadece çalıştır) ---
# if __name__ == "__main__":
#     print("--- Soru 1: Palindrome Test ---")
#     try:
#         print(f"kabak  -> {is_palindrome('kabak')} (Beklenen: True)")
#         print(f"radar  -> {is_palindrome('radar')} (Beklenen: True)")
#         print(f"python -> {is_palindrome('python')} (Beklenen: False)")
#         print(f"a      -> {is_palindrome('a')} (Beklenen: True)")
#     except Exception as e:
#         print(f"HATA YAPTIN: {e}")

#     print("\n--- Soru 2: Deep Sum Test ---")
#     sample_list = [1, 2, [3, 4], [5, [6, 7], 8], 9] 
#     # 1+2+3+4+5+6+7+8+9 = 45 etmeli
#     try:
#         sonuc = deep_sum(sample_list)
#         print(f"Liste: {sample_list}")
#         print(f"Sonuç: {sonuc}")
        
#         if sonuc == 45:
#             print("TEBRİKLER! Doğru çalışıyor.")
#         else:
#             print(f"OLMADI! 45 çıkması lazım, sen {sonuc} buldun.")
#     except Exception as e:
#         print(f"HATA YAPTIN: {e}")

def flatten(L):
    """
    SORU 3: LİSTE DÜZLEŞTİRME (FLATTEN)
    
    Görev: İç içe geçmiş listeleri (nested lists) tek boyutlu düz bir liste haline getir.
    
    Kurallar:
    1. Recursion kullanmak ZORUNLUDUR.
    2. .append() veya .extend() metodlarını kullanmak YASAK.
    3. Listeleri birleştirmek için '+' operatörünü kullanacaksın.
    4. Döngü (for) sadece listenin elemanlarını gezmek için kullanılabilir.
    
    Örnek:
    Input:  [1, [2, [3, 4], 5], 6]
    Output: [1, 2, 3, 4, 5, 6]
    """
    empty_list=[]
    for i in L[:]:
        if type(i)==list:
            empty_list+=flatten(i)
            
        else:
            empty_list+=(i,)
    return empty_list

    # KODUNU BURAYA YAZ
    # İpucu: Eleman listeyse recursion yap, değilse listeye çevirip ekle.
    

def to_binary(n):
    """
    SORU 4: DECIMAL TO BINARY (TABAN ÇEVİRME)
    
    Görev: Verilen pozitif bir tamsayıyı (int), binary (ikilik) formatta
    string'e çevir.
    
    Kurallar:
    1. Döngü (while/for) kullanmak KESİNLİKLE YASAK.
    2. bin() fonksiyonunu kullanmak YASAK.
    3. Sadece matematiksel işlemler (//, %) ve recursion kullanılacak.
    
    Örnek:
    Input:  13
    Output: "1101"  (Çünkü 13 = 8 + 4 + 1)
    """
    
    # KODUNU BURAYA YAZ
    
    if n==0:
        return "0"
    elif n==1:
        return "1"
    return to_binary(n // 2) + str(n % 2)
    

    
    # İpucu: Base case n=0 ve n=1 durumlarıdır.
    # Formül: to_binary(n // 2) + str(n % 2) (Sıralamaya dikkat et!)


# --- TEST KODLARI (Buraları değiştirme, sadece çalıştır) ---
if __name__ == "__main__":
    print("--- TEST 1: FLATTEN ---")
    try:
        input_list = [1, [2, [3, 4], 5], 6, [[7]]]
        sonuc = flatten(input_list)
        beklenen = [1, 2, 3, 4, 5, 6, 7]
        
        print(f"Girdi:    {input_list}")
        print(f"Senin:    {sonuc}")
        print(f"Beklenen: {beklenen}")
        
        if sonuc == beklenen:
            print(">> SONUÇ: BAŞARILI! ✅")
        else:
            print(">> SONUÇ: HATALI! ❌")
    except Exception as e:
        print(f">> HATA ALDIN: {e}")

    print("\n" + "-"*30 + "\n")

    print("--- TEST 2: BINARY ---")
    try:
        test_sayilar = {13: "1101", 10: "1010", 0: "0", 1: "1", 255: "11111111"}
        hatasiz = True
        
        for sayi, beklenen_str in test_sayilar.items():
            senin_str = to_binary(sayi)
            if senin_str != beklenen_str:
                print(f"❌ HATA: {sayi} için '{beklenen_str}' bekleniyordu, sen '{senin_str}' buldun.")
                hatasiz = False
        
        if hatasiz:
            print(">> SONUÇ: TÜM TESTLER BAŞARILI! ✅")
        else:
            print(">> SONUÇ: BAZI TESTLER GEÇEMEDİ. ❌")
            
    except Exception as e:
        print(f">> HATA ALDIN: {e}")