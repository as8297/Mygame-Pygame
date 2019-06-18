class Settings():
    # This is a class for all the settings related to the game
    def __init__(self):
        ''' Initialize the games's settings '''
        
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (250,250,250)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5