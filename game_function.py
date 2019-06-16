import sys,pygame

def check_events(ship) :
    ''' This checks actions and responds to the mouse and  keyboard input '''
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                # move the ship to Right
                ship.moving_right = True
            if event.key == pygame.K_LEFT :
                # move the ship to Left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
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