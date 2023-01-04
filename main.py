import pygame
import sqlite3
def create_table(таблица счета):
    # Здесь name - название таблицы
    # Создаем запрос на создание таблицы, если таковой еще не существует
    que_create = '''
        CREATE TABLE IF NOT EXISTS ''' + name + '''(
            id INTEGER PRIMARY KEY,
            name TEXT,
            score TEXT
        )
    '''

    # С помощью курсора выполняем запрос
    cur.execute(que_create)
    # Сохраняем изменения в базе данных
    database.commit()

# Функция получения данных
def get_data(table_name, column):
    # Здесь column - поля таблицы, которые хотим получить(столбцы)
    # table_name - имя таблицы, из которой хотим получить данные
    # Создаем запрос на получение данных
    que_select = '''
        SELECT ''' + column + ''' FROM ''' + table_name + '''
    '''

    # Получаем результат
    result = cur.execute(que_select)
    # Получаем все строки из результата
    data = result.fetchall()
    # Возвращаем полученные строки
    return data

# Функция занесения данных в таблицу
def insert_data(table_name, column, values):
    # Здесь table_name - название таблицы, в которую хотите занести данные
    # column - поля(столбцы) в которые хотите занести данные
    # value - сами данные
    # Создаем запрос на внесение данных в таблицу
    que_insert = '''
            INSERT INTO ''' + table_name + ''' (''' + column + ''') VALUES (''' + values + ''') 
        '''

    # С помощью курсора выполняем запрос
    cur.execute(que_insert)
    # Сохраняем изменения в базе данных
    database.commit()


# Создаем подключение в базе данных
database = sqlite3.connect('game.sqlite')

# Создаем курсор, который дальше будет общаться с базой
cur = database.cursor()

# Вызываем функцию создания таблицы с названием 'scores'
create_table('scores')

# Вносим в таблицу с названием 'scores' данные
# Обратите внимание, что вторым аргументом вводятся поля(колонки/столбцы), в которые вы хотите внести данные. Вводятся они через запятую и через пробел
# Третьим аргументом идут сами данные. Обратите внимание, что здесь стоят двойные кавычки("")
# Чтобы ввести текстовые данные, необходимо поставить еще и одинарные кавычкы, иначе работать НЕ БУДЕТ
insert_data('scores', 'name, score', "'', 10")


print(get_data('scores', 'name, score'))

database.close()
class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('png-clipart-graphics-basketball-backboard-sport-cartoon.png')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images.jfif')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5


class Enem(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images.jfif')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0


class DatabaseObject:
    def create_table(self):
        pass

    def insert_data(self):
        pass

    def get_data(self, table_name):
        pass


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

enemy.rect.left = 200

all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

enemy_sprites.add(enemy)

all_sprites.add(ball)
enemy_sprites.add(ball)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hits = pygame.sprite.spritecollide(ball, enemy_sprites, True)

    win.fill((255, 255, 255))
    x, y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        print("бросок")

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
    all_sprites.update()
    enemy_sprites.update()
    # all_sprites.draw(win)
    # enemy_sprites.draw(win)
    pygame.display.update()
