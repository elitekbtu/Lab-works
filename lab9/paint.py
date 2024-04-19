import pygame

pygame.init()

painting = []

timer = pygame.time.Clock()

fps = 60

activeColor = (0, 0, 0)
activeShape = 0

w = 800
h = 600

screen = pygame.display.set_mode([w, h])

pygame.display.set_caption("Paint")


def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100])
    pygame.draw.line(screen, 'black', [0, 100], [w, 100])
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)
    triangle = [pygame.draw.rect(screen, 'black', [200, 10, 80, 80]), 2]
    pygame.draw.polygon(screen, "white", ((240, 30),(240 - 30, 80),(240 + 30, 80)))
    rhomb = [pygame.draw.rect(screen, 'black', [300, 10, 80, 80]), 3]
    pygame.draw.polygon(screen, "white", ((340, 50-30), (340+30, 50), (340, 50+30), (340-30, 50)))
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)]
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)]
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)]
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)]
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)]
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)]
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)]
    return [blue, red, green, yellow, black, purple, eraser], [rect, circ, triangle, rhomb]


def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        if paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])
        if paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-15, paint[1][1]+15), (paint[1][0], paint[1][1]-15), (paint[1][0]+15, paint[1][1]+15)))
        if paint[2] == 3:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0], paint[1][1]-15), (paint[1][0]+15, paint[1][1]), (paint[1][0], paint[1][1]+15), (paint[1][0]-15, paint[1][1])))


def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)
        if activeShape == 2:
            pygame.draw.polygon(screen, activeColor, ((mouse[0]-15, mouse[1]+15), (mouse[0], mouse[1]-15), (mouse[0]+15, mouse[1]+15)))
        if activeShape == 3:
            pygame.draw.polygon(screen, activeColor, ((mouse[0], mouse[1]-15), (mouse[0]+15, mouse[1]), (mouse[0], mouse[1]+15), (mouse[0]-15, mouse[1])))


run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    colors, shapes = drawDisplay()

    mouse = pygame.mouse.get_pos()
    draw()
     
    click = pygame.mouse.get_pressed()[0]
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape))
    drawPaint(painting)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shapes:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]

     
    pygame.display.flip()

pygame.quit()
