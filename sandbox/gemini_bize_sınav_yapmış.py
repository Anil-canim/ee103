import copy

# ==========================================
# BÖLÜM 1: KOMPLEKS LIST COMPREHENSION
# ==========================================

def analyze_cell_temps(temp_list):
    """
    TODO 1: Durum Analizi
    List Comprehension kullanarak yeni bir 'status_list' oluştur.
    
    KURAL (Tek Satırda):
    - Eğer sıcaklık 45'ten büyükse -> "CRITICAL" stringini listeye ekle.
    - Eğer 45 ve altındaysa -> "NORMAL" stringini listeye ekle.
    
    İpucu: [("SONUC_A" if KOŞUL else "SONUC_B") for x in liste] yapısını hatırla.
    """
    status_list=["CRITICAL" if i >45 else "NORMAL" for i in temp_list]
    return status_list

def calculate_cell_power(voltages, current):
    """
    TODO 2: Güç Hesabı (P = V * I)
    Sadece voltajı 3.0V üzerinde olan (sağlam) hücrelerin gücünü hesapla.
    3.0V ve altını yok say (listeye alma).
    
    Döndürülen liste şu formatta olmalı: [Guç1, Guç2, ...]
    """
    return [i*current for i in voltages if i>3]

# ==========================================
# BÖLÜM 2: SİMÜLASYON VE KOPYALAMA
# ==========================================

def create_stress_test_clone(battery_pack):
    """
    TODO 3: Güvenli Simülasyon Ortamı
    'battery_pack' listesi, iç içe modüllerden oluşur: [[3.7, 3.8], [3.6, 3.7]]
    Biz bu veriler üzerinde "patlama testleri" yapacağız. 
    Gerçek verilerin (battery_pack) ASLA değişmemesi lazım.
    
    Buna uygun kopya yöntemini (copy modülü ile) kullanarak 'clone' oluştur ve döndür.
    """
    clone=copy.deepcopy(battery_pack)
    return clone

# ==========================================
# BÖLÜM 3: KRİTİK HATA TEMİZLİĞİ (Döngüde Silme)
# ==========================================

def eject_dead_cells(module_voltages):
    """
    TODO 4: Ölü Hücreleri Atma
    Bir modüldeki voltaj listesini al.
    Voltajı 2.5V'un altına düşmüş (ölü) hücreleri listeden sil.
    
    DİKKAT: 
    1. Fonksiyon void olmalı (return yok), listeyi yerinde (in-place) değiştirmeli.
    2. İndeks kayması hatasına düşmemek için doğru döngü yöntemini kullan.
    """
    shallow_copy=copy.copy(module_voltages)
    for i in shallow_copy:
        if i<2.5:
            module_voltages.remove(i)
    

# ==========================================
# ANA SENARYO (TEST KISMI)
# ==========================================

def run_bms():
    print("--- BMS SİSTEMİ BAŞLATILIYOR ---")
    
    # Veriler
    temps = [30, 48, 42, 50, 25]  # Derece
    cell_volts = [3.7, 4.1, 2.1, 3.9, 0.5, 4.0] # 2.5 altı ölüdür
    
    # Karmaşık Yapı: 2 Modül, her modülde 2 hücre voltajı var
    main_battery_pack = [[3.7, 3.7], [3.8, 3.8]]

    # 1. Sıcaklık Analizi Testi
    # Beklenen: ['NORMAL', 'CRITICAL', 'NORMAL', 'CRITICAL', 'NORMAL']
    statuses = analyze_cell_temps(temps)
    print(f"Sıcaklık Durumları: {statuses}")

    # 2. Simülasyon Testi (Deep Copy Kontrolü)
    sim_pack = create_stress_test_clone(main_battery_pack)
    if sim_pack: # Fonksiyonu yazınca burası çalışacak
        sim_pack[0][0] = 0.0 # Simülasyonda bir hücreyi patlatıyoruz
        print(f"Simülasyon Paketi: {sim_pack}")
        print(f"Gerçek Paket (Değişmemeli): {main_battery_pack}")
        
        if main_battery_pack[0][0] == 3.7:
            print("✅ TEST GEÇİLDİ: Gerçek batarya güvende.")
        else:
            print("❌ HATA: Gerçek batarya hasar gördü! (Yanlış kopya yöntemi)")
    print(calculate_cell_power(cell_volts,20))
    # 3. Ölü Hücre Temizliği Testi
    print(f"Temizlik Öncesi Voltajlar: {cell_volts}")
    eject_dead_cells(cell_volts)
    print(f"Temizlik Sonrası Voltajlar: {cell_volts}")
    # Beklenen: [3.7, 4.1, 3.9, 4.0]

run_bms()