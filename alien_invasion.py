import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from alien_ship import Alien_ship
from pygame.sprite import Group

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

    # Make a group to store bullets in.
    bullets = Group()

    # Make a alien_ship
    alien_ship = Alien_ship(screen)


    #start with main loop
    while True:

        # Using GameFuntion to check if game is exited
        #gf.check_events()

        # Tracking the elements movement
        gf.check_events(ai_settings,screen,ship,alien_ship,bullets)
        ship.update()

        bullets.update()

        # Get rid of bullets that have disappeared.
        gf.update_bullets(bullets)

        # Screen Update Function
        gf.update_screen(ai_settings,screen,ship,alien_ship,bullets)
        
run_game()