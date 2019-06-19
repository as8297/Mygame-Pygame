import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
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

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings=ai_settings,screen=screen,aliens=aliens)

    #start with main loop
    while True:

        # Using GameFuntion to check if game is exited
        #gf.check_events()

        # Tracking the elements movement
        gf.check_events(ai_settings=ai_settings,screen=screen,ship=ship,bullets=bullets)
        ship.update()

        bullets.update()

        # Get rid of bullets that have disappeared.
        gf.update_bullets(bullets)

        # Screen Update Function
        gf.update_screen(ai_settings=ai_settings,screen=screen,ship=ship,aliens=aliens,bullets=bullets)
        
run_game()