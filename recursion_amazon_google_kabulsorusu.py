def alternating_sum(L, depth=1):
    """
    SORU: ALTERNATING DEEP SUM (DALGALI DERİNLİK TOPLAMI)
    
    Kurallar:
    1. Listenin derinliği (depth) TEK sayı ise (1, 3, 5...) sayıları TOPLA (+).
    2. Listenin derinliği (depth) ÇİFT sayı ise (2, 4, 6...) sayıları ÇIKAR (-).
    3. Global değişken yasak.
    4. Flatten (düzleştirme) yasak.
    
    Örnek:
    L = [10, [5], 4]
    - 10 ve 4 (Derinlik 1, Tek): +10 +4
    - 5 (Derinlik 2, Çift): -5
    Sonuç: 9
    """
    total = 0
    
    for element in L:
        # DURUM 1: Eleman bir SAYI ise (int)
        if isinstance(element, int):
            # Buraya mantığı kur:
            
            if depth%2!=0:
                total+=element
            else:
                total-=element
            
            # Eğer depth % 2 != 0 ise (TEK), toplama ekle.
            # Eğer depth % 2 == 0 ise (ÇİFT), toplamdan çıkar.
            # KODUNU BURAYA YAZ
            
        # DURUM 2: Eleman bir LİSTE ise (list)
        elif isinstance(element, list):
            # RECURSION BURADA
            total+=alternating_sum(element,depth+1)
            # Alt listeye inerken depth parametresini ne yapman lazım?
            # Dönen sonucu 'total' değişkenine nasıl ekleyeceksin?
            # KODUNU BURAYA YAZ
            
    return total

# --- TEST KODLARI ---
if __name__ == "__main__":
    print("--- Zor Soru Testi ---")
    
    # Test 1: Örnekteki Soru
    # L1 (Tek): 10, 4 -> +14
    # L2 (Çift): 5, 3, 6 -> -14
    # L3 (Tek): 2, 1 -> +3
    # Toplam: 3 olmalı.
    soru_listesi = [10, [5, 3, [2, 1]], 4, [6]]
    sonuc = alternating_sum(soru_listesi)
    
    print(f"Liste: {soru_listesi}")
    print(f"Senin Sonucun: {sonuc}")
    print(f"Beklenen: 3")
    
    if sonuc == 3:
        print(">> HELAL OLSUN! Doğru. ✅")
    else:
        print(">> PATLADIN. Mantığı tekrar kur. ❌")
        
    print("-" * 20)
    
    # Test 2: Basit Kontrol
    # L1: 10 -> +10
    # L2: [5] -> -5
    # Sonuç: 5 olmalı
    basit_liste = [10, [5]]
    sonuc2 = alternating_sum(basit_liste)
    if sonuc2 == 5:
        print(">> Basit test geçti. ✅")
    else:
        print(f">> Basit testte hata. Beklenen 5, Seninki {sonuc2} ❌")