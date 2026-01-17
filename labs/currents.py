# currents=[0.5, 2.3, 50.0, 1.2, 100.0, 0.9]

# def protect_circuit(current_list):
#     for i in current_list[:]:
#         if i>10.0:
#             current_list.remove(i)

# protect_circuit(currents)
# print(currents)

# R=10
# voltages = [10, 20, 5, 100]
# # P=[(i)**2/R for i in voltages[:]]
# P=[(i)**2/R for i in voltages if i>15]
# print(P)

import copy

# ==========================================
# BÖLÜM 1: LİSTE ÜRETEÇLERİ (List Comprehension)
# ==========================================

def scale_voltages(voltages, gain):
    """
    TODO 1: List Comprehension kullanarak;
    'voltages' listesindeki her değeri 'gain' (kazanç) ile çarp.
    Elde edilen yeni listeyi döndür (return).
    (Tek satırda yazılmalı)
    """
    # KODU BURAYA YAZ
    return [i*gain for i in voltages]

def filter_noise(readings, threshold):
    """
    TODO 2: List Comprehension ve If kullanarak;
    'readings' listesinde SADECE 'threshold' (eşik) değerinden 
    BÜYÜK olan değerleri içeren yeni bir liste döndür.
    (Tek satırda yazılmalı)
    """
    # KODU BURAYA YAZ
    return [i for i in readings if i>threshold]

# ==========================================
# BÖLÜM 2: MUTABILITY & COPYING (Kopyalama)
# ==========================================

def backup_sensors_bad(sensor_list):
    """
    TODO 3: (Aliasing Hatası Simülasyonu)
    Bu fonksiyon şu an 'backup = sensor_list' yaparak hatalı (alias) yedek alıyor.
    Bu satırı sil ve yerine 'Slicing' [:] yöntemiyle 
    gerçek bir sığ kopya (shallow copy) alarak döndür.
    """
    backup = sensor_list[:] # BU SATIRI DÜZELT
    return backup

def create_secure_matrix_copy(matrix_data):
    """
    TODO 4: Derin Kopya (Deep Copy)
    'matrix_data' iç içe geçmiş listelerden oluşuyor (örn: [[1,2], [3,4]]).
    copy modülünü kullanarak bu matrisin 'deepcopy'sini oluştur ve döndür.
    Böylece kopyada yapılan değişiklik orijinali bozmasın.
    """
    
    deepcopy_matrix_data=copy.deepcopy(matrix_data)
    return deepcopy_matrix_data

# ==========================================
# BÖLÜM 3: DÖNGÜ İÇİNDE SİLME (Modifying Loop)
# ==========================================

def remove_dead_sensors(sensor_ids):
    """
    TODO 5: Güvenli Silme
    'sensor_ids' listesinde değeri 0 (sıfır) olan sensörleri listeden sil.
    DİKKAT: 'Index Shifting' hatası olmaması için döngüyü 
    listenin kopyası [:] üzerinde kurmalısın.
    Fonksiyon bir şey döndürmemeli (void), orijinal listeyi yerinde değiştirmeli.
    """
    for i in sensor_ids[:]:
        if i==0:
            void=sensor_ids.remove(i)
    return void

# ==========================================
# BÖLÜM 4: ANA SENARYO (Integration)
# ==========================================

def main_process():
    # Test Verileri
    raw_volts = [0.1, 0.5, 0.05, 1.2, 0.0, 3.3]
    matrix_settings = [[10, 20], [30, 40]]
    active_ids = [101, 0, 103, 0, 105, 0] # 0 olanlar bozuk

    print("--- BAŞLANGIÇ ---")

    # TODO 6: scale_voltages fonksiyonunu çağır.
    # raw_volts listesini 10 ile çarp (gain=10). Sonucu 'amplified' değişkenine ata.
    amplified = [scale_voltages(raw_volts, 10)] # BURAYI DOLDUR

    # TODO 7: remove_dead_sensors fonksiyonunu çağır.
    # 'active_ids' listesindeki 0'ları temizle.
    # (Bu fonksiyon yerinde değişiklik yaptığı için bir şeye eşitlemene gerek yok)
    remove_dead_sensors(active_ids)
    
    # --- SONUÇLARI YAZDIRMA (Buralara dokunma) ---
    print(f"Yükseltilmiş Voltajlar: {amplified}") 
    # Beklenen: [1.0, 5.0, 0.5, 12.0, 0.0, 33.0]
    
    print(f"Temizlenmiş ID'ler: {active_ids}")     
    # Beklenen: [101, 103, 105]

    # Deep Copy Testi
    safe_copy = create_secure_matrix_copy(matrix_settings)
    safe_copy[0][0] = 9999
    print(f"Orijinal Matris Bozuldu mu? (10 kalmalı): {matrix_settings[0][0]}")

# Çalıştır
main_process()