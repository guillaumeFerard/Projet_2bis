# ! créer une classe les touches pressées
import pygame
from file_class.object_menu import Object_menu
from file_class.connexion import Connexion

class Keyboard_f:

    def __init__(self):
        # ! créer la librairie de touches
        self.keyboard_code = {113: "a",
                             119: "z",
                             101: "e",
                             114: "r",
                             116: "t",
                             121: "y",
                             117: "u",
                             105: "i",
                             111: "o",
                             112: "p",
                             97: "q",
                             115: "s",
                             100: "d",
                             102: "f",
                             103: "g",
                             104: "h",
                             106: "j",
                             107: "k",
                             108: "l",
                             59: "m",
                             122: "w",
                             120: "x",
                             99: "c",
                             118: "v",
                             98: "b",
                             110: "n",
                             256: 0,
                             257: 1,
                             258: 2,
                             259: 3,
                             260: 4,
                             261: 5,
                             262: 6,
                             263: 7,
                             264: 8,
                             265: 9,
                             48: "@",
                             44: ".",
                             266: "."}

    def key_pressed(self, keyboard):
        # ! si la touche est dans le dictionnaire je retourne sa valeur sinon je retourne ?
        if keyboard in self.keyboard_code:
            return self.keyboard_code[keyboard]

        else:
            return ""

    def tab_enter(self, keyboard, list_home_object):
        # ? si on presse la touche entrée ou tab dans le menu login
        self.connexion = Connexion()
        self.list_home_object = self.connexion.list_home_object

        if keyboard in self.keyboard_code == 32:
            list_home_object[0].image = pygame.image.load('assets/input_ko.PNG')
            list_home_object[1].image = pygame.image.load('assets/input_ko.PNG')
            list_home_object[0].can_write = False
            list_home_object[1].can_write = False


