import pygame
from game import Game

pygame.init()


pygame.display.set_caption("Lord Regalius")
screen = pygame.display.set_mode((1080,720))

#ajouter une musique de fond
pygame.mixer.init()
pygame.mixer.music.load("./src/BG_MUSIC.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#importer et charger l'arrière plan
background = pygame.image.load('./src/BG.png')

x_background = 0
#charger le jeu
game = Game()
running = True

#tant que cette condition est vraie:
while running:
    #appliquer la fenetre du jeu
    if x_background == -9372:
        x_background += 0
    else:
        if game.player.rect.x >= 750:
            x_background -= 2
    
    screen.blit(background, (x_background,0))

    #appliquer le sprite du joueur sur la fenetre du jeu
    screen.blit(game.player.image , game.player.rect)
    
    for player in game.all_players:
        player.forwardP()
        player.update_health_bar(screen)
        
    #vérifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 750:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    game.all_monsters.draw(screen)
    
    for monster in game.all_monsters:
        monster.forwardM()
        monster.update_health_bar(screen)
        
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verif si la souris est en collision avec le bouton jouer
            game.is_playing = True