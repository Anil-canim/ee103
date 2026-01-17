# Python file for user: anilcanguler (Experiment 8 Prep)
# =======================================================
# KONU: Nested Data Structures (Dict of Lists of Tuples)
#       Complex Iteration & Safe Retrieval (.get)
#
# ZORLUK: MAX (Sen istedin)
# =======================================================

# Senaryo: Bir uzay istasyonunun kargo manifestosu var.
# Veri yapısı şöyledir:
# {
#    "Gemi_Adi": [ ("Malzeme", Miktar, Birim_Fiyat), ("Malzeme", Miktar, Birim_Fiyat) ],
#    "Gemi_2": ...
# }

cargo_manifest = {
    "Nostromo": [("Fuel_Cells", 50, 100), ("Food_Rations", 200, 5), ("Alien_Egg", 1, 9999)],
    "Sulaco": [("Ammo_Box", 100, 20), ("Rifles", 10, 500)],
    "Derelict": [] # Boş gemi, dikkat et!
}

# ---------- PART 1: DICT METHODS & ITERATION (20 pts) ----------

def print_ship_manifests(manifest):
    """
    TODO (Part 1):
      - Verilen manifest (dictionary) üzerinde .items() kullanarak dön.
      - Her gemi için: "Gemi: <Gemi_Adi>" yazdır.
      - Sonra o geminin yük listesinde (list) dön.
      - Yük listesindeki her bir tuple için: 
            "  - <Malzeme>: <Miktar> adet (<Birim_Fiyat> kredi)" formatında yazdır.
      - Eğer gemi boşsa (liste boşsa), "  - YÜK YOK" yazdır.
    """
    print("\n--- PART 1: MANIFESTO ---")
    
    # KODU BURAYA YAZ
    for gemi,yük in manifest.items():
        print(f"Gemi:{gemi}")
        if yük==[]:
            print("YÜK YOK")
        for malzeme,miktar,birim_fiyat in yük:
            print(f"Malzeme: {malzeme}: {miktar} adet {birim_fiyat} kredi")
        

    # ---------------------
    # TODO: Bunu sil ve kodunu yaz.
    # ---------------------


# ---------- PART 2: SAFE RETRIEVAL & CALCULATION (30 pts) ----------

def calculate_ship_value(manifest, ship_name):
    """
    TODO (Part 2):
      - Verilen 'ship_name' anahtarını dictionary içinde .get() metodu ile ara.
      - DİKKAT: .get() kullanırken default değer olarak BOŞ LİSTE [] ver. 
        Böylece gemi yoksa kod patlamaz, 0 döner.
      - Geminin içindeki her bir malzeme (tuple) için toplam değeri hesapla:
            (Miktar * Birim_Fiyat)
      - O geminin toplam yük değerini integer olarak döndür.
      
      İPUCU: If-else ile gemi var mı diye kontrol etme. .get()'in gücünü kullan.
    """
    # KODU BURAYA YAZ
    total_value=0
    gemi=manifest.get(ship_name, [])
   
    for malzeme,miktar,para in gemi:
        total_value+=(miktar*para)
    return total_value
    # ---------------------
    # TODO: Kodunu yaz, mazeret üretme.
    # ---------------------


# ---------- PART 3: COMPLEX FILTERING (30 pts) ----------

def find_critical_supplies(manifest, min_price):
    """
    TODO (Part 3):
      - Tüm gemileri ve yüklerini tara.
      - Birim fiyatı 'min_price' değerinden YÜKSEK olan malzemeleri bul.
      - Şu formatta bir liste oluştur ve döndür:
        [ "GemiAdi - MalzemeAdi", "GemiAdi - MalzemeAdi", ... ]
      - Nested loop (İç içe döngü) kullanmak zorundasın.
    """
    critical_items = []
    for gemi,yük in manifest.items():
        for malzeme,miktar,para in yük:
            if para > min_price:
                critical_items.append(f"{gemi}-{malzeme}")

    
    # KODU BURAYA YAZ
    # ---------------------
    # TODO: Sil ve doldur.
    # ---------------------
    
    return critical_items


# ---------- PART 4: DATA TRANSFORMATION (20 pts) ----------

def convert_to_inventory_dict(manifest):
    """
    TODO (Part 4):
      - Mevcut yapıyı tersine çevir.
      - Hangi malzemeden toplam kaç tane olduğunu tutan basit bir sözlük döndür.
      - Çıktı formatı: { "Fuel_Cells": 50, "Ammo_Box": 100, ... }
      - İPUCU: Sözlükte key var mı diye kontrol etmen gerekecek (veya .get kullanıp üstüne ekleyeceksin).
    """
    inventory = {}
    for gemi,yük in manifest.items():
        for malzeme,miktar,para in yük:
            inventory[malzeme]=inventory.get(malzeme,0)+miktar

    return inventory
    # KODU BURAYA YAZ
    # ---------------------
    # TODO: Yapamazsan önceki laba geri dön.
    # ---------------------



# ---------- MAIN TEST BLOCK ----------

def main():
    print("Sistem Başlatılıyor... Hatalarını göreceğiz.\n")

    # TEST 1
    print_ship_manifests(cargo_manifest)

    # TEST 2
    val = calculate_ship_value(cargo_manifest, "Nostromo")
    print(f"\nNostromo Değeri (Beklenen: 15999): {val}")
    if val != 15999: print("!!! HATA: Hesaplama yanlış!")

    val_empty = calculate_ship_value(cargo_manifest, "Hayalet_Gemi")
    print(f"Olmayan Gemi Değeri (Beklenen: 0): {val_empty}")
    if val_empty != 0: print("!!! HATA: .get() kullanımın yanlış!")

    # TEST 3
    print("\n--- Kritik Malzemeler (Fiyat > 200) ---")
    crit = find_critical_supplies(cargo_manifest, 200)
    print(crit)
    # Beklenen: ['Nostromo - Alien_Egg', 'Sulaco - Rifles']

    # TEST 4
    print("\n--- Toplam Envanter ---")
    inv = convert_to_inventory_dict(cargo_manifest)
    print(inv)
    # Beklenen: {'Fuel_Cells': 50, 'Food_Rations': 200, 'Alien_Egg': 1, 'Ammo_Box': 100, 'Rifles': 10}

if __name__ == "__main__":
    main()