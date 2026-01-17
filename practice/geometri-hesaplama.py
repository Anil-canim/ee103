# Python file for user: anilcanguler

"""
============================================
 EE103 - Python Lab
 Geometry Calculator (Functions + Parameters)
============================================
"""

PI = 3.14

# ---------- GEOMETRY FUNCTIONS ----------

def circle_area(r):
    area = PI * (r**2)
    return area

def circle_perimeter(r):
    perimeter = 2 * PI * r
    return perimeter

def rectangle_area(w, h):
    area = w * h
    return area

def rectangle_perimeter(w, h):
    perimeter = 2 * (w + h)
    return perimeter

def triangle_area(first_side, second_side, third_side):
    from math import sqrt
    u = (first_side + second_side + third_side) / 2
    # Alan hesabı (Heron formülü)
    area = sqrt(u * (u - first_side) * (u - second_side) * (u - third_side))
    return area

# ---------- HELPER FUNCTIONS (INPUT / OUTPUT) ----------

def get_number(msg):
    """
    Kullanıcıdan sayı almak için kullanılan fonksiyon.
    """
    text = input(msg)
    value = float(text)
    return value

def show_result(label, value):
    """
    Sonucu yazdırma fonksiyonu.
    Örn: Alan = 25.0
    """
    print(label, "=", value)

# ---------- MAIN MENU FUNCTION ----------

def main():
    while True:
        print()
        print("=== Geometri Laboratuvarı ===")
        print("1) Daire Hesaplamaları")
        print("2) Dikdörtgen Hesaplamaları")
        print("3) Üçgen Alanı")
        print("4) Çıkış")

        choice = input("Seçiminiz (1-4): ")

        if choice == "1":
            # Daire işlemleri
            r = get_number("Dairenin yarıçapını giriniz: ")
            a = circle_area(r)
            p = circle_perimeter(r)
            show_result("Alan", a)
            show_result("Çevre", p)

        elif choice == "2":
            # Dikdörtgen işlemleri
            w = get_number("Dikdörtgenin genişliğini giriniz: ")
            h = get_number("Dikdörtgenin yüksekliğini giriniz: ")
            
            area = rectangle_area(w, h)
            perimeter = rectangle_perimeter(w, h)
            
            show_result("Alan", area)
            show_result("Çevre", perimeter)

        elif choice == "3":
            # Üçgen işlemleri
            while True:
                f_s = get_number("Üçgenin birinci kenarını giriniz: ")
                s_s = get_number("Üçgenin ikinci kenarını giriniz: ")
                t_s = get_number("Üçgenin üçüncü kenarını giriniz: ")
                
                try:
                    area = triangle_area(f_s, s_s, t_s)
                    show_result("Alan", round(area, 2))
                    break # Hesaplama başarılıysa döngüden çık
                except:
                    # Hata mesajı düzeltildi
                    print("HATA: Bu kenar uzunlukları ile bir üçgen oluşturulamaz!")
                    x = input("Tekrar denemek için 'x' tuşuna basın, menüye dönmek için başka bir tuşa basın: ")
                    if x == "x":
                        continue
                    else:
                        break

        elif choice == "4":
            print("Programdan çıkılıyor...")
            exit()

        else:
            print("Geçersiz seçim, lütfen tekrar deneyiniz.")

# Program buradan başlar
main()