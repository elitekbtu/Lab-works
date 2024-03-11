import pygame
import random 

pygame.init()
run = True


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Racing Pro")
clock = pygame.time.Clock()
fps = 24

grass = pygame.Color(126,200,80)
barder = pygame.Color(255,255,255)

display2 = pygame.Surface((450,600))
display2.fill(barder)
icon = pygame.image.load(r"racerelements\car1.png")
pygame.display.set_icon(icon)

background = pygame.image.load(r"racerelements\background.png")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
    
    screen.fill(grass)
    screen.blit(display2,(75,0))
    screen.blit(background, (100,0))
    
    clock.tick(fps)
    pygame.display.update()
