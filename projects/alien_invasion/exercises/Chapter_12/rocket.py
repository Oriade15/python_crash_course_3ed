import sys

import pygame


class Rocket:
    """ Rocket class """

    def __init__(self, game):
        """ Initialize """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the rocket's image and get its rect.
        self.image = pygame.image.load('assets/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        self.speed = 1.5

        # Store a float for the rocket's exact horizontal &  position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def draw(self):
        """ Draw at current positon """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update positon """
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # Update rect object from self.x & self.y.
        self.rect.x = self.x
        self.rect.y = self.y


class Game:
    """ Game class """

    def __init__(self):
        """ Initialize Game """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run(self):
        """ Start game main loop """
        while True:
            self._check_events()

            self.rocket.update()

            self._update_screen()

    def _check_events(self):
        """  """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _update_screen(self):
        """  """
        self.screen.fill((255, 255, 255))

        self.rocket.draw()

        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
