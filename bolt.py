import pygame

class Bolt():

    def __init__(self,screen):
        ''' Initializing the Bolt and set its starting position '''
        self.screen = screen

        # Load the Bloat image and get its rectangle
        self.image = pygame.image.load('images/Bolt.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # starting each bolt at top+center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        ''' Draw the ship at its current location '''
        self.screen.blit(self.image,self.rect)
        