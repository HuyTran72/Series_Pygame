import pygame

pygame.init() # initialize all module pygame
screen = pygame.display.set_mode((800,400)) #initialize module height, width
pygame.display.set.caption("Covid Fighting")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("game/graphics/300.png")
while True:
    # create exit button
    for even in pygame.even.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))        
    pygame.display.update()
    clock.tick(60)