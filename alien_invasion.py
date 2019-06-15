import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Initialize the game and create a screen object.
    pygame.init()
    
    # Creating an instance of Settings()
    ai_settings=Settings()
    
    # making the SCREEN with the help of SETTINGS() CLASS
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))


    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    #start with main loop
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen with every pass of loop
        screen.fill(ai_settings.bg_color)
        # including the ship in the display
        ship.blitme()

        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()