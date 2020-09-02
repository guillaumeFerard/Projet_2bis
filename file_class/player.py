#coding : utf-8

import pygame
from file_class.sql_request import SQL_request

#? création classe joueur

class Player:
    
    #? le joueur est instancié au lancement du jeu (écran login) on ne connait donc pas encore les atttributs de celui-ci donc init vide
    def __init__(self, pseudo):

        self.sql_request = SQL_request()

        self.pseudo = pseudo
        self.speed = 25
        

        self.set_avatar(self.sql_request.get_info_player(self.pseudo, "avatar"), self.sql_request.get_info_player(self.pseudo, "orientation"))
        self.set_pos_X(self.sql_request.get_info_player(self.pseudo, "pos_X"))
        self.set_pos_Y(self.sql_request.get_info_player(self.pseudo, "pos_Y"))
        self.set_pv(self.sql_request.get_info_player(self.pseudo, "pv"))

    #? méthodes pour associer les attributs correspondant au joueur loggé
    def set_avatar(self, avatar, orientation):
        avatar = f"{avatar}/{orientation}.png" 
        self.image = pygame.image.load(avatar)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        
        
    def set_pos_X(self, x):
        self.rect.x = x

    def set_pos_Y(self, y):
        self.rect.y = y

    def set_pv(self, pv):
        self.pv = pv