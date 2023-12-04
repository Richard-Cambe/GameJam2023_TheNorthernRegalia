import pygame
pygame.init()

pygame.display.set_caption("The Northern Regalia")
screen = pygame.display.set_mode((1080,1500))

background = pygame.image.load('Hackathon/GameJam2023_TheNorthernRegalia/assets/BG.png')
running = True

while running:
    screen.blit(background, (0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
