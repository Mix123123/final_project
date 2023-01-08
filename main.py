import pygame
import sqlite3

import database

def create_table(name):
    # Здесь name - название таблицы
    # Создаем запрос на создание таблицы, если таковой еще не существует
    que_create = '''
        CREATE TABLE IF NOT EXISTS ''' + name + '''(
            id INTEGER PRIMARY KEY,
            score TEXT
        )
    '''


class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.reset.stats


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('png-clipart-graphics-basketball-backboard-sport-cartoon.png')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.left = self.rect.width
        self.rect.top = self.rect.height
        self.rect.left = 700
        self.rect.top = 350
    def update(self):
        self.rect.left += 1
        #self.rect.top += 1


class Stats():
    def __init__(self):
        if ball.rect.left <= 1500:
            self.reset_stats()

    def reset_stats(self):
        self.ball_left = 700


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images.jfif')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.x = 100
        self.rect.y = 325


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 1
        if keys[pygame.K_DOWN]:
            self.rect.top += 1
        if keys[pygame.K_LEFT]:
            self.rect.left -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.left += 1


class Enem(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images (2).jfif')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.left = 1000
        self.rect.top = 325
        self.speed = 10
        self.score = 1
    def update(self):
        if self.rect.top == height:
            self.rect.top = 0
        else:
            self.rect.top += 1





width = 1500
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

all_sprites = pygame.sprite.Group()

ball = Ball()

player = Player()

enemy = Enem()

enemy.rect.left = 1250

create_table('scores')

all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

enemy_sprites.add(enemy)

all_sprites.add(ball)


clock = pygame.time.Clock()


hits = pygame.sprite.spritecollide(ball, enemy_sprites, True)

scores = 0

if game_over:
    database.insert_data('scores', 'name, score', str(scores))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()

    if(ball.rect.left >= 1425 and ball.rect.left <= (1425 + 55)) and (ball.rect.top >= 400 - 55 and ball.rect.top <=(400+ 55)):
        scores += 1
        ball.rect.left = 700
        ball.rect.top = 350
    win.fill((255, 255, 255))
    x, y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        print("1")
    pygame.draw.circle(win, red, (750, 400), 100)
    pygame.draw.circle(win, red, (150, 400), 250)
    pygame.draw.circle(win, red, (1350, 400), 250)
    pygame.draw.circle(win, white, (150, 400), 240)
    pygame.draw.circle(win, white, (1350, 400), 240)
    pygame.draw.circle(win, white, (750, 400), 90)
    pygame.draw.line(win, black, (750, 0), (750, 1000), 3)
    pygame.draw.circle(win, red, (300, 400), 90)
    pygame.draw.circle(win, white, (300, 400), 80)
    pygame.draw.circle(win, red, (1200, 400), 90)
    pygame.draw.circle(win, white, (1200, 400), 80)
    pygame.draw.rect(win, red, (0, 300, 215, 200))
    pygame.draw.rect(win, red, (1285, 300, 215, 200))
    pygame.draw.line(win, black, (50, 0), (50, 100), 3)
    pygame.draw.line(win, black, (150, 325), (0, 325), 3)
    pygame.draw.line(win, black, (150, 475), (0, 475), 3)
    pygame.draw.line(win, black, (150, 475), (150, 325), 3)
    pygame.draw.circle(win, black, (75, 400), 65)
    pygame.draw.circle(win, white, (75, 400), 55)
    pygame.draw.line(win, black, (1350, 325), (1350, 475), 3)
    pygame.draw.line(win, black, (1350, 475), (1500, 475), 3)
    pygame.draw.line(win, black, (1350, 325), (1500, 325), 3)
    pygame.draw.circle(win, black, (1425, 400), 65)
    pygame.draw.circle(win, white, (1425, 400), 55)
    enemy_sprites.update()
    all_sprites.update()
    enemy_sprites.draw(win)
    all_sprites.draw(win)
    pygame.display.update()

