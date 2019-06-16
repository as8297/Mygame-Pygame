import sys,pygame

def check_events(ship) :
    ''' This checks actions and responds to the mouse and  keyboard input '''
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            key_press(event,ship)
        elif event.type == pygame.KEYUP :
            key_unpress(event,ship)

# function to check wether any key is pressed
def key_press(event,ship):
    """Respond to keypresses """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

# function to check if any key is unpressed
def key_unpress(event,ship):
    """Respond to key release """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 

def update_screen(ai_settings,screen,ship,bolt):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    bolt.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()