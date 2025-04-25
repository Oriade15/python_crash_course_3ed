class Settings:
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's static settings. """
        # Screen settings
        self.screen_width = 960
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, difficulty_level="beginner"):
        """ Initialize settings that change throughout the game. """
        # fleet_direction of 1 represents right; -1 represents left 
        # (Like an enumerated constant).
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

        # Use the selected difficulty level to set dynamic attributes
        if difficulty_level == "beginner":
            self.ship_speed = 1.5
            self.bullet_speed = 2.5
            self.alien_speed = 1.0
            self.difficulty_level = difficulty_level 
        elif difficulty_level == "intermediate":
            self.ship_speed = 2.0
            self.bullet_speed = 3.0
            self.alien_speed = 1.5
            self.difficulty_level = difficulty_level 
        elif difficulty_level == "pro":
            self.ship_speed = 2.5
            self.bullet_speed = 3.5
            self.alien_speed = 2.0 
            self.difficulty_level = difficulty_level 

        # TODO: Show Difficulty level on game screen

    def increase_speed(self):
        """ Increase speed settings and alien point values. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
