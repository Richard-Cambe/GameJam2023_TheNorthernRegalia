import pygame
from game import Game
pygame.init()

pygame.display.set_caption("The Northern Regalia")

screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('Hackathon/GameJam2023_TheNorthernRegalia/src/BG.png')
game = Game()
running = True

while running:
    screen.blit(background, (0,0))
    game.all_monsters.draw(screen)
    
    for monster in game.all_monsters:
        monster.forward()
        
    pygame.display.flip()
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
