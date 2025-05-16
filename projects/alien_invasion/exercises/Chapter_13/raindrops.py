import sys

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """ Raindrop class """

    def __init__(self, game):
        """ Initialize Raindrop """
        super().__init__()
        self.screen = game.screen

        self.speed = 0.5

        # Load the image and set rect.
        self.image = pygame.image.load('assets/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Place near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position.
        self.y = float(self.rect.y)

    def update(self):
        """ Move down the screen. """
        self.y += self.speed
        self.rect.y = self.y


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
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_raindrop_grid()

    def _create_raindrop_grid(self):
        """ Create the grid of raindrops. """
        # Create an raindrop and keep adding raindrops until there's no room left.
        # Spacing between raindrops is one raindrop width and one raindrop height.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.screen_height - (2 * raindrop_height)):
            while current_x < (self.screen_width - (2 * raindrop_width)):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width

            # Finished a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _create_raindrop(self, x_position, y_position):
        """ Create an raindrop and place it in the grid. """
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position

        new_raindrop.y = y_position

        self.raindrops.add(new_raindrop)

    def run(self):
        """  """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            #  update raindrops
            self._update_raindrops()

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

    def _update_raindrops(self):
        """ Update Raindrop poistions """
        self.raindrops.update()

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.screen_bg_color)

        #  draws each raindrop at the position defined by its rect
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
