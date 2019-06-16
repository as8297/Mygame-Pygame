import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from bolt import Bolt

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
    ship = Ship(ai_settings,screen)

    # Make a bolt
    bolt = Bolt(screen)


    #start with main loop
    while True:

        # Using GameFuntion to check if game is exited
        #gf.check_events()

        # Tracking the ship movement
        gf.check_events(ship)
        ship.update()

        # Screen Update Function
        gf.update_screen(ai_settings,screen,ship,bolt)
        
run_game()