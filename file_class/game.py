# coding : utf-8

import pygame
from file_class.player import Player
from file_class.objet_class_player import Object_class_player
from file_class.sql_request import SQL_request

# ! créer une classe game


class Game:

    def __init__(self, width_screen, height_screen):
        """
            initialisation de la classe game en argument on a besoin de longueur et hauteur de l'écran
        """
        # ! definir si le jeu a commencer ou pas
        self.game_launch = False
        self.player_select = False
        self.background = pygame.image.load('assets/bg.png')
        self.background = pygame.transform.scale(
            self.background, (width_screen, height_screen))

        # ! instance de la classe sql
        self.sql_request = SQL_request()

        # ! def des font pour les name
        self.name_font = pygame.font.Font(None, 50)

    # ! method update pour mettre a jour a chaque frame de tour, on met screen en argument pour faire les éventul blit
    def update(self, screen):
        if self.player_select:
            self.update_game(screen)
        else:
            self.update_champ_select(screen)

    # ! method pour launch la champ select
    def start(self, user):
        self.game_launch = True

        # ! j'affiche les logos
        self.logo_info = []

        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/pseudo.png", 450, 50, 40, 40))
        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/pseudo.png", 1050, 50, 40, 40))

        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/pv.png", 450, 120, 40, 40))
        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/pv.png", 1050, 120, 40, 40))

        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/map.png", 450, 180, 40, 40))
        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/map.png", 1050, 180, 40, 40))

        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/classe.png", 450, 250, 40, 40))
        self.logo_info.append(Object_class_player(
            "assets/avatar/avatar_in_menu/classe.png", 1050, 250, 40, 40))

        #! je créer les boutons play
        self.button_play = []

        self.button_play.append(Object_class_player("assets/avatar/avatar_in_menu/play.png", 500, 300, 200, 100, self.sql_request.get_player_data(
            user)[0][2]))
        self.button_play.append(Object_class_player("assets/avatar/avatar_in_menu/play.png", 1050, 300, 200, 100, self.sql_request.get_player_data(
            user)[1][2]))

        # ! je recupere les classes
        self.champ = self.sql_request.get_class_choice(user)
        self.champ_obj = []
        self.champ_obj.append(Object_class_player(
            self.champ[0][0], 50, 50, 400, 800))
        self.champ_obj.append(Object_class_player(
            self.champ[0][1], 650, 50, 400, 800))

        self.class_name_blit = []
        self.class_name_blit.append(
            self.name_font.render(self.champ[1][0], 1, (0, 0, 0)))
        self.class_name_blit.append(
            self.name_font.render(self.champ[1][1], 1, (0, 0, 0)))

        # ! je recupere les noms des players
        self.name_player = [self.sql_request.get_player_data(
            user)[0][2], self.sql_request.get_player_data(user)[1][2]]
        self.name_player_blit = []
        self.name_player_blit.append(
            self.name_font.render(self.name_player[0], 1, (0, 0, 0)))
        self.name_player_blit.append(
            self.name_font.render(self.name_player[1], 1, (0, 0, 0)))

        # ! je recupere les pv
        self.pv_player = [self.sql_request.get_player_data(
            user)[0][8], self.sql_request.get_player_data(user)[1][8]]

        # ! je recupere les map sur lesquels sont les player
        self.map_name = [self.sql_request.get_player_data(
            user)[0][12], self.sql_request.get_player_data(user)[1][12]]
        self.map_name_blit = []
        self.map_name_blit.append(
            self.name_font.render(self.map_name[0], 1, (0, 0, 0)))
        self.map_name_blit.append(
            self.name_font.render(self.map_name[1], 1, (0, 0, 0)))

    def update_champ_select(self, screen):
        for icone in self.logo_info:
            screen.blit(icone.image, icone.rect)

        for champ in self.champ_obj:
            screen.blit(champ.image, champ.rect)

        for button in self.button_play:
            screen.blit(button.image, button.rect)

        screen.blit(self.name_player_blit[0], (500, 50))
        screen.blit(self.name_player_blit[1], (1100, 50))

        screen.blit(self.map_name_blit[0], (500, 180))
        screen.blit(self.map_name_blit[1], (1100, 180))

        screen.blit(self.class_name_blit[0], (500, 250))
        screen.blit(self.class_name_blit[1], (1100, 250))

        # ! dessin des pv
        # dessin barre grise
        pygame.draw.rect(screen, (50, 50, 50), (500, 120, 200, 25))
        pygame.draw.rect(screen, (50, 50, 50), (1100, 120, 200, 25))
        # dessin barre rouge
        self.pv_player_blit = [pygame.draw.rect(screen, (250, 0, 0), (500, 120, self.pv_player[0] * 2, 25)), pygame.draw.rect(
            screen, (250, 0, 0), (1100, 120, self.pv_player[1] * 2, 25))]

    def update_game(self, screen):
        # ! print les section

        # map
        pygame.draw.rect(screen, (130, 198, 101), (50, 50, 1200, 675))
        # heure
        pygame.draw.rect(screen, (129, 143, 199), (1300, 50, 250, 100))
        # stat
        pygame.draw.rect(screen, (240, 236, 103), (1300, 200, 250, 350))
        # joueur
        pygame.draw.rect(screen, (159, 87, 162), (1300, 600, 250, 250))
        # button 1
        pygame.draw.rect(screen, (238, 56, 58), (50, 775, 200, 75))
        # button 2
        pygame.draw.rect(screen, (115, 26, 25), (300, 775, 200, 75))
        # button 3
        pygame.draw.rect(screen, (242, 129, 129), (550, 775, 200, 75))
        # button 4
        pygame.draw.rect(screen, (115, 62, 61), (800, 775, 200, 75))
        # button 5
        pygame.draw.rect(screen, (192, 44, 44), (1050, 775, 200, 75))


        screen.blit(self.player.image, self.player.rect)


        # blit des hp
        # dessin logo pv
        
        # dessin barre grise
        pygame.draw.rect(screen, (50, 50, 50), (1375, 250, 150, 20))
        # dessin barre rouge
        pygame.draw.rect(screen, (250, 0, 0), (1375, 250, self.player.pv * 1.5, 20))

    def lauch_player_choice(self, pseudo):
        self.player_select = True
        self.player = Player(pseudo)
