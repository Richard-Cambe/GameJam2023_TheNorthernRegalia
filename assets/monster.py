import pygame
import random

class Monster(pygame.sprite.Sprite) :
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = random.randint(3,5)      
        self.image = pygame.image.load('./src/skeleton.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,7000)
        self.rect.y = 505

    def damageM(self, amount):
        self.health -= amount
        
    def update_health_bar(self, surface):
        #definir une couleur pour la jauge de vie (rouge)
        bar_color = (170, 37, 32)
        #definir la position de la jauge de vie + largeur + epaisseur
        bar_position = [self.rect.x-20, self.rect.y, self.health, 5]
        #dessiner la jauge de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def forwardM(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.health -= self.attack
            if self.health<0:
                self.kill()