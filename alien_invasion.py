import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

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

        # Using GameFuntion to check if game is exited
        gf.check_events()

        # Screen Update Function
        gf.update_screen(ai_settings, screen, ship)
        
run_game()