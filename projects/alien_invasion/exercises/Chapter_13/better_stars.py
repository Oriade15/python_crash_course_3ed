import sys

import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    """ Star class """

    def __init__(self, game):
        """ Initialize Star """
        super().__init__()
        self.screen = game.screen

        # Load the image and set rect.
        self.image = pygame.image.load('assets/star.bmp')
        self.rect = self.image.get_rect()

        # Place near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position.
        self.x = float(self.rect.x)


class Game:
    """ Game class """

    def __init__(self):
        """ Initialize Game & its resources """
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (255, 255, 255)

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("Better Stars")

        self.stars = pygame.sprite.Group()

        self._create_star_galaxy()

    def _create_star_galaxy(self):
        """ Create the galaxy of stars. """
        # Create an star and keep adding stars until there's no room left.
        # Spacing between stars is one star width and one star height.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_height - (2 * star_height)):
            while current_x < (self.screen_width - (2 * star_width)):
                # Create star adjusting its positon by a random amount
                self._create_star(
                    randint(current_x-10, current_x+10), 
                    randint(current_y-10, current_y+10))
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """ Create an star and place it in the fleet. """
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        
        new_star.x = x_position

        self.stars.add(new_star)

    def run(self):
        """  """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.screen_bg_color)

        #  draws each star at the position defined by its rect
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
