class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 0, 0, 0

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 96
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the aline point valeus increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Intialize settings that change throughotu the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3

        self.alien_speed_factor = 1

        # fleet_direction of 1 represent right; -1 represetn left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def get_display(self):
        return self.screen_width, self.screen_height

    def get_bg_color(self):
        return self.bg_color

    def increase_speed(self):
        """Increae speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)