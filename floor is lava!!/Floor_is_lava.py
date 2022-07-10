#importing modules
import pygame
import time
import random
import math
pygame.init()
#screen
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption('The floor is lava')
background = pygame.image.load('background.png')
icon = pygame.image.load('icon_lava.png')
pygame.display.set_icon(icon)  
#sound effects
jump_sound = pygame.mixer.Sound('jump.wav')
coin_sound = pygame.mixer.Sound('coin.wav')
hurt_sound = pygame.mixer.Sound('hurt.wav')
shoot_sound = pygame.mixer.Sound('shoot.wav')
#bullet class
class Bullets():
    def __init__(self, bullet_right_img, bullet_left_img, bulletX_change):
        self.bullet_right_img = bullet_right_img
        self.bullet_left_img = bullet_left_img
        self.bulletX_change  = bulletX_change
        self.bulletX = 0
        self.bulletY = 0
        self.bullet_side = 'right'
        self.bullet_state = 'ready'

#bullets
#(bullet_right_img, bullet_left_img, bulletX_change)
pistol_bullet = Bullets(pygame.image.load('bullet_right.png'), pygame.image.load('bullet_left.png'), 0.1) 
#player class
class Player:
    def __init__(self, x , y , speed , y_change , jump_height , gravity , power, gun, name, hp):
        self.x = x
        self.y = y
        self.speed = speed
        self.y_change = y_change
        self.jump_height = jump_height
        self.power = power
        self.gun = gun
        self.name = name
        self.gravity = gravity
        self.hp = hp
        self.max_hp = self.hp
    def re_image(self):
        if self.power == True:    
            self.image = pygame.image.load(self.name + '.png')
            self.image_left = pygame.image.load(self.name + '_left.png')
            self.image_right = pygame.image.load(self.name + '_right.png')
            self.image_right_power = pygame.image.load(self.name + '_right_power.png')
            self.image_left_power = pygame.image.load(self.name + '_left_power.png')
        else:
            self.image = pygame.image.load(self.name + '.png')
            self.image_left = pygame.image.load(self.name + '_left.png')
            self.image_right = pygame.image.load(self.name + '_right.png')
            self.image_right_power = pygame.image.load(self.name + '_right.png')
            self.image_left_power = pygame.image.load(self.name + '_left.png')
    
    def draw_player(self , image):
        screen.blit(image, (self.x, self.y))
#initialisation
sam = Player(300 , 530 , 5 , 10 , 100, 5, False ,False,'sam', 100)
jump = False
left = False
right = True
collision_sam = True
jump_height = sam.y - 200
win = False
can_jump = True
death = False
sam_x_change = 0
sam_img = pygame.image.load('sam.png')
player_1_attack_radius = 0
player_1_attack_power = 0
player_1_fire = False
recent_key = 'right'

#characters Player(x , y , speed , jump_speed , jump_height , gravity ,  power(Boolean) , gun ,name, hp)
default = Player(300 , 530 , 5 , 10 , 110, 5 , False ,False,'sam', 100)
azerbaijan_knight = Player(300, 530, 5, 10, 100, 5 , True,False, 'azerbaijan_knight', 120)
rabbit = Player(300, 530, 6, 10, 130, 5 , False, False, 'rabbit', 90) 
ethan = Player(300, 530, 5, 10, 110, 5 , True, False, 'ethan', 110)
cowboy = Player(300, 530, 5, 10, 110, 5 , False, True, 'cowboy', 100)
dog = Player(300, 530, 8, 10, 100, 5 , False, False, 'dog' , 90)
astronaut = Player(300, 530, 3, 10, 120 , 2, False, False, 'astronaut' , 90)

#enemy
class Enemy:
    def __init__(self , x , y , speed , name , power , radius, hp):
        enemy_list.append(self)
        self.x = x
        self.x = x
        self.y = y
        self.speed = speed
        self.name = name
        self.power = power
        self.image = pygame.image.load(name + '.png')
        self.image_right = pygame.image.load(name + '_right.png')
        self.image_left = pygame.image.load(name + '_left.png')
        self.current_image = self.image
        self.radius = radius
        self.is_attacking = False
        self.direction = ''
        self.hp = hp
        self.max_hp = self.hp
        if name == 'orc':
            self.image_right_power = pygame.image.load(name + '_right_attack.png')
            self.image_left_power = pygame.image.load(name + '_left_attack.png')
        else:
            self.image_right_power = pygame.image.load(name + '_right.png')
            self.image_left_power = pygame.image.load(name + '_left.png')
    def draw_enemy(self):
        if self.hp > 0:
            screen.blit(self.current_image, (self.x, self.y))
    def move(self):
        global sam
        if self.hp > 0:
            if self.x > sam.x:
                self.x -= self.speed
                self.direction = 'left'
                if self.is_attacking == False:    
                    self.current_image = self.image_left
            elif self.x < sam.x:
                self.x += self.speed
                self.direction = 'right'
                if self.is_attacking == False:   
                    self.current_image = self.image_right
            elif dist(self.x , sam.x , self.y , sam.y) < self.radius:
                self.is_attacking = True
                sam.hp -= self.power
                hurt_sound.play()
                if self.direction == 'left':
                    self.current_image = self.image_left_power
                else:
                    self.current_image = self.image_right_power
            else:
                self.current_image = self.image

        
enemy_list = []
orc = Enemy(540, 530, 5, 'orc', 1, 10, 75)
goblin = Enemy(0, 530, 10, 'goblin', 0.1, 5, 50)
        
#lava
lava_x = 0
lava_y = 600
lava_w = 600
lava_h = 0
lava_speed = 1
lava_rise = False
lava_time = 1000
#platforms class and other
pM = 2
pM2 = 2 
platform_list = []
#coordinates
class Platform:
    def __init__(self, x, y):
        platform_list.append(self)
        self.x = x
        self.y = y
        self.w = 70
        self.h = 10
    
    def colllsion_platform(self, sam_x, sam_y):
        global collision_sam
        if (sam_y + 45) == (self.y - self.h) and sam_x > (self.x - 40) and sam_x < (self.x + 40) and jump == False or sam_y == 530:
            collision_sam = True
    
    def platform(self):
        pygame.draw.rect(screen, (168, 117, 16), (self.x, self.y, self.w, self.h))

platform1 = Platform(random.randint(0,300), 520)
platform2 = Platform(random.randint(platform1.x - 7,300), 460)
platform3 = Platform(1, 400)
platform4 = Platform(random.randint(200,400), 340)
platform5 = Platform(random.randint(platform4.x - 7,platform4.x + 7), 280)
platform6 = Platform(540, 220)
platform7 = Platform(random.randint(0,540), 160)

#coin
coin_img = pygame.image.load('coin.png')
coin_y = platform7.y - 60
coin_x = platform7.x

#score
score_value = 0
font = pygame.font.SysFont('arial', 32)
#functions
menu_running = True
def menu():
    #variables
    global menu_running
    bg =  pygame.image.load('Menu_bg.png')
    page = 1
    player_select1 = False
    player_select2 = False
    #main loop
    while menu_running:
        #background
        if player_select1 == True or player_select2 == True:
            if page == 1:
                bg = pygame.image.load('player_select_bg.png')
            if page == 2:
                bg = pygame.image.load('player_select_bg_2.png')
        screen.blit(bg , (0,0))
        #keyboard listening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    player_select1 = True
                    time.sleep(1)
                elif event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_p:
                    page += 1
                    time.sleep(1)
                elif event.key == pygame.K_o:
                    page -= 1
                    time.sleep(1)
                elif event.key == pygame.K_1 and player_select1 == True :
                    if page == 1:
                        change_character(dog)
                        menu_running = False
                    else:
                        change_character(astronaut)
                        menu_running = False
                elif event.key == pygame.K_2 and player_select1 == True:
                    change_character(azerbaijan_knight)
                    menu_running = False
                elif event.key == pygame.K_3 and player_select1 == True:
                    change_character(rabbit)
                    menu_running = False
                elif event.key == pygame.K_4 and player_select1 == True:
                    change_character(cowboy)
                    menu_running = False
                elif event.key == pygame.K_5 and player_select1 == True:
                    change_character(ethan)
                    menu_running = False
                elif event.key == pygame.K_6 and player_select1 == True:
                    change_character(sam)
                    menu_running = False
        #updtae screen
        pygame.display.update()
        
def gravity():
    global collision_sam
    global sam
    if sam.y < 530:
        sam.y += sam.gravity

def lava(lava_h , time):
    green = (((math.sin(time)) + 2) * 30)
    pygame.draw.rect(screen, (255,green,0), (lava_x,lava_y,lava_w, lava_h))

def show_score(x , y):
    score = font.render('SCORE: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def dist(x1,x2,y1,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def show_hp(x , y):
    global sam
    green_w = sam.hp / 2
    red_w = (sam.max_hp / 2 ) - green_w
    hp_h = 5
    pygame.draw.rect(screen, (0, 255, 0), (x + red_w , y, green_w, hp_h))
    if sam.hp < sam.max_hp:
        pygame.draw.rect(screen, (255 , 0, 0), (x, y, red_w, hp_h))

def retry():
    retry = font.render(('PRESS R TO RETRY'), True, (255, 255, 255))
    screen.blit(retry, (50, 500))
    score_value = 0

def attack():
    global sam
    global enemy_list
    global player_1_attack_radius
    global player_1_attack_power
    global recent_key
    if sam.name == 'azerbaijan_knight':  
        player_1_attack_power = 25
        player_1_attack_radius = 5 
        fire = False
    if sam.name == 'ethan':
        player_1_attack_power = 25
        player_1_attack_radius = 5
        fire = False
    for i in enemy_list:
        if dist(i.x , sam.x , i.y , sam.y) < player_1_attack_radius:
            if recent_key == 'right':
                if i.x >= sam.x:
                    i.hp -= player_1_attack_power
            if recent_key == 'left':
                if i.x <= sam.x:
                    i.hp -= player_1_attack_power

def reset():
    global sam
    global lava_h
    global tick
    global win
    global jump
    time.sleep(1)
    platform1.x  = random.randint(20,500)
    platform2.x  = random.randint(platform1.x - 15,platform1.x + 15)
    platform4.x  = random.randint(50,500)
    platform5.x  = random.randint(platform4.x - 15,platform4.x + 15)
    sam.y = 530
    sam.x = 300
    lava_h = 0
    tick = 0
    jump = False
    win = False

def change_character(other):
    global sam
    sam.speed = other.speed
    sam.y_change = other.y_change
    sam.jump_height = other.jump_height
    sam.power = other.power
    sam.name = other.name
    sam.gun = other.gun
    sam.max_hp = other.max_hp
    sam.hp = other.hp
    sam.gravity = other.gravity
    sam.re_image()

def coin(coin_x, coin_y):
    screen.blit(coin_img, (coin_x, coin_y))

def collision(x1, y1, x2, y2):
    global collision_sam
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 27:
        return True
    else:
        return False
def show_high_score(x,y,score_value):
    high_score_file = open("high_score.txt", "r")
    if eval(high_score_file.read() + '<' + str(score_value)) ==  True:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(score_value))
        high_score_file.close()
        high_score_file = open("high_score.txt", "r")
        high_score = font.render('HIGH SCORE: ' + (high_score_file.read()), True, (255, 255, 255))
        screen.blit(high_score, (x, y))
        high_score_file.close()
    else:
        high_score_file = open("high_score.txt", "r")
        high_score = font.render('HIGH SCORE: ' + (high_score_file.read()), True, (255, 255, 255))
        screen.blit(high_score, (x, y))
        high_score_file.close()
    
    
#main loop
tick = 0
running = True
while running:
    #draw bg
    screen.blit(background, (0,0))
    #memu
    if menu_running == True:
        menu()
    tick += 1
    #regenrating a new map
    if win == True:
        reset()
        lava_speed += 1
        lava_time -= 10
        for i in enemy_list:
            i.hp = i.max_hp
    #time controller
    time.sleep(0.01)
    #checking if lava should rise
    if tick <= lava_time:
        tick += 1
        lava_rise = False
    else:
        lava_rise = True
    #speed controller
    time.sleep(0.001)
    #collision
    collision_sam = False
    if jump == False:
        jump_height = sam.y - sam.jump_height
    #keyboard listening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and death == True:
                reset()
                score_value = 0
                background = pygame.image.load('background.png')
                lava_speed = 1
                lava_time = 1000
                death = False
                menu_running = True
                sam.hp = sam.max_hp
            elif event.key ==  pygame.K_m:
                if sam.gun == False:
                    attack()
                    if recent_key == 'right':
                        sam_img = sam.image_right_power
                    if recent_key == 'left':
                        sam_img = sam.image_left_power
                if sam.gun == True and pistol_bullet.bullet_state == 'ready':
                    shoot_sound.play()
                    if recent_key == 'right':
                        sam_img = sam.image_right
                        pistol_bullet.bullet_side = 'right'
                    if recent_key == 'left':
                        pistol_bullet.bullet_side = 'left'
                        sam_img = sam.image_left
                    pistol_bullet.bulletY = sam.y
                    pistol_bullet.bulletX = sam.x
                    pistol_bullet.bullet_state = 'fire'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                left = False
                right = True
                sam_x_change = sam.speed
                sam_img = sam.image_right
                recent_key = 'right' 
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                sam_x_change = 0 - sam.speed
                right = False
                left = True
                sam_img = sam.image_left
                recent_key = 'left'
            if event.key == pygame.K_UP and can_jump == True  or  event.key == pygame.K_w and can_jump == True:
                jump = True
                jump_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                sam_x_change = 0
                sam_img = sam.image
    #drawing
    if death == False:
        for i in platform_list:
            i.colllsion_platform(sam.x, sam.y)
            i.platform()
        if score_value >= 4:
            for i in enemy_list:
                i.draw_enemy()
                i.move()
        if collision_sam == True:
            can_jump = True
        else:
            can_jump = False
    #sam movement
    if jump == True:
        #jump
        if sam.y != jump_height:
            sam.y -= sam.y_change
        else:
            jump = False
    #left + right
    sam.x = sam.x + sam_x_change
    #boundries
    if sam.x > 536:
        sam.x = 536
    if sam.x < 0:
        sam.x = 0 
    #platform movement
    platform3.x -= pM
    platform6.x -= pM2
    if platform6.x < 0 or platform6.x > 550:
        pM2 *= -1
    if platform3.x < 0 or platform3.x > 550:
        pM *= -1
    #collision with coin
    coin_x = platform7.x
    if collision(coin_x, coin_y, sam.x, sam.y) == True and win == False:
        coin_x = random.randint(0, 530)
        score_value += 1
        coin_sound.play()
        win = True
    #lava death
    if (lava_y + lava_h) <= sam.y:
        death = True
        pygame.display.set_caption('GAME OVER!!')
        background = pygame.image.load('gameover.png') 
    #gravity
    if collision_sam == False:
        gravity()
    #drawing
    if death == False:
        font = pygame.font.SysFont('arial', 32)
        sam.draw_player(sam_img)
        if tick < 10: 
            sam_img = sam.image
        if win == False:
            coin(coin_x, coin_y)
        show_score(0, 0)
        show_hp(sam.x + 10, sam.y - 10)
        if lava_rise == True:
            lava(lava_h , tick)
            lava_h -= lava_speed
    
    #game over scene
    else:
        retry()
        font = pygame.font.SysFont('arial', 50)
        show_score(200,400)
        show_high_score(100,350, score_value)
    #hp check
    if sam.hp <= 0:
        death = True
        pygame.display.set_caption('GAME OVER!!')
        background = pygame.image.load('gameover.png')
    #bullet code 
    if pistol_bullet.bullet_state == 'fire':
        if pistol_bullet.bullet_side == 'right':
            screen.blit(pygame.image.load('bullet_right.png'),(pistol_bullet.bulletX + 20, pistol_bullet.bulletY + 30))
            pistol_bullet.bulletX += 7
        if pistol_bullet.bullet_side == 'left':
            screen.blit(pygame.image.load('bullet_left.png'),(pistol_bullet.bulletX, pistol_bullet.bulletY + 30))
            pistol_bullet.bulletX -= 7
    if pistol_bullet.bulletX > 600 or pistol_bullet.bulletX < 0:
        pistol_bullet.bullet_state = 'ready'
    for i in enemy_list:
        if dist(pistol_bullet.bulletX , i.x,pistol_bullet.bulletY,i.y) < 20:
            pistol_bullet.bullet_state = 'ready'
            i.hp -= 5 
            
    pygame.display.update()
#quit
pygame.quit()