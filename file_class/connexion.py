# coding : utf-8
import pygame
from file_class.object_menu import Object_menu
from file_class.sql_request import SQL_request
from file_class.game import Game

class Connexion:

    def __init__(self, width_screen, height_screen):


        self.background = pygame.image.load('assets/bg2.jpg')
        self.background = pygame.transform.scale(self.background, (width_screen, height_screen))
        self.background = self.background.convert()

        self.list_home_object = []
        self.list_home_object.append(Object_menu('assets/input_ko.PNG', 450, 380, 700, 70))
        self.list_home_object.append(Object_menu('assets/input_ko.PNG', 450, 550, 700, 70))
        self.list_home_object.append(Object_menu('assets/label_user.PNG', 450, 300, 200, 60))
        self.list_home_object.append(Object_menu('assets/label_pass.PNG', 425, 450, 300, 100))
        self.list_home_object.append(Object_menu('assets/submit.png', 650, 680, 300, 70))
        self.list_home_object.append(Object_menu('assets/logo.png', 550, 20, 500, 250))

        
        self.input_font = pygame.font.Font(None, 50)
        self.text_font = pygame.font.Font(None, 50)
        self.mail_user = ""
        self.mail_user_blit = self.input_font.render(self.mail_user, 1, (0, 0, 0))
        self.password_user = ""
        self.password_user_hash = ""
        self.password_user_blit = self.input_font.render(self.password_user_hash, 1, (0, 0, 0))
        self.error_message = "Identifiant ou mot de passe inconnu"
        self.error_message_blit = self.text_font.render(self.error_message, 1, (0, 0, 0))

        # ? var qui determine si l'user a test de ce log et a échouer
        self.login_false = False


    def update(self, screen):

        screen.blit(self.background, (0,0))
        for bloc in self.list_home_object:
            screen.blit(bloc.image, bloc.rect)
            screen.blit(self.mail_user_blit, (490,397))
            screen.blit(self.password_user_blit, (490,575))

        if self.login_false:
            screen.blit(self.error_message_blit, (0, 0))


    def write_mail_user(self, letter):
        self.mail_user = f"{self.mail_user}{letter}"
        self.mail_user_blit = self.input_font.render(self.mail_user, 1, (0, 0, 0))


    def write_password_user(self, letter):
        self.password_user = f"{self.password_user}{letter}"
        self.password_user_hash = "*" * len(self.password_user)
        self.password_user_blit = self.input_font.render(self.password_user_hash, 1, (0, 0, 0))


    def return_mail_user(self):
        if self.list_home_object[0].can_write:
            self.mail_user = self.mail_user[:-1]
            self.mail_user_blit = self.input_font.render(self.mail_user, 1, (0, 0, 0))


    def return_password_user(self):
        if self.list_home_object[1].can_write:
            self.password_user = self.password_user[:-1]
            self.password_user_hash = "*" * len(self.password_user)
            self.password_user_blit = self.input_font.render(self.password_user_hash, 1, (0, 0, 0))


    def test_login(self, sql_object):
        self.email_check = sql_object.check_email(self.mail_user)
        self.password_check = sql_object.check_password(self.password_user)
        if self.email_check and self.password_check:
            self.user_playing = sql_object.get_user_id(self.mail_user)