import pygame

class Alien_ship():

    def __init__(self,screen):
        ''' Initializing the alien_ship and set its starting position '''
        self.screen = screen

        # Load the Bloat image and get its rectangle
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # starting each alien_ship at top+center of the screen
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top

    def blitme(self):
        ''' Draw the ship at its current location '''
        self.screen.blit(self.image,self.rect)
        