#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Hayvan Avcısı"
FPS = 30

# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
oyna = Actor("oyna", (300, 100))
carpi = Actor("çarpı", (580, 20))
dukkan = Actor("mağaza", (300, 200))
koleksiyon = Actor("koleksiyon", (300, 300))
timsah = Actor("timsah", (120, 180))
suaygiri = Actor("suaygırı", (320, 180))

# Değişkenler
puan = 0
tiklama = 1000
mod = 'menü'

def draw():
    if mod == 'menü':
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 36)
        dukkan.draw()
        koleksiyon.draw()
    
    elif mod == 'dukkan':
        arkaplan.draw()
        carpi.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 36)
        timsah.draw()
        suaygiri.draw()
        screen.draw.text("500$", center=(120, 280), color="white", fontsize = 36)
        screen.draw.text("2500$", center=(320, 280), color="white", fontsize = 36)
        
        
    elif mod == 'oyun':    
        arkaplan.draw()
        hayvan.draw()
        screen.draw.text(puan, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("Ücret : 15$", center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("Ücret : 50$", center=(450, 210), color="black", fontsize = 20)
        carpi.draw()

def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def on_mouse_down(button, pos):
    global puan
    global mod
    global tiklama
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
         # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
        # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            if puan >= 15:
                schedule_interval(bonus_1_icin, 2)
                puan -= 15
         # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            if puan >= 50:
                schedule_interval(bonus_2_icin, 2)
                puan -= 50
        # Menu mode
        elif carpi.collidepoint(pos):
            mod = 'menü'
            
        
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
        
        if dukkan.collidepoint(pos):
            mod = 'dukkan'
            
    elif mod == 'dukkan' and button == mouse.LEFT:        
        if carpi.collidepoint(pos):
            mod = 'menü'
            
        if timsah.collidepoint(pos) and puan >= 500:
            puan -= 500
            hayvan.image = 'timsah'
            tiklama = 5
        if suaygiri.collidepoint(pos) and puan >= 2500:
            puan -= 2500
            hayvan.image = 'suaygırı'
            tiklama = 10
            
