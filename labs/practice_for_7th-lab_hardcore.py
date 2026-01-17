# ==========================================
# SENARYO: KARGO UÇAĞI YÜKLEME (NO DICT, NO CLASS)
# KONULAR: Nested Lists, Indexing, Rollback, Assert, Raise
# ==========================================

# ÖZEL HATALAR
class UcakKapasiteHatasi(Exception): pass
class KargoBulunamadiHatasi(Exception): pass

# ---------------------------------------------------------
# YARDIMCI FONKSİYONLAR
# ---------------------------------------------------------

def kargo_bul_ve_cikar(depo_listesi, kargo_adi):
    """
    Bu fonksiyon, iç içe listede kargoyu arar, bulursa listeden SİLER ve geri döndürür.
    depo_listesi: [["Koli1", 50], ["Koli2", 30]]
    """
    bulunan_index = -1
    
    # Listeyi gezip indeksi buluyoruz
    for i in range(len(depo_listesi)):
        if depo_listesi[i][0] == kargo_adi:
            bulunan_index = i
            break
            
    # TODO 1: Kargo Kontrolü (Raise)
    # Eğer bulunan_index hala -1 ise, kargo yok demektir.
    # 'KargoBulunamadiHatasi' fırlat.
    # Mesaj: "[kargo_adi] depoda yok!"
    
    # KOD BURAYA:
    if bulunan_index == -1:
        raise KargoBulunamadiHatasi(kargo_adi,"depoda yok")
    

    # Kargoyu listeden çıkar ve döndür (pop)
    silinen_kargo = depo_listesi.pop(bulunan_index)
    print(f"📦 '{silinen_kargo[0]}' depodan çıkarıldı. (Ağırlık: {silinen_kargo[1]}kg)")
    return silinen_kargo


def ucaga_yukle(ucak_listesi, yeni_kargo, max_kapasite):
    """
    Kargoyu uçağa yüklemeye çalışır. Kapasiteyi kontrol eder.
    ucak_listesi: [["EskiKoli", 100]]
    yeni_kargo: ["YeniKoli", 50]
    """
    
    # Uçaktaki mevcut ağırlığı hesaplayalım
    mevcut_agirlik = 0
    for kargo in ucak_listesi:
        mevcut_agirlik += kargo[1] # Listenin 1. elemanı ağırlık
        
    # TODO 2: Kapasite Kontrolü (Raise)
    # Eğer (mevcut_agirlik + yeni_kargo[1]) > max_kapasite ise;
    # 'UcakKapasiteHatasi' fırlat.
    # Mesaj: "Uçak kapasitesi doldu! Yüklenemez."
    if mevcut_agirlik+ yeni_kargo[1]> max_kapasite:
        raise UcakKapasiteHatasi("Uçak kapasitesi doldu! Yüklenemez.")
    
    # KOD BURAYA:
    

    # Hata yoksa ekle
    ucak_listesi.append(yeni_kargo)
    print(f"✈️  '{yeni_kargo[0]}' uçağa başarıyla yüklendi.")


# ---------------------------------------------------------
# ANA TRANSFER OPERASYONU (ROLLBACK BURADA)
# ---------------------------------------------------------

def transfer_baslat(depo, ucak, kargo_adi, ucak_limiti):
    print(f"\n🔄 TRANSFER: '{kargo_adi}' depodan uçağa taşınıyor...")

    # TODO 3: Assert ile Veri Kontrolü
    # 'depo' ve 'ucak' değişkenlerinin tipi kesinlikle 'list' olmalıdır.
    # Değilse assert hatası ver.
    
    # KOD BURAYA:
    assert type(depo) and type(ucak) == list
    

    gecici_kargo = None # Henüz elimize almadık

    try:
        # ADIM 1: Kargoyu depodan bul ve ÇIKAR (Eline al)
        # kargo_bul_ve_cikar fonksiyonunu çağır ve sonucu 'gecici_kargo'ya eşitle.
        # Bu noktada kargo artık depoda DEĞİL.
        
        # KOD BURAYA:
        gecici_kargo=kargo_bul_ve_cikar(depo, kargo_adi)


         # gecici_kargo = ...

        # ADIM 2: Uçağa yüklemeye çalış (Riskli İşlem)
        # ucaga_yukle fonksiyonunu çağır.
        # Eğer kapasite hatası verirse, kargo elimizde kalır!
        
        # KOD BURAYA:
        ucaga_yukle(ucak,gecici_kargo,ucak_limiti)

    except UcakKapasiteHatasi as e:
        # TODO 4: ROLLBACK (Geri Alma)
        # Uçak dolu olduğu için hata aldık.
        # AMA kargoyu (gecici_kargo) az önce depodan sildik (pop yaptık).
        # Eğer buraya bir şey yazmazsak kargo kaybolur.
        # 'gecici_kargo'yu tekrar 'depo' listesine ekle (append).
        
        print(f"🛑 HATA: {e}")
        print(f"↩️  ROLLBACK: '{gecici_kargo[0]}' depoya geri konuluyor...")
        
        # KOD BURAYA:
        depo.append(gecici_kargo)
        
        # Hatayı tekrar fırlat ki test başarısız olduğunu anlasın
        raise e
        

    except KargoBulunamadiHatasi as e:
        print(f"❌ İşlem iptal: {e}")
        raise e

# ---------------------------------------------------------
# TEST SENARYOSU
# ---------------------------------------------------------
def testi_calistir():
    # Nested List Yapısı: [ [Ad, Kg], [Ad, Kg] ]
    ana_depo = [
        ["Motor Parçası", 500], 
        ["Tıbbi Malzeme", 200], 
        ["Posta Çuvalı", 50]
    ]
    
    kargo_ucagi = [
        ["Zaten Var Olan Yük", 900]
    ]
    
    # Uçağın limiti 1000 Kg. İçinde 900 var. Boş yer: 100 Kg.
    
    print(f"Başlangıç Depo: {ana_depo}")
    print(f"Uçak Yükü: {900} / 1000 kg")

    # TEST: 500 Kg'lık "Motor Parçası"nı yüklemeye çalış.
    # Beklenen: Depodan çıkacak -> Uçağa sığmayacak -> Depoya geri dönecek.
    try:
        transfer_baslat(ana_depo, kargo_ucagi, "Motor Parçası", 1000)
    except Exception:
        pass # Hatayı test için yutuyoruz

    print(f"\nSonuç Depo: {ana_depo}")
    
    # KONTROL
    # Eğer "Motor Parçası" depoda yoksa, rollback çalışmamış demektir.
    kargo_isimleri = [x[0] for x in ana_depo] # List comprehension ile isimleri al
    
    if "Motor Parçası" in kargo_isimleri:
        print("✅ BAŞARILI: Rollback çalıştı, Motor Parçası kaybolmadı.")
    else:
        print("❌ HATA: Motor Parçası kayboldu! Rollback yapılmamış.")

if __name__ == "__main__":
    testi_calistir()