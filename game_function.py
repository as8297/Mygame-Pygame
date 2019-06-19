import sys,pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, alien_ship, bullets) :
    ''' This checks actions and responds to the mouse and  keyboard input '''
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            key_press(event,ai_settings,screen,ship,alien_ship,bullets)
        elif event.type == pygame.KEYUP :
            key_unpress(event,ship)

# function to check wether any key is pressed
def key_press(event,ai_settings,screen,ship,alien_ship,bullets):
    """Respond to keypresses """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
# function to check if any key is unpressed
def key_unpress(event,ship):
    """Respond to key release """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 

def update_screen(ai_settings,screen,ship,alien_ship,bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien_ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)