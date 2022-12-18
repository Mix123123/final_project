import pygame

class Man:
    def __init__(self):
        self.width = 150
        self.height = 100
        self.image = pygame.image.load(''
                                       )
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



width = 1500
height = 800

x = 1000
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
    pygame.draw.line(win, red, (500, 0), (500, 1000), 4)
    pygame.display.update()

