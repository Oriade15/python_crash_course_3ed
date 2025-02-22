import sys

import pygame
from pygame.sprite import Sprite


class SidewaysShooter:
    """ SidewayShooter class """

    def __init__(self, game):
        """ Initialize the shooter and set its starting position. """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the shooter image and get its rect.
        self.image = pygame.image.load('assets/sideways_shooter.bmp')
        self.rect = self.image.get_rect()

        # Start each new shooter at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        self.speed = 1.5

        # Store a float for the shooter's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flags; start with a shooter that's not moving.
        self.is_moving_down = False
        self.is_moving_up = False

    def update(self):
        """ Update the shooter's position based on movement flags. """
        # Give both flags the same priority by not using elif statement
        # And allow the shooter to momentarily stop
        # if both up and down keys are pressed

        # Update the shooter's y value, not the rect.
        if self.is_moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.is_moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def draw_self(self):
        """ Draw the shooter at its current location. """
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """ Bullet class """

    def __init__(self, game):
        """Create a bullet object at the shooter's current position."""
        super().__init__()
        self.screen = game.screen

        # Properties
        self.speed = 2.0
        self.width = 15
        self.height = 3
        self.color = (32, 32, 32)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = game.shooter.rect.midright

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.x += self.speed

        # Update the rect position.
        self.rect.x = self.x

    def draw_self(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


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
        pygame.display.set_caption("Sideways Shooter")

        self.shooter = SidewaysShooter(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        """  """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Update shooter's position
            self.shooter.update()

            #  update bullets
            self._update_bullets()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_UP:
            self.shooter.is_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.shooter.is_moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_UP:
            self.shooter.is_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.shooter.is_moving_down = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # update the position of the bullets
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        # we use the copy() method to allow us safely modify the bullets
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.screen_bg_color)

        # We place this loop before the line that draws the shooter,
        # so the bullets don’t start out on top of the shooter.
        for bullet in self.bullets.sprites():
            bullet.draw_self()

        self.shooter.draw_self()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
