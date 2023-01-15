import pygame
from sys import *
import play_game
import pymysql
from tkinter import *
from pygame import mixer
# initialize pygame
pygame.init()

# Create window
main_screen = pygame.display.set_mode((1534, 800))
main_screen.fill((255, 255, 255))
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


def redraw(player_name):
    #main_bg = pygame.image.load('Images/start.jpg')
    #main_screen.blit(main_bg, (0, 0))
    main_screen.fill((171, 194, 112))
    avatar=pygame.image.load('assets/images/user.png')
    main_screen.blit(avatar,(10,15))
    font = pygame.font.Font('freesansbold.ttf', 40)
    name = font.render("    "+player_name,True, (0, 0, 0))
    main_screen.blit(name,(24,15))
    start.draw(main_screen, (255, 255, 255))
    score.draw(main_screen,(255,255,255))
    m.draw(main_screen, (255, 255, 255))
    logout.draw(main_screen,(255,255,255))

def start_menu(player_name):

    menu = True
    value=0
    db = pymysql.connect("localhost", "user", "password10", "choco_run", 3306)
    # prepare a cursor object using cursor() method

    cursor = db.cursor()
    score_list = "SELECT score FROM player WHERE Player_name ='%s'" % (player_name)
    try:
        # Execute the SQL command
        cursor.execute(score_list)
        value = cursor.fetchall()
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    while menu:
        redraw(player_name)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Login button event
                if start.isAbove(pos):
                    pygame.mixer.music.stop()
                    btn3 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn3.play()
                    play_game.play(player_name)

                if score.isAbove(pos):
                    btn4 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn4.play()
                    window = Tk()
                      # Title
                    #window.iconbitmap(r'Images/chocolatei.ico')  # icon here r->raw string

                    def center(root):
                        root.configure(bg='black')
                        # position the window to center
                        width = root.winfo_reqwidth()
                        height = root.winfo_reqheight()
                        right = int(root.winfo_screenwidth() / 2 - width / 2)
                        down = int(root.winfo_screenheight() / 2 - height / 2)
                        root.geometry('+{}+{}'.format(right - 100, down - 100))

                    center(window)
                    window.geometry('300x200')
                    window.title('SCORE')
                    message=""
                    for i in range(len(value)):
                        message=message+str(value[i][0])+"\n"
                    label = Label(window, text=message, bg="yellow", fg="black", width=33,anchor=CENTER).place(x=20, y=20)
                    window.mainloop()
                if logout.isAbove(pos):
                    btn5 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn5.play()
                    menu=False
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEMOTION:
                #start hover
                if start.isAbove(pos):
                    start.color = (0, 255, 0)
                else:
                    start.color = (71, 105, 73)
                 #score hover
                if score.isAbove(pos):
                    score.color = (0, 0, 255)
                else:
                    score.color = (71, 105, 73)
                # logout hover
                if logout.isAbove(pos):
                    logout.color = (255, 0, 0)
                else:
                    logout.color = (71, 105, 73)
                if m.isAbove(pos):
                    m.color = (0, 255, 0)
                else:
                    m.color = (230, 16, 55)
                # logout hover

            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                exit()


start=button((71, 105, 73),630,380,200,50,'START')
score = button((71, 105, 73), 1260, 380, 200, 50, 'SCORE')
logout=button((71,105,73),30,380,200,50,'EXIT')
m=button((230, 16, 55),600,30,300,50,'MAIN MENU')
pygame.display.update()
