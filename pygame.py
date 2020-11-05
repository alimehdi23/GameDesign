import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
black =[0,0,0]
red = [250,0,0]
screen.fill((0,0,0))
pygame.display.flip()
pygame.display.set_caption("Testing Pygame")
pygame.time.delay(100)
run = True
while run:
    pygame.time.delay(100)
    screen.fill((162,32,69))
    pygame.display.update()
    for event in pygame.get():
        print(event)
        if eve.type == pygame.QUIT:
            run = False

pygame.time.delay(50)
pygame.quit()
