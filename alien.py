import pygame
from pygame.sprite import Sprite
class Alien():

    def __init__(self,ai_settings,screen):
        super().__init__()
        ''' Initializing the alien_ship and set its starting position '''
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Bloat image and get its rectangle
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        ''' Draw the ship at its current location '''
        self.screen.blit(self.image,self.rect)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True
    
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x     