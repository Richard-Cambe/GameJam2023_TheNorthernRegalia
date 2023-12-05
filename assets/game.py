import pygame
import random
from player import Player 
from monster import Monster

#créer une classe qui représente le jeu:
class Game:
    
    def __init__ (self):
        self.is_playing = False
        #générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.monster = Monster(self)   
        nbmonstre = random.randint(50,100)
        for i in range (nbmonstre):
            self.spawn_monster()
        self.pressed = {}   
        #initialiser le score
        self.score = 0
        
            
    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    