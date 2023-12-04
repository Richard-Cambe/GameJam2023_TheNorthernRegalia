import pygame
from player import Player 
from monster import Monster

#créer une classe qui représente le jeu:
class Game:
    
    def __init__ (self):
        #générer le joueur
        self.player = Player()
        self.pressed = {}
        self.is_playing = False
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        
    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
