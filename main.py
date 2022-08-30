from pygame import *
from random import *
# import time
W = 1200
H = 800
FPS = 60

ENEMY_COUNT = 0
#0.Заменить музыку
#1.Сделать возможность создавать противника, который не преследует игрока, а двигаеться в случайную сторону.
#2.Сделать возможность меня кол-во противников с помощью переменной ENEMY_COUNT (Вспоминаем списки).
window = display.set_mode((W, H))
timer = time.Clock()
backgroud = transform.scale(image.load(‘background.jpg’), (W,H))
game_over = transform.scale(image.load(‘game_over.jpg’), (W,H))
game_win = transform.scale(image.load(‘game_win.jpg’), (W,H))
randomEnemies = []
mixer.init()
mixer.music.load(‘background (2).mp3’)
mixer.music.play()

class Sprite():
def __init__(self, model, w, h, x, y):
self.model = transform.scale(image.load(model), (w, h))
self.rect = self.model.get_rect()
self.rect.x = x
self.rect.y = y

def draw(self):
window.blit(self.model, (self.rect.x, self.rect.y))
class Coin(Sprite):
def __init__(self, model, w, h, x, y, speed):
super().__init__(model, w, h, x, y)
class Player(Sprite):
def __init__(self, model, w, h, x, y, speed):
super().__init__(model, w, h, x, y)
self.speed = speed
def move(self):
najatie_knopki = key.get_pressed()

if najatie_knopki[K_UP] and self.rect.y > 0:

self.rect.y -= self.speed
if najatie_knopki[K_DOWN] and self.rect.y < H - self.rect.h:
self.rect.y += self.speed
if najatie_knopki[K_LEFT] and self.rect.x > 0:
self.rect.x -= self.speed
if najatie_knopki[K_RIGHT] and self.rect.x < W - self.rect.w:
self.rect.x += self.speed
def checkCollison(self):
if self.rect.colliderect(enemy.rect) == True:
return True
for e in randomEnemies:
if self.rect.colliderect(e.rect) == True:
return True
return False
def win(self):
if self.rect.colliderect(moneta.rect) == True:
return True
return False
class Enemy(Sprite):
def __init__(self, model, w, h, x, y, speed):
super().__init__(model, w, h, x, y)
self.speed = speed

def chase(self, target):
if target.rect.x > self.rect.x:
self.rect.x += self.speed
else:
self.rect.x -= self.speed
if target.rect.y > self.rect.y:
self.rect.y += self.speed
else:
self.rect.y -= self.speed
def move(self):
direction = randint(0,3)
if direction == 0 and self.rect.y > 0:
for i in range(randint(10, 20)):
self.rect.y -= self.speed
if direction == 1 and self.rect.y < H - self.rect.h:
for i in range(randint(10, 20)):
self.rect.y += self.speed
if direction == 2 and self.rect.x > 0:
for i in range(randint(10, 20)):
self.rect.x -= self.speed
if direction == 3 and self.rect.x < W - self.rect.w:
for i in range(randint(10, 20)):
self.rect.x += self.speed
myPlayer = Player(‘player.png’, 50, 60, 0, 0, 5)
enemy = Enemy(‘enemy.png’, 50, 60, 400, 300, 2)
moneta = Coin(‘монета.png’, 230, 120, 500, 500, 1)
for i in range(ENEMY_COUNT):
newEnemy = Enemy(‘enemy.png’, 50, 70, randint(0, W), randint(0, H), 3)
randomEnemies.append(newEnemy)
isWin = False
isGame = True #Остановка движения
run = True #Остановка всей игры целиком!
while run:
display.update()

for e in event.get():
if e.type == QUIT:
run = False
myPlayer.move()
if myPlayer.checkCollison() == True:
isGame = False
isWin = False
if myPlayer.win() == True:
isGame = False
isWin = True
enemy.chase(myPlayer)
for e in randomEnemies:
e.move()
#—————————————————

if isGame == True:



window.fill((0, 0, 0))
window.blit(backgroud, (0, 0))
myPlayer.draw()
enemy.draw()
moneta.draw()
for e in randomEnemies:
e.draw()
else:
if isWin == False:
window.blit(game_over, (0, 0))
else:
window.blit(game_win, (0, 0))
timer.tick(FPS)