#importing
import random
import pygame
#init and screen
pygame.init()
screen = pygame.display.set_mode([600,600])
bg = pygame.image.load('game_bg1.png')
pygame.display.set_caption('Keyboard master')
icon = pygame.image.load('keyboard_icon.png')
pygame.display.set_icon(icon)
#sound effects
pygame.mixer.music.load('bg_sound.mp3')
pygame.mixer.music.play(-1)
#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
#heart
heart_img = pygame.image.load('heart.png')
lives = 3
#keys
key_image = []
key_x = []
key_y = []
key_speed = []
key_nums = []
amount_keys = 8
for i in range(amount_keys):
    key_nums.append(random.randint(1,4))
    if key_nums[i] == 1:
        key_name = 'up'
    elif key_nums[i] == 2:
        key_name = 'down'
    elif key_nums[i] == 3:
        key_name = 'right'
    else:
        key_name = 'left'
    key_image.append(pygame.image.load(key_name + '_arrow_key.png'))
    key_x.append((64*i) + (204 / amount_keys))
    key_y.append(random.randint(-64,0))
    key_speed.append(random.randint(1, 5))
#functions
def show_score():
    score_text = font.render('SCORE: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (0, 0))
def hit_square():
    pygame.draw.rect(screen, (0,0,0), (0, 536, 600, 64))
#main_loop
running = True
while running:
    #keyboard listening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            for i in range(amount_keys):
                if event.key == pygame.K_RIGHT and key_y[i] <= 600 and key_y[i] >= 536 and key_nums[i] == 3:
                    score += 1
                    key_y[i] = random.randint(-64,0)
                    key_nums[i] = random.randint(1,4)
                    if key_nums[i] == 1:
                        key_name = 'up'
                    elif key_nums[i] == 2:
                        key_name = 'down'
                    elif key_nums[i] == 3:
                        key_name = 'right'
                    else:
                        key_name = 'left'
                    key_image[i] = (pygame.image.load(key_name + '_arrow_key.png'))
                if event.key == pygame.K_LEFT and key_y[i] <= 600 and key_y[i] >= 536 and key_nums[i] == 4:
                    score += 1
                    key_y[i] = random.randint(-64,0)
                    key_nums[i] = random.randint(1,4)
                    if key_nums[i] == 1:
                        key_name = 'up'
                    elif key_nums[i] == 2:
                        key_name = 'down'
                    elif key_nums[i] == 3:
                        key_name = 'right'
                    else:
                        key_name = 'left'
                    key_image[i] = (pygame.image.load(key_name + '_arrow_key.png'))
                if event.key == pygame.K_UP and key_y[i] <= 600 and key_y[i] >= 536 and key_nums[i] == 1:
                    score += 1
                    key_y[i] = random.randint(-64,0)
                    key_nums[i] = random.randint(1,4)
                    if key_nums[i] == 1:
                        key_name = 'up'
                    elif key_nums[i] == 2:
                        key_name = 'down'
                    elif key_nums[i] == 3:
                        key_name = 'right'
                    else:
                        key_name = 'left'
                    key_image[i] = (pygame.image.load(key_name + '_arrow_key.png'))
                if event.key == pygame.K_DOWN and key_y[i] <= 600 and key_y[i] >= 536 and key_nums[i] == 2:
                    score += 1
                    key_y[i] = random.randint(-64,0)
                    key_nums[i] = random.randint(1,4)
                    if key_nums[i] == 1:
                        key_name = 'up'
                    elif key_nums[i] == 2:
                        key_name = 'down'
                    elif key_nums[i] == 3:
                        key_name = 'right'
                    else:
                        key_name = 'left'
                    key_image[i] = (pygame.image.load(key_name + '_arrow_key.png'))
    #drawing
        #bg
    screen.blit(bg , (0,0))
        #hit square
    hit_square()
        #keys
    for i in range(amount_keys):
        screen.blit(key_image[i], (key_x[i], key_y[i]))
        key_y[i] += (key_speed[i]/10)
        if key_y[i] >= 600:
            lives -= 1
            key_y[i] = random.randint(-64,0)
            key_nums[i] = random.randint(1,4)
            if key_nums[i] == 1:
                key_name = 'up'
            elif key_nums[i] == 2:
                key_name = 'down'
            elif key_nums[i] == 3:
                key_name = 'right'
            else:
                key_name = 'left'
            key_image[i] = (pygame.image.load(key_name + '_arrow_key.png'))
        #heart
    for i in range(lives):
        screen.blit(heart_img, (64*i + 408, 0))
    #score
    show_score()
    #update
    pygame.display.update()
    #quiting
    if lives <= 0:
        running = False
#quiting
pygame.quit()
