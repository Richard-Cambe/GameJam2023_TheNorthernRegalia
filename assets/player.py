import pygame

#créer une classe qui va représenter le joueur:
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load("./src/boredhero.png")
        self.rect = self.image.get_rect()
        self.rect.x = 118
        self.rect.y = 515


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity