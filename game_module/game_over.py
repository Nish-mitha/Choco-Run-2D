import pygame
from sys import *
import pymysql
import main_menu
from pygame import mixer
# initialize pygame
pygame.init()

# Create window
over_screen = pygame.display.set_mode((1534, 800))
over_screen.fill((255, 255, 255))

pygame.display.set_caption('Candy Run')
icon=pygame.image.load('assets/images/character/run_move_4.png')
pygame.display.set_icon(icon)

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


def redraw(player_name,value,score):
    over_screen.fill((230, 16, 55))
    if score >= value:
        font = pygame.font.Font('freesansbold.ttf', 40)
        hscore = font.render("HIGHEST SCORE :   " + str(value), True, (0, 255, 0))
        over_screen.blit(hscore, (630, 650))
    else:
        font = pygame.font.Font('freesansbold.ttf', 30)
        s = font.render("SCORE :  " + str(score), True, (0, 0, 0))
        over_screen.blit(s, (670, 650))

    avatar=pygame.image.load('assets/images/user.png')
    over_screen.blit(avatar,(690,530))
    font = pygame.font.Font('freesansbold.ttf', 30)
    pname = font.render(player_name, True, (0, 0, 0))
    over_screen.blit(pname, (750, 530))
    font = pygame.font.Font('freesansbold.ttf', 100)
    name = font.render("GAME OVER!!!",True, (0, 0, 0))
    over_screen.blit(name,(420,200))
    restart.draw(over_screen, (255, 255, 255))
    logout.draw(over_screen,(255,255,255))

def over(player_name,score):
    over = True
    high_value=0
    # Database
    db = pymysql.connect("localhost", "user", "password10", "choco_run", 3306)
    # prepare a cursor object using cursor() method

    cursor = db.cursor()
    sql = "INSERT INTO player(Player_name,score)  VALUES ('%s', '%d')" % (
        player_name, score)
    max_score = "SELECT MAX(score) FROM player WHERE Player_name ='%s'" % (player_name)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        cursor.execute(max_score)
        value = cursor.fetchall()
        high_value=value[0][0]
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    while over:
        redraw(player_name,high_value,score)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Login button event
                if restart.isAbove(pos):
                    btn9 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn9.play()
                    main_menu.start_menu(player_name)
                if logout.isAbove(pos):
                    btn10 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn10.play()
                    over=False
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEMOTION:
                #start hover
                if restart.isAbove(pos):
                    restart.color = (0, 255, 0)
                else:
                    restart.color = (71, 105, 73)
                # logout hover
                if logout.isAbove(pos):
                    logout.color = (255, 0, 0)
                else:
                    logout.color = (71, 105, 73)
                # logout hover

            if event.type == pygame.QUIT:
                over= False
                pygame.quit()
                exit()


restart=button((71, 105, 73),500,380,200,50,'MENU')
logout=button((71,105,73),850,380,200,50,'EXIT')
pygame.display.update()
