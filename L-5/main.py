from pygame import *
from random import *
from time import time as timer
import sys
from button import Button
W,H = 1200,800

massive_attack_time = 10
max_enemy1 = 10
max_enemy2 = 1
max_enemy3 = 2
max_pickle = 1
max_bullet1 = 5
coins = 0
pickle_money_need = 25
speed_money_need = 75
massive_attack_money_need = 100
life_money_need = 100
wave = 0
life = 3
goal = 25
window = display.set_mode((W,H))
display.set_caption("space.jpg")
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
                window.blit(self.image, (self.rect.x,self.rect.y))        
class Player(GameSprite):
    def update(self, ):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:   
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < H-150:
            self.rect.y += self.speed
        if keys [K_a] and self.rect.x > 5:   
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < W-55:
            self.rect.x += self.speed

    def fire(self):
        for i in range(max_pickle):
            bullet = Bullet("Pickle.png", self.rect.centerx-randint(-10,40), self.rect.y-randint(10,100), 15, 55, 20)
            bullets.add(bullet)
            
player = Player("nova_rocket_full.png", 250, H-150, 50, 150, 10)        
            
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost   
        if self.rect.y > H:
            self.rect.y = 0
            self.rect.x = randint(80, W-160)
            lost +=1

class Enemy2(GameSprite):
    def __init__(self, img, x, y, w, h, speed, life):
        GameSprite.__init__(self, img, x, y, w, h, speed)
        self.life = life
    def update(self):
        self.rect.y += self.speed
        global lost   
        if self.rect.y > H:
            self.rect.y = 0
            self.rect.x = randint(80, W-160)
            lost +=5
            
class Enemy3(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost   
        if self.rect.y > H:
            self.rect.y = 0
            self.rect.x = randint(80, W-160)
            lost +=9
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill
            
class Bullet2(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = H

from button import Button

#MENU

BG = image.load("space.jpg")

def get_font(size): 
    font.init()
    return font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = mouse.get_pos()

        window.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(W,H))
        window.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(window)
        
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        display.update()

def options_menu():
    global max_enemy1, max_enemy2, max_enemy3, max_pickle, player, max_bullet1, massive_attack_time, life, speeds, massive_attack, lifes, massive_attack_time
    
    a = ("amount of small dumplings")
    b = ("amount of swarm of dumplings")
    c = ("amount of pickles per shoot")
    d = ("amount of red dumplings")
    speeds = ("player speed")
    massive_attack = ("relouding of base turrets")
    lifes = ("number of lifes")
    font.init()
    text1 = sysfont.SysFont(None, 80)
    text3 = sysfont.SysFont(None, 30)
    while True:
        OPTIONS_MOUSE_POS = mouse.get_pos()
        bg = transform.scale(image.load("space.jpg"), (W,H))
        window.blit(bg, (0,0))
        text_max_pickle = text1.render(str(max_pickle), 1, "turquoise")
        window.blit(text_max_pickle, (100, 350))
        
        text_max_enemy1 = text1.render(str(max_enemy1), 1, "turquoise")
        window.blit(text_max_enemy1, (100, 200))
        
        text_max_enemy2 = text1.render(str(max_enemy2), 1, "turquoise")
        window.blit(text_max_enemy2, (100, 250))
        
        text_max_enemy3 = text1.render(str(max_enemy3), 1, "turquoise")
        window.blit(text_max_enemy3, (100, 300))
        
        text_speed = text1.render(str(player.speed), 1, "turquoise")
        window.blit(text_speed, (100, 400))
        
        text_max_bullet1 = text1.render(str(massive_attack_time), 1, "turquoise")
        window.blit(text_max_bullet1, (100, 450))
        
        text_max_lifes = text1.render(str(life), 1, "turquoise")
        window.blit(text_max_lifes, (100, 500))
        
        
        
        PLUS_BUTTON1 = Button(image=None, pos=(235, 230), 
                            text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_enemy1 = text3.render(str(a), 1, "turquoise")
        window.blit(text_max_enemy1, (245, 220))
        
        MINUS_BUTTON1 = Button(image=None, pos=(80, 230), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        PLUS_BUTTON2 = Button(image=None, pos=(235, 275), 
                            text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_enemy2 = text3.render(str(b), 1, "turquoise")
        window.blit(text_max_enemy2, (245, 265))
        
        MINUS_BUTTON2 = Button(image=None, pos=(80, 275), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        PLUS_BUTTON3 = Button(image=None, pos=(235, 370), 
                            text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_pickle = text3.render(str(c), 1, "turquoise")
        window.blit(text_max_pickle, (245, 360))
        
        MINUS_BUTTON3 = Button(image=None, pos=(80,370), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")

        PLUS_BUTTON7 = Button(image=None, pos=(235, 320), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_enemy3 = text3.render(str(d), 1, "turquoise")
        window.blit(text_max_enemy3, (245, 310))
    
        MINUS_BUTTON7 = Button(image=None, pos=(80,320), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        PLUS_BUTTON4 = Button(image=None, pos=(235, 420), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_speed = text3.render(str(speeds), 1, "turquoise")
        window.blit(text_speed, (245, 410))
    
        MINUS_BUTTON4 = Button(image=None, pos=(80,420), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        PLUS_BUTTON5 = Button(image=None, pos=(235, 470), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_massive_attack = text3.render(str(massive_attack), 1, "turquoise")
        window.blit(text_massive_attack, (245, 460))
    
        MINUS_BUTTON5 = Button(image=None, pos=(80,470), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        PLUS_BUTTON6 = Button(image=None, pos=(235, 520), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_lifes = text3.render(str(lifes), 1, "turquoise")
        window.blit(text_max_lifes, (245, 510))
    
        MINUS_BUTTON6 = Button(image=None, pos=(80,520), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        
        
        OPTIONS_TEXT = get_font(55).render("OPTIONS", True, "turquoise")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 80))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(600, 720), 
                            text_input="BACK", font=get_font(75), base_color="turquoise", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON1.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON1.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON2.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON2.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON3.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON3.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON4.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON4.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON5.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON5.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON6.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON6.changeColor(OPTIONS_MOUSE_POS)
        PLUS_BUTTON7.changeColor(OPTIONS_MOUSE_POS)
        MINUS_BUTTON7.changeColor(OPTIONS_MOUSE_POS)
        
        
        OPTIONS_BACK.update(window)
        
        PLUS_BUTTON1.update(window)
        MINUS_BUTTON1.update(window)
        PLUS_BUTTON2.update(window)
        MINUS_BUTTON2.update(window)
        PLUS_BUTTON3.update(window)
        MINUS_BUTTON3.update(window)
        PLUS_BUTTON4.update(window)
        MINUS_BUTTON4.update(window)
        PLUS_BUTTON5.update(window)
        MINUS_BUTTON5.update(window)
        PLUS_BUTTON6.update(window)
        MINUS_BUTTON6.update(window)
        PLUS_BUTTON7.update(window)
        MINUS_BUTTON7.update(window)
        
        for e in event.get():
            if e.type == QUIT:
                window.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if PLUS_BUTTON1.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy1 += 1
                if MINUS_BUTTON1.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy1 -= 1   
                if PLUS_BUTTON2.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy2 += 1
                if MINUS_BUTTON2.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy2 -= 1
                if PLUS_BUTTON3.checkForInput(OPTIONS_MOUSE_POS):
                    max_pickle += 1
                if MINUS_BUTTON3.checkForInput(OPTIONS_MOUSE_POS):
                    max_pickle -= 1
                if PLUS_BUTTON4.checkForInput(OPTIONS_MOUSE_POS):
                    player.speed += 1
                if MINUS_BUTTON4.checkForInput(OPTIONS_MOUSE_POS):
                    player.speed -= 1
                if PLUS_BUTTON5.checkForInput(OPTIONS_MOUSE_POS):
                    massive_attack_time += 1
                if MINUS_BUTTON5.checkForInput(OPTIONS_MOUSE_POS):
                    massive_attack_time -= 1
                if PLUS_BUTTON6.checkForInput(OPTIONS_MOUSE_POS):
                    life += 1
                if MINUS_BUTTON6.checkForInput(OPTIONS_MOUSE_POS):
                    life -= 1
                if PLUS_BUTTON7.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy3 += 1
                if MINUS_BUTTON7.checkForInput(OPTIONS_MOUSE_POS):
                    max_enemy3 -= 1
                
                
        display.update()
def shop_menu():
    global coins, max_pickle, player, max_bullet1, pickle_money_need, life, massive_attack_time, speed_money_need, massive_attack_money_need, life_money_need
    text1 = sysfont.SysFont(None, 80)
    coin_color = (255, 255, 0)
    pickle_info = ("amount of pickles per shoot")
    money_needs = ("money needed to buy = ")
    text3 = sysfont.SysFont(None, 30)
    speeds = ("player speed")
    massive_attack = ("relouding of base turrets")
    lifes = ("number of lifes")
    while True:
        SHOP_MOUSE_POS = mouse.get_pos()

        bg = transform.scale(image.load("space.jpg"), (W,H))
        window.blit(bg, (0,0))

        SHOP_TEXT = get_font(55).render("SHOP", True, "turquoise")
        SHOP_RECT = SHOP_TEXT.get_rect(center=(600, 80))
        window.blit(SHOP_TEXT, SHOP_RECT)

        SHOP_BACK = Button(image=None, pos=(600, 720),
                            text_input="BACK", font=get_font(75), base_color="turquoise", hovering_color="Green")

        SHOP_BACK.changeColor(SHOP_MOUSE_POS)
        
        SHOP_BACK.update(window)
        
        text_coins = text1.render(str(coins), 1, coin_color)
        window.blit(text_coins, (1000, 60))
        
        text_pickle_money_need = text3.render(str(pickle_money_need), 1, coin_color)
        window.blit(text_pickle_money_need, (480, 143))
        text_pickle_money_need = text3.render(str(money_needs), 1, "turquoise")
        window.blit(text_pickle_money_need, (245, 140))
        text_max_pickle = text1.render(str(max_pickle), 1, "turquoise")
        window.blit(text_max_pickle, (100, 110))
        
        text_speed = text1.render(str(player.speed), 1, "turquoise")
        window.blit(text_speed, (100, 160))
        text_speed_money_need = text3.render(str(speed_money_need), 1, coin_color)
        window.blit(text_speed_money_need, (480, 193))
        text_speed_money_need = text3.render(str(money_needs), 1, "turquoise")
        window.blit(text_speed_money_need, (245, 190))
        
        text_life = text3.render(str(money_needs), 1, "turquoise")
        window.blit(text_life, (245, 290))
        text_life_money_need = text3.render(str(life_money_need), 1, coin_color)
        window.blit(text_life_money_need, (480, 293))
        text_max_lifes = text1.render(str(life), 1, "turquoise")
        window.blit(text_max_lifes, (100, 260))
        
        text_massive_attack_time = text1.render(str(massive_attack_time), 1, "turquoise")
        window.blit(text_massive_attack_time, (100, 210))
        text_massive_attack_money_need = text3.render(str(money_needs), 1, "turquoise")
        window.blit(text_massive_attack_money_need, (245, 240))
        text_massive_attack_money_need = text3.render(str(massive_attack_money_need), 1, coin_color)
        window.blit(text_massive_attack_money_need, (480, 243))
        
        SHOP_PLUS_BUTTON1 = Button(image=None, pos=(235, 140), 
                            text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_max_pickle = text3.render(str(pickle_info), 1, "turquoise")
        window.blit(text_max_pickle, (245, 120))
        
        
        SHOP_MINUS_BUTTON1 = Button(image=None, pos=(80, 140), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        SHOP_PLUS_BUTTON2 = Button(image=None, pos=(235, 190), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_speed = text3.render(str(speeds), 1, "turquoise")
        window.blit(text_speed, (245, 170))
    
        SHOP_MINUS_BUTTON2 = Button(image=None, pos=(80,190), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        SHOP_PLUS_BUTTON3 = Button(image=None, pos=(235, 240), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_speed = text3.render(str(massive_attack), 1, "turquoise")
        window.blit(text_speed, (245, 220))
    
        SHOP_MINUS_BUTTON3 = Button(image=None, pos=(80,240), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        SHOP_PLUS_BUTTON4 = Button(image=None, pos=(235, 290), 
                           text_input="+", font=get_font(25), base_color="turquoise", hovering_color="Green")
        text_speed = text3.render(str(lifes), 1, "turquoise")
        window.blit(text_speed, (245, 270))
    
        SHOP_MINUS_BUTTON4 = Button(image=None, pos=(80,290), 
                            text_input="-", font=get_font(25), base_color="turquoise", hovering_color="Green")
        
        SHOP_PLUS_BUTTON1.changeColor(SHOP_MOUSE_POS)
        SHOP_MINUS_BUTTON1.changeColor(SHOP_MOUSE_POS)
        SHOP_PLUS_BUTTON2.changeColor(SHOP_MOUSE_POS)
        SHOP_MINUS_BUTTON2.changeColor(SHOP_MOUSE_POS)
        SHOP_PLUS_BUTTON3.changeColor(SHOP_MOUSE_POS)
        SHOP_MINUS_BUTTON3.changeColor(SHOP_MOUSE_POS)
        SHOP_PLUS_BUTTON4.changeColor(SHOP_MOUSE_POS)
        SHOP_MINUS_BUTTON4.changeColor(SHOP_MOUSE_POS)
        
        SHOP_PLUS_BUTTON1.update(window)
        SHOP_MINUS_BUTTON1.update(window)
        SHOP_PLUS_BUTTON2.update(window)
        SHOP_MINUS_BUTTON2.update(window)
        SHOP_PLUS_BUTTON3.update(window)
        SHOP_MINUS_BUTTON3.update(window)
        SHOP_PLUS_BUTTON4.update(window)
        SHOP_MINUS_BUTTON4.update(window)
        
        for e in event.get():
            if e.type == QUIT:
                window.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                if SHOP_BACK.checkForInput(SHOP_MOUSE_POS):
                    main_menu()
                if SHOP_PLUS_BUTTON1.checkForInput(SHOP_MOUSE_POS) and coins >= pickle_money_need:
                    coins -= pickle_money_need
                    max_pickle += 1
                    pickle_money_need += 25
                    
                if SHOP_MINUS_BUTTON1.checkForInput(SHOP_MOUSE_POS): 
                    max_pickle -= 1
                    
                if SHOP_PLUS_BUTTON2.checkForInput(SHOP_MOUSE_POS) and coins >= speed_money_need:
                    coins -= speed_money_need
                    player.speed += 1
                    speed_money_need += 75
                    
                if SHOP_MINUS_BUTTON2.checkForInput(SHOP_MOUSE_POS):
                    player.speed -= 1
                    
                if SHOP_PLUS_BUTTON3.checkForInput(SHOP_MOUSE_POS):
                    massive_attack_time += 1
                    
                if SHOP_MINUS_BUTTON3.checkForInput(SHOP_MOUSE_POS) and coins >= massive_attack_money_need:
                    coins -= massive_attack_money_need
                    massive_attack_time -= 1
                    massive_attack_money_need += 100
                    if massive_attack_time == 1:
                        massive_attack_money_need += 9000
                    
                if SHOP_PLUS_BUTTON4.checkForInput(SHOP_MOUSE_POS) and coins >= life_money_need:
                    coins -= life_money_need
                    life += 1
                    life_money_need *= 2
                    
                if SHOP_MINUS_BUTTON4.checkForInput(SHOP_MOUSE_POS):
                    life -= 1
                    
        display.update()
def main_menu():
    while True:
        window.blit(BG, (0, 0))

        MENU_MOUSE_POS = mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#40E0D0")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))

        PLAY_BUTTON = Button(image=image.load("Play Rect.png"), pos=(590, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#40E0D0", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=image.load("Options Rect.png"), pos=(590, 550), 
                            text_input="OPTIONS", font=get_font(75), base_color="#40E0D0", hovering_color="Green")
        SHOP_BUTTON = Button(image=image.load("Play Rect.png"), pos=(590, 400), 
                            text_input="SHOP", font=get_font(75), base_color="#40E0D0", hovering_color="Green")
        QUIT_BUTTON = Button(image=image.load("Quit Rect.png"), pos=(590, 700), 
                            text_input="QUIT", font=get_font(75), base_color="#40E0D0", hovering_color="Green")

        window.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SHOP_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)

        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if wave >= 25:
                        options_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit()
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shop_menu()    
                    sys.exit()
        
        display.update()
  
    
def game():
    global bullets, max_pickle, lost, max_enemy1, max_enemy2, max_enemy3, coins, wave, player, life, massive_attack_time, goal, massive_attack_money_need, life_money_need, speed_money_need, pickle_money_need
    background = transform.scale(image.load("space.jpg"), (W,H))    
    lost = 0
    max_lost = 10
    rel_time = False
    num_fire = 0
    score = 0
    bullets = 0
    
    coin = ("Coins")
    waves = ("Wave")
    text4 = sysfont.SysFont(None, 40)
    HP = ("HP")
    mixer.init()
    mixer.music.load("Project Ex - Neo Nebula.mp3")
    fire = mixer.Sound("fire.ogg")
    mixer.Sound.set_volume(fire, 0.1)
    mixer.music.set_volume(0.5)
    mixer.music.play()

    font.init()
    text1 = sysfont.SysFont(None, 80)
    text2 = sysfont.SysFont(None, 36)
    text_win = text1.render("YOU WIN!", 1, (0,255,0))
    text_lose = text1.render("YOU LOSE!", 1, (255,0,0))
    
    bullets = sprite.Group()
    monsters1 = sprite.Group()
    monsters2 = sprite.Group()
    monsters3 = sprite.Group()
    
    for i in range(max_enemy1):
        enemy = Enemy("Пельмешка.png", randint(40, W-40), -60, 60, 70, randint(1,5)/2)
        monsters1.add(enemy)

    for i in range(max_enemy2):
        enemy = Enemy2("Пельмешкабагато.png", randint(40, W-40), -150, 140, 70, randint(1,2), 5)
        monsters2.add(enemy)
    
    for i in range(max_enemy3):
        enemy = Enemy3("червонапельмешка.png", randint(40, W-40), -60, 60, 70, randint(3,7)/2)
        monsters3.add(enemy)
    
    
    game = True
    finish = False           
    clock = time.Clock()
    FPS = 60
    ammo = transform.scale(image.load("Pickle.png"), (10,20))
    massive_fire_time = timer()
    while game:
        x,y = 20, H-50
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if num_fire < max_enemy1//6*5 and rel_time == False:
                        num_fire += 1
                        player.fire()
                        fire.play()
                    if num_fire >= max_enemy1//6*5 and rel_time == False:
                        last_time = timer()
                        rel_time = True 
            if e.type == MOUSEBUTTONDOWN:
                if num_fire < max_enemy1//6*5 and rel_time == False:
                    num_fire += 1
                    player.fire()
                    fire.play()
                if num_fire >= max_enemy1//6*5 and rel_time == False:
                    last_time = timer()
                    rel_time = True 
            
        window.blit(background, (0, 0))
        if not finish:
            player.update()
            player.reset()
            monsters1.update()
            monsters1.draw(window)
            monsters2.update()
            monsters2.draw(window)
            monsters3.update()
            monsters3.draw(window)
            bullets.update()
            bullets.draw(window)
            
            now_time1 = timer()
            if now_time1 - massive_fire_time > massive_attack_time:
                for i in range(max_bullet1):
                    bullet = Bullet("Pickle.png", randint(40, W-40), H, 15, 55, 10)
                    bullets.add(bullet)
                massive_fire_time = timer()
                        
            if rel_time:
                now_time = timer()
                if now_time - last_time < 1:
                    reload = text1.render("Wait for reloading...", 1, (100, 0, 0))
                    window.blit(reload, (10, H-90))
                else:
                    num_fire = 0
                    rel_time = False
                
            for b in range((max_enemy1//6*5)-num_fire):
                window.blit(ammo, (x, y))
                x += 5
                
            text_lost = text2.render("Lost: "+str(lost), 1, (255,255,255),(40,137,67))
            text_score = text2.render("Score: "+str(score), 1, (255,255,255),(40,137,67))
            window.blit(text_lost, (10,50))
            window.blit(text_score, (10,20))
            
            collides = sprite.groupcollide(monsters1, bullets, True, True)
            for c in collides:
                score += 1
                coins += 1
                enemy = Enemy("Пельмешка.png", randint(40, W-40), -60, 60, 70, randint(1,5)/2)
                monsters1.add(enemy)
                
            collides = sprite.groupcollide(monsters2, bullets, False, True)
            for t in collides:
                
                t.life -= 1
                if t.life == 0:
                    t.kill()
                    score += 5
                    coins += 10
                    enemy = Enemy2("Пельмешкабагато.png", randint(40, W-40), -150, 140, 70, randint(1,2), 5)
                    monsters2.add(enemy)
                    
            collides = sprite.groupcollide(monsters3, bullets, True, True)
            for c in collides:
                score += 1
                enemy = Enemy("червонапельмешка.png", randint(40, W-40), -60, 60, 70, randint(1,5)/2)
                monsters1.add(enemy)
            
            if (sprite.spritecollide(player, monsters1, False)):
                sprite.spritecollide(player, monsters1, True)
                monsters1.add(enemy)
                life -= 1
            if (sprite.spritecollide(player, monsters2, False)):
                sprite.spritecollide(player, monsters2, True)
                monsters2.add(enemy)
                life -= 2
            if (sprite.spritecollide(player, monsters3, False)):
                sprite.spritecollide(player, monsters3, True)
                monsters3.add(enemy)
                life -= 3
            
            if score >= goal:
                max_enemy1 +=10
                max_enemy2 +=1
                max_enemy3 +=1
                goal += 25
                wave += 1
                finish = True
                window.blit(text_win, (90,200))
             
            if lost >= max_lost or life <= 0:
                if max_enemy1 or max_enemy2 > 10:
                    max_enemy1 = 10
                    max_enemy2 = 1
                    max_enemy3 = 2
                    goal = 25
                    wave = 0
                    life = 3
                    player.speed = 10
                    massive_attack_time = 10
                    speed_money_need = 75
                    massive_attack_money_need = 100
                    max_pickle = 1
                    main_menu()
                    
                finish = True
                window.blit(text_lose, (200, 200))
                
            if life >= 3:
                life_color = (0,150, 0)
            elif life == 2:
                life_color = (150, 150, 0)
            elif life == 1:
                life_color = (150, 0, 0)
            else:
                life_color = (255, 0, 0)             
            
            if wave <= 3:
                wave_color = (0,255, 0)
            elif wave <= 5:
                wave_color = (153, 204, 0)
            elif wave <= 10:
                wave_color = (51, 153, 102)
            elif wave <= 15:
                wave_color = (128, 0, 0)
            else:
                wave_color = (255, 0, 0)
                
            coin_color = (255, 255, 0)
            
            text_life = text1.render(str(life), 1, life_color)
            window.blit(text_life, (W-100, 20))
            text_HP = text4.render(str(HP), 1, life_color)
            window.blit(text_HP, (W-140, 25))
            text_wave = text1.render(str(wave), 1, wave_color)
            window.blit(text_wave, (W-120, 80))
            text_waves = text4.render(str(waves), 1, wave_color)
            window.blit(text_waves, (W-190, 80))
            text_coins = text1.render(str(coins), 1, coin_color)
            window.blit(text_coins, (W-140, 140))
            text_coin = text4.render(str(coin), 1, coin_color)
            window.blit(text_coin, (W-220, 140))
        else:
            finish = False
            time.delay(3000)
            for b in bullets:
                b.kill()
                
            for n in monsters1:
                n.kill()
            for n in monsters2:
                n.kill()
            for n in monsters3:
                n.kill()   
                
            score = 0
            lost = 0
            rel_time = False
            num_fire = 0
            
            for y in range(1,max_enemy1):
                enemy1 = Enemy("Пельмешка.png", randint(40, W-40), -60, 60, 70, randint(1,5)/2)
                monsters1.add(enemy1)
                
            for y in range(5,max_enemy2):
                enemy2 = Enemy2("Пельмешкабагато.png", randint(40, W-40), -150, 140, 70, randint(1,2), 5)
                monsters2.add(enemy2)
                
            for y in range(5,max_enemy3):
                enemy3 = Enemy3("червонапельмешка.png", randint(40, W-40), -60, 60, 70, randint(1,2)/2)
                monsters3.add(enemy3)    
        display.update()
        clock.tick(FPS)

main_menu()
