import pygame

# ! créer une classe pour mes objets du menu
class Object_menu:

    def __init__(self, path, x, y, width, height):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if path == 'assets/input_ko.PNG':
            self.can_write = False
        self.width = width
        self.height = height

    def change_image(self, path):
        if path == 'assets/input_ko.PNG':
            self.can_write = False
        
        if path == 'assets/input_ok.PNG':
            self.can_write = True

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
