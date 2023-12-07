import pygame
import random
import animation

class Monster(animation.AnimateSprite) :
    def __init__(self, game):
        super().__init__("skeleton")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = random.randint(3,5)      
        self.image = pygame.image.load('./src/skeleton.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,15000)
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

        #define function to update naimations
    def update_animation(self):
        self.animate()
    
    def forwardM(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.health -= self.attack
            if self.health<0:
                self.kill()
                self.game.score +=1