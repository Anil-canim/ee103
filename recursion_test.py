# def flat_the_list_by_rec(liste):
#     empty_list=[]
#     for lists in (liste[:]):
#         if type(lists)==list:
           
#             coming_list=flat_the_list_by_rec(lists)
#             empty_list.extend(coming_list)
#         else:
#             empty_list.append(lists)
            
#     return empty_list
import sys
sys.setrecursionlimit(2000) # Limiti 2000'e çıkar
# Şimdi 1500'ü hesapla
# liste=[1, [2, [3, 4], 5], 6]
# print(type(liste))
# print(flat_the_list_by_rec(liste))

fibo_dic={0:0,1:1}
def fibonacci_rec(fibo):
    if fibo in fibo_dic:
        return fibo_dic[fibo]
    else:
        kef=fibonacci_rec(fibo-2) + fibonacci_rec(fibo-1)
        fibo_dic[fibo]=kef
        return fibo_dic[fibo]
    
    

print(fibonacci_rec(3670))

# import sys
# print(sys.getrecursionlimit())

#benim kodum
result=[0,1]
def fibo_dic_for(n):
    for i in range(n):
        if i>1:
            last=result[i-1]+result[i-2]
            result.append(last)
    return result[n-1]
print(fibo_dic_for(5))

#gemini sağolsun
def fibonacci_iterative(n):
    # Başlangıç değerleri (F(0) ve F(1))
    a, b = 0, 1
    
    # n kez döndür
    for _ in range(n):
        # Python'ın sihirli "tuple unpacking" özelliği ile tek satırda geçiş:
        # a yeni b olsun, b de ikisinin toplamı olsun.
        a, b = b, a + b
        
    return a

# Test et: Göz açıp kapayana kadar hesaplar.
print(fibonacci_iterative(100))