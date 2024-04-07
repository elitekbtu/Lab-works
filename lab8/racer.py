import pygame
import random
import time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
gameicon = pygame.image.load(r"racerelements\car.png")
pygame.display.set_icon(gameicon)

clock = pygame.time.Clock()
fps = 24
background = pygame.image.load(r"racerelements\background.png")

width = 400
height = 600

speed = 5
score = 0
scorecoin = 0
generateplaces = [(120, 0), (280, 0)]
x = random.randint(0,1)

font1 = pygame.font.SysFont('calibri', 30, True)
font2 = pygame.font.SysFont('calibri', 40)

gameover = font2.render("Game Over", True, (0, 0, 255))

class Racer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"racerelements\car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (170, 500)

    def move(self, x):
        prsdkeys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if prsdkeys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < width:
            if prsdkeys[K_RIGHT]:
                self.rect.move_ip(7, 0)

class Cars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"racerelements\taxi.png")
        self.rect = self.image.get_rect()
        self.rect.center = generateplaces[x]

    def move(self,x):
        global speed
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.center = generateplaces[x]

class Coins(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        global generateplaces
        self.image = pygame.image.load("racerelements\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(generateplaces)

    def move(self):
        global coin, scorecoin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            scorecoin += 1
            self.rect.center = random.choice(generateplaces)


    def move(self, x):
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            if  x<1:
                self.rect.center = generateplaces[1]
            else:
                self.rect.center = generateplaces[0]
            

racer = Racer()
cars = Cars()
coin = Coins()
enemies = pygame.sprite.Group()
enemies.add(cars)
prize = pygame.sprite.Group()
prize.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(racer)
all_sprites.add(cars)
all_sprites.add(coin)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    scores = font1.render(str(scorecoin), True, (0, 0, 255))
    screen.blit(scores, (10, 10))
    x = random.randint(0,1)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move(x)

    if pygame.sprite.spritecollideany(racer, prize):
        for entity in prize:
            entity.rect.y = -80
        scorecoin += 1

    if pygame.sprite.spritecollideany(racer, enemies):
        pygame.mixer.Sound(r'racerelements\crash.mp3').play()
        time.sleep(0.5)

        screen.fill((255, 255, 255))
        screen.blit(gameover, (100, 250))
        screen.blit(scores, (180, 200))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(4)
        pygame.quit()
        exit() 

    pygame.display.update()
    clock.tick(fps)
