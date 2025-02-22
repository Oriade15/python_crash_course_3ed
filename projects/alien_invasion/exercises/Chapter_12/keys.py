import sys

import pygame


class Game:
    """ Game class """

    def __init__(self):
        """  """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Keys")

    def run(self):
        """  """
        print("\nPrinting pressed keys\n")
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
        # TODO: print key string instead of int
        print(f" • {event.key}")
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill((255, 255, 255))

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
