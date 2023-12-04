import pygame
from game import Game
pygame.init()

pygame.display.set_caption("The Northern Regalia")
screen = pygame.display.set_mode((1080,720))

#importer et charger l'arrière plan
background = pygame.image.load('C:/Users/richa/OneDrive/Bureau/GAMEJAM/GameJam2023_TheNorthernRegalia/src/BG.png')

#charger le jeu
game = Game()
running = True

#tant que cette condition est vraie:
while running:
    #appliquer la fenetre du jeu
    screen.blit(background, (0,0))

    #appliquer le sprite du joueur sur la fenetre du jeu
    screen.blit(game.player.image , game.player.rect)

    #vérifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 750:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre a jour l'écran
    pygame.display.flip()

    #si l'utilisateur ferme la fenetre du jeu:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()         
        #detecter si le joueur lache une touche 
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False