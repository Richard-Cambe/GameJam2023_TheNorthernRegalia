import pygame

class Monster(pygame.sprite.Sprite) :

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load('Hackathon/GameJam2023_TheNorthernRegalia/src/KnightIdle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 559
        self.velocity = 2
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity