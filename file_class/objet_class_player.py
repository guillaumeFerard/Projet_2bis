import pygame

# ! créer une classe pour mes champ select
class Object_class_player:

    def __init__(self, path, x, y, width, height, player = False):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player


    def lauch_player(self):
        return self.player
