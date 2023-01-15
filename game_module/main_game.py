from pygame import mixer
import pygame
from sys import *
import register_form
import login_form

# initialize pygame
pygame.init()

# Create window
main_screen = pygame.display.set_mode((1534, 800))

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


def redraw():
    main_screen.fill((255, 255, 255))
    main_bg = pygame.image.load('assets/images/main_background.png')
    main_screen.blit(main_bg, (0, 45))
    choco.draw(main_screen,(0,0,0))
    login_button.draw(main_screen, (255, 255, 255))
    register_button.draw(main_screen,(255,255,255))

def main_menu():

    menu = True
    while menu:
        redraw()
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Login button event
                if login_button.isAbove(pos):
                    btn1 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn1.play()
                    login_form.login()
                if register_button.isAbove(pos):
                    btn2 = mixer.Sound('assets/music/button_sound.wav')  # Bullet sound
                    btn2.play()
                    register_form.register()
            if event.type == pygame.MOUSEMOTION:
                #Login hover
                if login_button.isAbove(pos):
                    login_button.color = (0, 255, 0)
                else:
                    login_button.color = (71, 105, 73)
                 #Register hover
                if register_button.isAbove(pos):
                    register_button.color = (0, 255, 0)
                else:
                    register_button.color = (71, 105, 73)
                if choco.isAbove(pos):
                    choco.color = (0, 255, 0)
                else:
                    choco.color = (120, 4, 4)

            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                exit()

login_button = button((71, 105, 73), 200, 730, 200, 50, 'LOGIN')
choco=button((120, 4, 4),650,5,200,25,"CANDY RUN")
register_button = button((71, 105, 73), 1100, 730, 200, 50, 'REGISTER')
main_menu()
pygame.display.update()
