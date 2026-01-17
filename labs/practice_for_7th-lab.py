# ==========================================
# SENARYO: GÜVENLİ BANKA İŞLEM SİSTEMİ
# KONULAR: Custom Exception, Raise, Assert, Try/Except
# ==========================================

# ---------------------------------------------------------
# BÖLÜM 1: ÖZEL HATA TANIMLAMA (CUSTOM EXCEPTION)
# ---------------------------------------------------------
# TODO 1: Python'un standart hataları (ValueError vs) bize yetmiyor.
# "YetersizBakiyeHatasi" (InsufficientFundsError) adında yeni bir hata sınıfı oluştur.
# İpucu: class YeniHata(Exception): pass
class InsufficientFundsError(Exception):
    pass

# ---------------------------------------------------------
# BÖLÜM 2: HATA FIRLATMA VE ASSERT (RAISE & ASSERT)
# ---------------------------------------------------------
def withdraw_money(current_balance, amount_to_withdraw):
    """
    Bu fonksiyon para çekme işlemini gerçekleştirir.
    Ancak güvenlik önlemleri almalıdır.
    """
    
    # TODO 2: Geliştirici Kontrolü (Assert)
    # Banka veritabanında bakiye ASLA negatif olmamalıdır.
    # Eğer current_balance 0'dan küçük gelirse bu bir yazılım hatasıdır.
    # Bunu 'assert' ile kontrol et. Mesaj: "Sistem Hatası: Bakiye negatif olamaz!"
    # KOD BURAYA:
    assert current_balance>=0,("Sistem Hatası: Bakiye negatif olamaz!")

    # TODO 3: Geçersiz Giriş Kontrolü (Raise ValueError)
    # Kullanıcı 0 veya negatif bir çekim miktarı (amount_to_withdraw) girerse,
    # 'ValueError' fırlat. Mesaj: "Çekilecek miktar pozitif olmalıdır."
    # KOD BURAYA:
    if amount_to_withdraw<=0:
        raise ValueError("Çekilecek miktar pozitif olmalıdır.")

    # TODO 4: Yetersiz Bakiye Kontrolü (Raise Custom Exception)
    # Eğer çekilmek istenen miktar, mevcut bakiyeden fazlaysa,
    # Yukarıda tanımladığın 'InsufficientFundsError' hatasını fırlat.
    # Mesaj: "İşlem reddedildi: Bakiye yetersiz."
    # KOD BURAYA:
    if amount_to_withdraw>current_balance:
        raise InsufficientFundsError("İşlem reddedildi: Bakiye yetersiz.")

    # Her şey yolundaysa yeni bakiyeyi döndür
    return current_balance - amount_to_withdraw

# ---------------------------------------------------------
# BÖLÜM 3: HATALARI YAKALAMA (TRY / EXCEPT)
# ---------------------------------------------------------
def process_atm_queue(customer_requests):
    """
    Bir dizi işlem isteğini sırayla dener.
    Hatalar oluşsa bile program çökmemeli, hatayı loglayıp sonraki müşteriye geçmelidir.
    
    Girdi: [(100, 20), (50, 100), (200, -50)] -> (Bakiye, Çekilecek Miktar)
    Döndür: Başarılı işlem sonrası kalan bakiyeler listesi (Hatalı işlemler listeye girmemeli)
    """
    successful_balances = []

    for balance, amount in customer_requests:
        # TODO 5: Try / Except Bloğu
        # withdraw_money fonksiyonunu çağır.
        # - Eğer işlem başarılıysa sonucu 'successful_balances' listesine ekle.
        # - Eğer 'InsufficientFundsError' yakalanırsa ekrana "🔴 Bakiye Yetersiz" yaz.
        # - Eğer 'ValueError' yakalanırsa ekrana "🟡 Hatalı Giriş" yaz.
        # - Diğer tüm hatalar için (Exception) ekrana "⚫ Beklenmeyen Hata" yaz.
        
        # KOD BURAYA (try/except yapısı kur):
        try:
             withdraw_money(customer_requests)
             
        except InsufficientFundsError:
            raise InsufficientFundsError("🔴 Bakiye Yetersiz") 
        
        except ValueError:
            raise ValueError("🟡 Hatalı Giriş")
        
        except Exception:
            raise Exception("⚫ Beklenmeyen Hata")
      

    return successful_balances

# ==========================================
# TEST MOTORU (BURAYI DEĞİŞTİRME)
# ==========================================
def run_tests():
    print("--- 🏦 BANKA SİSTEMİ TESTLERİ BAŞLIYOR 🏦 ---")
    
    # TEST 1: Custom Exception Varlığı
    try:
        raise InsufficientFundsError("Test")
    except InsufficientFundsError:
        print("✅ TODO 1: Özel hata sınıfı doğru tanımlanmış.")
    except NameError:
        print("❌ TODO 1: InsufficientFundsError tanımlanmamış!")
        return

    # TEST 2: Assert ve Raise Mantığı
    try:
        withdraw_money(-50, 10)
        print("❌ TODO 2: Assert çalışmadı! Negatif bakiye kabul edildi.")
    except AssertionError:
        print("✅ TODO 2: Assert doğru çalışıyor (Negatif bakiye engellendi).")
    except:
        print("❌ TODO 2: Yanlış hata türü fırlatıldı (Assert olmalıydı).")

    try:
        withdraw_money(100, -20)
        print("❌ TODO 3: ValueError fırlatılmadı! Negatif çekim kabul edildi.")
    except ValueError:
        print("✅ TODO 3: ValueError doğru çalışıyor.")

    try:
        withdraw_money(50, 100)
        print("❌ TODO 4: Custom Exception fırlatılmadı! Fazla para çekildi.")
    except InsufficientFundsError:
        print("✅ TODO 4: Yetersiz Bakiye hatası doğru çalışıyor.")

    # TEST 3: Try/Except Akışı
    print("\n--- İşlem Kuyruğu Testi ---")
    requests = [
        (1000, 200),  # Başarılı olmalı (Kalan: 800)
        (50, 100),    # Hata: Bakiye yetersiz (Custom Error)
        (200, -50),   # Hata: Negatif giriş (ValueError)
        (500, 100)    # Başarılı olmalı (Kalan: 400)
    ]
    
    results = process_atm_queue(requests)
    
    print(f"Sonuç Listesi: {results}")
    
    if results == [800, 400]:
        print("✅ TODO 5: Try/Except bloğu harika çalışıyor! Hatalı işlemler filtrelendi.")
    else:
        print("❌ TODO 5: Sonuç listesi yanlış. Hataları doğru yakaladığından emin ol.")

if __name__ == "__main__":
    run_tests()