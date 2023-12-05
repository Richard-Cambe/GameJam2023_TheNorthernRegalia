import pygame
import animation

#créer une classe qui va représenter le joueur:
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("boredhero_sword")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.rect = self.image.get_rect()
        self.rect.x = 118
        self.rect.y = 505
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity
        
    def update_health_bar(self, surface):
        #definir une couleur pour la jauge de vie (rouge)
        bar_color = (111, 210, 46)
        #definir la position de la jauge de vie + largeur + epaisseur
        bar_position = [self.rect.x-20, self.rect.y, self.health, 5]
        #dessiner la jauge de vie
        pygame.draw.rect(surface,(60,63,60),[self.rect.x-20, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, bar_color, bar_position)
        
    def update_animation(self):
        self.animate()

    def forward(self):
        if self.game.check_collision(self, self.game.all_monsters):
            self.game.monster.damage(self.attack)