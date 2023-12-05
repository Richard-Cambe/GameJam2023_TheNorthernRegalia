import pygame
from game import Game

pygame.init()


pygame.display.set_caption("The Northern Regalia")
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


#importer, modifier et charger la bannière
banner = pygame.image.load('./src/gamepic.jpg')
banner = pygame.transform.scale(banner , (600,400))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4
banner_rect.y = screen.get_height() / 6

#importer, modifier et charger un bouton "commencer"
play_button = pygame.image.load('./src/button_startv2.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 4
play_button_rect.y = screen.get_height() / 6


#tant que cette condition est vraie:
while running:
    #appliquer la fenetre du jeu
    print(x_background)
    if x_background == -9372:
        x_background += 0
    else:
        if game.player.rect.x >= 750:
            x_background -= 1
    
    screen.blit(background, (x_background,0))
    
    #vérifier si le jeu a commencé ou non
    if game.is_playing:
        #déclencher les instructions de partie
        game.update(screen)
    else:
        #ajouter ecran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(play_button, (0,0))

    #appliquer le sprite du joueur sur la fenetre du jeu
    screen.blit(game.player.image , game.player.rect)
    for player in game.all_players:
        player.forward()
        player.update_health_bar(screen)
        

    #vérifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 750:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    game.all_monsters.draw(screen)
    
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
 
    #afficher le compteur de score
    font = pygame.font.SysFont("vivaldi", 30)
    score_text = font.render(f"{game.score}", 1, (0, 0, 0))
    score_bg = pygame.image.load("./src/gold_counter.png")
    screen.blit(score_bg, (45, 625))
    screen.blit(score_text, (160, 640))

    #mettre a jour l'écrand
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
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True