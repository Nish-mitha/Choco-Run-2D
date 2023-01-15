import pygame, sys
from pygame.locals import *
import random
import math
import game_over
from pygame import mixer

pygame.init()

# Background Music

screen = pygame.display.set_mode((1534, 800))
pygame.display.set_caption('Candy Run')
icon = pygame.image.load('assets/images/character/run_move_4.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
bg = pygame.image.load('assets/images/game_background.png').convert()

bgOne_x = 0

# Score
textX = 1350
textY = 15
score_value = 0
# hero
walkRight = [pygame.image.load('assets/images/character/run_move_1.png'), pygame.image.load('assets/images/character/run_move_2.png'),
             pygame.image.load('assets/images/character/run_move_3.png'), pygame.image.load('assets/images/character/run_move_4.png'),
             pygame.image.load('assets/images/character/run_move_5.png'), pygame.image.load('assets/images/character/run_move_6.png'),
             pygame.image.load('assets/images/character/run_move_7.png'), pygame.image.load('assets/images/character/run_move_8.png'),
             pygame.image.load('assets/images/character/run_move_9.png'), pygame.image.load('assets/images/character/run_move_10.png')]
char = pygame.image.load('assets/images/character/stand.png')
slide = pygame.image.load('assets/images/character/slide.png')
die = pygame.image.load('assets/images/character/die.png')
heroX = 50
heroY = 435
heroX_change = 0
heroY_change = 440
done = pygame.image.load('assets/images/chocolate/choco_one.png')

# Choco
choco = []
chocoX = []
chocoY = []
chocoX_change = []
chocoY_change = []
num_of_choco = 3
for i in range(num_of_choco):
    choco.append(pygame.image.load('assets/images/chocolate/choco_two.png'))
    chocoX.append(random.randint(10, 1500))
    chocoY.append(random.randint(350, 480))
    chocoX_change.append(10)
    chocoY_change.append(0)

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 1
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/images/crow.png'))
    enemyX.append(1550)
    enemyY.append(random.randint(380, 480))
    enemyX_change.append(10)
    enemyY_change.append(0)

#delay function
def delay(x):
    for i in range(0,x):
        for j in range(0,i*1000):
            pass

# function to display enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# function to display enemy
def choco_fn(x, y, i):
    screen.blit(choco[i], (x, y))


# function to check collision with enemy
def isCollision_enemy(enemyX, enemyY, heroX, heroY):
    distance = math.sqrt((math.pow(enemyX - heroX, 2)) + (math.pow(enemyY - heroY, 2)))
    if distance < 30:
        return True
    else:
        return False


# function to check collision with enemy
def isCollision_choco(chocoX, chocoY, heroX, heroY):
    distance = math.sqrt((math.pow(chocoX - heroX, 2)) + (math.pow(chocoY - heroY, 2)))
    if distance < 50:
        return True
    else:
        return False


# Button class
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, main_screen, outline=None):
        if outline:
            pygame.draw.rect(main_screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(main_screen, self.color, (self.x, self.y, self.width, self.height))
        if self.text != '':
            font = pygame.font.SysFont('freesansbold.ttf', 30)
            button_text = font.render(self.text, 1, (255, 255, 255))
            main_screen.blit(button_text, (self.x + (self.width // 2 - button_text.get_width() // 2),
                                           self.y + (self.height // 2 - button_text.get_height() // 2)))

    def isAbove(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def redraw(player_name):
    avatar = pygame.image.load('assets/images/user.png')
    screen.blit(avatar, (10, 10))
    font1 = pygame.font.Font('freesansbold.ttf', 30)
    name = font1.render("    " + player_name, True, (255, 255, 255))
    screen.blit(name, (24, 15))
    play_button.draw(screen, (255, 255, 255))
    pause_button.draw(screen, (255, 255, 255))
    menu_button.draw(screen, (255, 255, 255))


def play(player_name):
    mixer.music.load('assets/music/main_music.mp3')
    mixer.music.play(-1)

    global bgOne_x, heroX_change, heroX, heroY_change, heroY, score_value
    heroY = 435
    heroX = 100
    heroX_change = 0
    heroY_change = 0
    bgOne_x = 0
    bg_change = 0
    Right = False
    walkCount = 0
    sleep = False
    down = False
    over = False
    score_value = 0
    win = True
    up = True
    d = True
    right = True

    def show_score(x, y):
        font = pygame.font.Font('freesansbold.ttf', 30)
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    while win:
        screen.fill((0, 0, 0))
        redraw(player_name)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                win = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and up:
                    jp = mixer.Sound('assets/music/jump.wav')  # Bullet sound
                    jp.play()
                    heroY -= 70
                    clock.tick(100)
                    Right = False
                    down = False
                if event.key == pygame.K_DOWN and d:
                    fall = mixer.Sound('assets/music/slide.wav')  # Bullet sound
                    fall.play()
                    down = True
                if event.key == pygame.K_RIGHT and right:
                    heroX_change = 0.5
                    bg_change = 2
                    Right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_DOWN:
                    heroX_change = 0
                    bg_change = 0
                    Right = False
                    down = False
                if event.key == pygame.K_UP:
                    heroY += 70

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Login button event
                if play_button.isAbove(pos):
                    btn6 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn6.play()
                    pygame.time.delay(0)
                if pause_button.isAbove(pos):
                    btn7 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn7.play()
                    pygame.time.delay(1000000)
                if menu_button.isAbove(pos):
                    btn8 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn8.play()
                    win = False
            if event.type == pygame.MOUSEMOTION:
                # Login hover
                if play_button.isAbove(pos):
                    play_button.color = (0, 255, 0)
                else:
                    play_button.color = (71, 105, 73)
                # Register hover
                if pause_button.isAbove(pos):
                    pause_button.color = (0, 255, 0)
                else:
                    pause_button.color = (71, 105, 73)
                if menu_button.isAbove(pos):
                    menu_button.color = (0, 255, 0)
                else:
                    menu_button.color = (71, 105, 73)

        heroX += heroX_change
        if heroX > 1530:
            heroX = 0
        if heroX < 0:
            heroX = 1530

        # Background Scrolling
        ref_x = bgOne_x % bg.get_rect().width
        bgOne_x -= bg_change
        screen.blit(bg, (ref_x - bg.get_rect().width, 65))
        if ref_x < 1534:
            screen.blit(bg, (ref_x, 65))

        for j in range(num_of_enemies):
            Collision_shoot = isCollision_enemy(enemyX[j], enemyY[j], heroX, heroY)
            if Collision_shoot:
                over = True

        for j in range(num_of_choco):
            Collision_choco = isCollision_choco(chocoX[j], chocoY[j], heroX, heroY)
            if Collision_choco:
                co = mixer.Sound('assets/music/collect.wav')  # Bullet sound
                co.play()
                score_value += 5
                chocoX[j] = random.randint(0, 1500)
                chocoY[j] = random.randint(400, 480)

        # character movement
        if walkCount + 1 >= 27:
            walkCount = 0
        if Right:
            screen.blit(walkRight[walkCount // 3], (heroX, heroY))
            walkCount += 1
        elif down:
            screen.blit(slide, (heroX, 500))
        elif over:
            pygame.mixer.music.stop()
            screen.blit(die, (heroX, 480))
            up = d = right = False
            go = mixer.Sound('assets/music/over.wav')  # Bullet sound
            go.play()
            sleep = True
        else:
            screen.blit(char, (heroX, heroY))
            walkCount = 0

        for j in range(num_of_enemies):
            if over:
                enemyX[j] = 5000
            else:
                enemyX[j] -= enemyX_change[j]
                if enemyX[j] < -500:
                    enemyX[j] = 1550
                enemy(enemyX[j], enemyY[j], j)

        for j in range(num_of_choco):
            if chocoX[j] < -5:
                chocoX[j] = 10
            choco_fn(chocoX[j], chocoY[j], j)

        show_score(textX, textY)
        if sleep:
            screen.blit(done, (heroX, heroY))
            game_over.over(player_name, score_value)
        pygame.display.update()
        clock.tick(50)


play_button = button((255, 255, 255), 20, 743, 130, 40, 'PLAY')
pause_button = button((255, 255, 255), 650, 743, 130, 40, 'PAUSE')
menu_button = button((255, 255, 255), 1390, 743, 130, 40, 'MENU')
pygame.display.update()
