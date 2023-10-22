import pygame

pygame.init() # initialize all module pygame
screen = pygame.display.set_mode((800,400)) #initialize module height, width
pygame.display.set.caption("Covid Fighting")

while True:
    # create exit button
    for even in pygame.even.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            exit()
    
            
    pygame.display.update()