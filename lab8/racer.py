import pygame
import random

pygame.init()
run = True

window_size = (400, 600)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Racing Pro")
clock = pygame.time.Clock()
fps = 24

grass = pygame.Color(126, 200, 80)
barder = pygame.Color(255, 255, 255)

display2 = pygame.Surface((450, 600))
display2.fill(barder)
icon = pygame.image.load(r"racerelements\car.png")
pygame.display.set_icon(icon)

background = pygame.image.load(r"racerelements\background.png")
car = pygame.image.load(r"racerelements\car.png")
pickup = pygame.image.load(r"racerelements\pickup_truck.png")
taxi = pygame.image.load(r"racerelements\taxi.png")
van = pygame.image.load(r"racerelements\van.png")

car_radius = 20
speed = 20
car_pos = [250, 400]

class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > window_size[1]:
            self.reset_position()

    def reset_position(self):
        self.rect.y = 0
        self.rect.x = random.choice([150, 350])

def check_collision(car, all_cars):
    for other_car in all_cars:
        if car != other_car and car.rect.colliderect(other_car.rect):
            return True
    return False

def draw_background(pos1, pos2):
    screen.blit(background, pos1)
    screen.blit(background, pos2)

pickup_truck = Car(pickup, random.choice([150, 350]), 0, 7)
while check_collision(pickup_truck, [pickup_truck]):
    pickup_truck.reset_position()

taxi_car = Car(taxi, random.choice([150, 350]), -200, 7)
while check_collision(taxi_car, [pickup_truck, taxi_car]):
    taxi_car.reset_position()

van_car = Car(van, random.choice([150, 350]), -400, 7)
while check_collision(van_car, [pickup_truck, taxi_car, van_car]):
    van_car.reset_position()

all_cars = pygame.sprite.Group()
all_cars.add(pickup_truck, taxi_car, van_car)

background_pos1 = [100, 0]
background_pos2 = [100, -600]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_pos[0] = max(car_pos[0] - speed, car_radius + 70)
    if keys[pygame.K_RIGHT]:
        car_pos[0] = min(car_pos[0] + speed, window_size[0] - car_radius + 40)

    all_cars.update()

    background_pos1[1] += speed
    background_pos2[1] += speed

    if background_pos1[1] >= 600:
        background_pos1[1] = -600
    if background_pos2[1] >= 600:
        background_pos2[1] = -600

    screen.fill(grass)
    screen.blit(display2, (75, 0))
    draw_background(background_pos1, background_pos2)
    screen.blit(car, tuple(car_pos))
    all_cars.draw(screen)

    clock.tick(fps)
    pygame.display.update()