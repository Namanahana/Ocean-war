#pgzero
import random
import time

WIDTH = 600
HEIGHT = 450

TITLE = "Pertempuran bawah air"
FPS = 30

# Objek dan variabel
ship = Actor("ship", (300, 400))
space = Actor("bg7",(300,225)) 
robos = []
sampahs = [Actor("sampah1", (700, random.randint(45, 450))), Actor("sampah2", (700, random.randint(45, 450))), Actor("sampah3", (700, random.randint(45, 450)))]
ikan = []
mode = 'intro'
type1 = Actor('kasel450', (100, 300))
type2 = Actor('kasel250', (300, 300))
type3 = Actor('kasel351', (500, 300))
missiles1 = []
count = 0
bos1 = Actor('bos1', (800, 300))
bos1.direction = 0
bos1.health = 5
peluru_bos = []
y_nembak = random.randint(50, 100)
intro1 = Actor('prof', (300,250))
text1 = Actor('text1', (300,80))
t_next = Actor('next',(550,400))

# Membuat daftar musuh
for i in range(5):
    x = 650
    y = random.randint(60, 400)
    robo2 = Actor("robo2", (x, y))
    robo2.speed = random.randint(2, 8)
    robos.append(robo2)
    
# Membuat daftar ikan
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(100, 200)
    hiu = Actor("hiu", (x, y))
    hiu.speed = random.randint(2, 10)
    ikan.append(hiu)

# Menggambar
def draw():
    # Mode permainan
    if mode == 'game':
        space.draw()
        screen.draw.text(count, (30, 30), color = "white", fontsize = 20)
        if (count >= 10 and bos1.image == 'bos1') or (count >= 20 and bos1.image == 'bos2') or (count >= 30 and bos1.image == 'bos3'):
            screen.draw.text("HP BOSS:", (450, 30), color = "red", fontsize = 20)
            screen.draw.text(bos1.health, (550, 30), color = "red", fontsize = 20)
        bos1.draw()
        sampahs[0].draw()
        # Menggambar ikan
        for i in range(len(ikan)):
            ikan[i].draw()
        ship.draw()
        # Menggambar musuh
        for i in range(len(robos)):
            robos[i].draw()
        for i in range(len(missiles1)):
            missiles1[i].draw()

        for i in range(len(peluru_bos)):
            peluru_bos[i].draw()
            
            
    elif mode == 'menu':
        space.draw()
        type1.draw()
        type2.draw()
        type3.draw()
        screen.draw.text("Pilih kapal selam kamu!", center = (300, 150), color = "yellow", fontsize = 30)
        screen.draw.text("Tembak : klik kiri", center = (300, 400), color = "white", fontsize = 15)
        
    # Jendela permainan berakhir   
    elif mode == 'end' :
        space.draw()
        screen.draw.text("Kamu kalah!", center = (300, 200), color = "white", fontsize = 36)
        
    elif mode == 'menang':
        space.draw()
        screen.draw.text("Kamu menang!", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text("Dunia telah terselamatkan dari kehancuran", center = (300, 250), color = "white", fontsize = 16)
        
    elif mode == 'intro':
        screen.fill('black')
        intro1.draw()
        text1.draw()
        t_next.draw()
        
        #screen.draw.text("Seorang profesor yang terobsesi untuk meningkatkan kecerdasan makhluk laut", center = (300, 100), color = "white", fontsize = 16)
        #time.sleep(2)
        #screen.draw.text("telah melakukan eksperimen ilegal secara rahasia", center = (300, 120), color = "white", fontsize = 16)
        #time.sleep(2)
        #screen.draw.text("formula rahasia telah mengalami mutasi genetik secara mengejutkan", center = (300, 140), color = "white", fontsize = 16)
        #time.sleep(2)
        #screen.draw.text("sehingga membuat makhluk eksperimen memiliki kecerdasan yang membahayakan", center = (300, 160), color = "white", fontsize = 16)
        #time.sleep(2)
        #screen.draw.text("KITA HARUS SELAMATKAN DUNIA DARI KEHANCURAN!!!", center = (300, 180), color = "white", fontsize = 16)
        #time.sleep(2)
        
def on_mouse_down(button, pos):
    global mode
    if button == mouse.LEFT:
        if mode == 'menu':
            if type1.collidepoint(pos):
                ship.image = 'kasel450'
                mode = 'game'
            elif type2.collidepoint(pos):
                ship.image = 'kasel250'
                mode = 'game'
            elif type3.collidepoint(pos):
                ship.image = 'kasel351'
                mode = 'game'
        if mode == 'game':
            bullet = Actor('missiles1', pos)
            missiles1.append(bullet)
            
        if mode == 'intro':
            if t_next.collidepoint(pos) and text1.image == 'text1':
                text1.image = 'text2c'
            elif t_next.collidepoint(pos) and text1.image == 'text2c':
                text1.image = 'text3a'
            elif t_next.collidepoint(pos) and text1.image == 'text3a':
                text1.image = 'text4a'
                intro1.image = 'bos3' 
            elif t_next.collidepoint(pos) and text1.image == 'text4a':
                text1.image = 'text5b'
                intro1.image = 'bos1'
            elif t_next.collidepoint(pos) and text1.image == 'text5b':
                text1.image = 'text6a' 
                intro1.image = 'bos2'
            elif t_next.collidepoint(pos) and text1.image == 'text6a':
                mode = 'menu'
                
# Kontrol
def on_mouse_move(pos):
    ship.pos = pos

# Menambahkan musuh baru ke daftar
def new_enemy():
    x = 650
    y = random.randint(60, 400)
    robo2 = Actor("robo2", (x, y))
    robo2.speed = random.randint(2, 3)
    robos.append(robo2)

# Pergerakan musuh
def enemy_fish():
    for i in range(len(robos)):
        if robos[i].x > -40:
            robos[i].x = robos[i].x - robos[i].speed
        else:
            robos.pop(i)
            new_enemy()

# Pergerakan sampah
def sampah():
    if sampahs[0].x > -40:
            sampahs[0].x = sampahs[0].x - 3
    else:
        sampahs[0].x = -100
        sampahs[0].y = random.randint(45, 450)
        first = sampahs.pop(0)
        sampahs.append(first)


# Pergerakan ikan
def ikans():
    for i in range(len(ikan)):
        if ikan[i].x > 0:
            ikan[i].x = ikan[i].x - ikan[i].speed
        else:
            ikan[i].y = random.randint(100, 400)
            ikan[i].x = 600
            ikan[i].speed = random.randint(2, 10)

# Collisions (tabrakan-tabrakan)
def collisions():
    global mode
    global count
    for j in range(len(missiles1)):
        cek = 0
        for i in range(len(robos)):
            if robos[i].colliderect(missiles1[j]):
                robos.pop(i)
                missiles1.pop(j)
                new_enemy()
                count = count + 1
                cek = 1
                break
            if ship.colliderect(robos[i]):
                mode = 'end'
        if cek == 1:
            break
        if bos1.colliderect(missiles1[j]):
            missiles1.pop(j)
            bos1.health -= 1
            break
                
    for k in range(len(peluru_bos)):
        if ship.colliderect(peluru_bos[k]):
            mode = 'end'

            
def update(dt):
    global y_nembak
    global robos
    global mode
    if mode == 'game':
        # if count < 10:
        enemy_fish()
        collisions()
        sampah()
        ikans()
        if count >= 10:
            if bos1.x >500 and bos1.image == 'bos1':
                bos1.x -= 5
            if bos1.health >0 and bos1.image == 'bos1' :
                robos = []
            if bos1.health <=0 and bos1.image == 'bos1':
                # Membuat daftar musuh
                for i in range(5):
                    x = 650
                    y = random.randint(60, 400)
                    robo2 = Actor("robo2", (x, y))
                    robo2.speed = random.randint(2, 8)
                    robos.append(robo2)
                bos1.image = 'bos2'
                bos1.health = 10
                bos1.x =800
        if count >= 20 and bos1.image == 'bos2':
            if bos1.x >500 and bos1.image == 'bos2':
                bos1.x -= 5
            if bos1.health > 0  and bos1.image == 'bos2':
                robos = []
            if bos1.health <=0 and bos1.image == 'bos2':
                # Membuat daftar musuh
                for i in range(5):
                    x = 650
                    y = random.randint(60, 400)
                    robo2 = Actor("robo2", (x, y))
                    robo2.speed = random.randint(2, 8)
                    robos.append(robo2)
                bos1.image = 'bos3'   
                bos1.health = 30
                bos1.x =800
        if count >= 30 and bos1.image == 'bos3':
            if bos1.x >500 and bos1.image == 'bos3':
                bos1.x -= 5
            if bos1.health > 0  and bos1.image == 'bos3':
                robos = []
            if bos1.health <=0 and bos1.image == 'bos3':
                # Membuat daftar musuh
                for i in range(5):
                    x = 650
                    y = random.randint(60, 400)
                    robo2 = Actor("robo2", (x, y))
                    robo2.speed = random.randint(2, 8)
                    robos.append(robo2)
                # bos1.image = 'bos3'   
                bos1.health = 30
                bos1.x =800
                mode = "menang"
                
        if bos1.direction == 0:
            bos1.y -= 5
            y_nembak -= 5
            if y_nembak <= 0 and bos1.x <610:
                bos_peluru = Actor('peluru_bos', bos1.pos) 
                peluru_bos.append(bos_peluru)
                y_nembak = random.randint(50, 100)
            if bos1.y < 0:
                bos1.direction = 1
        else:
            bos1.y += 5
            y_nembak -= 5
            if y_nembak <= 0  and bos1.x <610:
                bos_peluru = Actor('peluru_bos', bos1.pos)
                peluru_bos.append(bos_peluru)
                y_nembak = random.randint(50, 100)
            if bos1.y > HEIGHT:
                bos1.direction = 0
        
        
        for i in range(len(peluru_bos)):
            if peluru_bos[i].x > -20:
                peluru_bos[i].x = peluru_bos[i].x - 20
            else:
                peluru_bos.pop(i)
                break
        
        for i in range(len(missiles1)):
            if missiles1[i].x < WIDTH + 20:
                missiles1[i].x = missiles1[i].x + 20
            else:
                missiles1.pop(i)
                break
            
