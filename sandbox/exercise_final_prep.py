#Class Yapısı: class Projectile: ile başlayacak.Constructor (__init__): 
# Hız ($v_0$) ve açı ($\theta$) parametrelerini alıp, $v_x$ ve $v_y$ bileşenlerini self değişkenlerine atayacak. 
# (Trigonometriyi math kütüphanesinden alabilirsin, serbest).Metot: update(dt) fonksiyonu her çalıştığında, yerçekimi ($g=9.81$) etkisiyle hızı ve konumu güncelleyecek.
# Simülasyon: Bir while döngüsü ile cisim yere çakılana kadar ($y < 0$) uçuracaksın.

from math import *
V0=float(input("give us the initial speed? "))
theta=float(input("projectile's angle? "))


class Projectile:
    def __init__(self,V0,theta):
        self.vx=V0*cos(theta)
        self.vy=V0*sin(theta)
        self.x=0
        self.y=0
    def update(self,dt):
        self.vy-=9.81*dt
        self.x +=self.vx*dt
        self.y +=dt*(self.vy-(9.81/2)*dt)
        
        if self.y < 0:
            self.y = 0
            # İstersen burada x'i de tam y=0 olduğu ana oranlayabilirsin.
            return False # Simülasyon bitti sinyali
        return True
        

obj=Projectile(V0,radians(theta))
while True:
    
    print(f"X: {obj.x:.4f} | Y: {obj.y:.4f} | Vy: {obj.vy:.4f} | Vf: {sqrt((obj.vx)**2+(obj.vy)**2)}")
    if not obj.update(0.01):
        print(f"Hit the Ground: X: {obj.x:.4f} | Y: {obj.y:.4f} | Vy: {obj.vy:.4f} | Vf: {sqrt((obj.vx)**2+(obj.vy)**2)}")
        break

print("--- Simulation Completed ---")