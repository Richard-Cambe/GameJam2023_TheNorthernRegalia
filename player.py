import pygame

#créer une classe qui va représenter le joueur:
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.health = 50
        self.max_health = 50
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load('src/KnightIdle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 559

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity