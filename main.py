import pygame

class Man:
    def __init__(self):
        self.width = 150
        self.height = 100
        self.image = pygame.image.load('1648041537_16-kartinkin-net-p-sport-multyashnie-kartinki-17 (1).png')
        self.rect = self.image.get_rect()
    def move_up(self):
        pass
    def move_down(self):
        pass
    def move_left(self):
        pass
    def move_right(self):
        pass
class Enemy:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()



width =1500
height = 800

x = 1500
y = 1000

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
FPS = 60

win = pygame.display.set_mode((width, height))


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill((255, 255, 255))
    x, y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        print("бросок")
    pygame.draw.circle(win, red, (750, 400), 100)
    pygame.draw.circle(win,red, (250,400), 250)
    pygame.draw.circle(win, red, (1250, 400), 250)
    pygame.draw.line(win, black, (750, 0), (750, 1000), 3)
    pygame.display.update()
