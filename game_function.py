import sys,pygame

def check_events():
    ''' This checks actions and responds to the mouse and  keyboard input '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship,bolt):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    bolt.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()