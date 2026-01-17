class Kapasitor:
    def __init__(self, kapasite, max_voltaj):
        self.kapasite = kapasite
        self.max_voltaj = max_voltaj
        self.mevcut_voltaj = 0 # Başlangıçta boş
        print(f"{kapasite}uF Kapasitör üretildi. Limit: {max_voltaj}V")

    def sarj_et(self, gelen_voltaj):
        # BURASI SENDE!
        if gelen_voltaj>self.max_voltaj:
            print("PATLADI")
        else:
            self.mevcut_voltaj=gelen_voltaj
        # Mantık: 
        # 1. Eğer gelen_voltaj > self.max_voltaj ise: Ekrana "PATLADI" yaz.
        # 2. Değilse: self.mevcut_voltaj değerini gelen_voltaj yap. Ekrana "Şarj oldu" yaz.
        

    def bilgi_ver(self):
        print(f"{self.kapasite}uF and {self.mevcut_voltaj}V")
        # BURASI DA SENDE!
        # Ekrana şunu yazdır: "Şu anki voltaj: [değer] V"
        pass

# TEST KISMI (Buna dokunma, kodunu bitirince çalıştır)
c1 = Kapasitor(1000, 25) # 1000uF, Max 25V
c1.bilgi_ver()

c1.sarj_et(10) # Sorun olmamalı
c1.bilgi_ver()

c1.sarj_et(50) # BURADA PATLAMALI!

      