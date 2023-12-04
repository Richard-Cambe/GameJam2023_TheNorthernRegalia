import pygame

class Monster(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load('Hackathon/GameJam2023_TheNorthernRegalia/assets/KnightIdle.png')
        self.rect = self.image.get_rect()