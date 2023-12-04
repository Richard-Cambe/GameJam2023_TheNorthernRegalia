import pygame

class Sword(pygame.sprite.Sprite) :

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('Hackathon/GameJam2023_TheNorthernRegalia/src/sword.png')
        self.rect = self.image.get_rect()
        self.rect.x = 425
        self.rect.y = 559