import sys
from time import sleep

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

        self.speed = 1.5

        self.set_position()

        # Track target hit & miss
        self.target_hit_count = 0
        self.target_miss_count = 0
        self.target_miss_limit = 3

        # Movement flags; start with a shooter that's not moving.
        self.is_moving_down = False
        self.is_moving_up = False

    def set_position(self):
        """ Set position  on the screen """
        # Start each new shooter at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        self.speed = 1.5

        # Store a float for the shooter's exact vertical position.
        self.y = float(self.rect.y)

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
        """ Draw at current location. """
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """ Bullet class """

    def __init__(self, game):
        """Create a bullet object at the shooter's current position."""
        super().__init__()
        self.screen = game.screen

        # Properties
        self.speed = 2.5
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


class Target():
    """ Target rectangle that moves up an down at a steady rate. """

    def __init__(self, game):
        """  """
        self.screen = game.screen
        self.screen_rect =  game.screen.get_rect()

        # Properties
        self.speed = 0.5
        self.width = 30
        self.height = 50
        self.color = (64, 64, 64)

        # Create rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.set_position()

        # Store position as a float.
        self.y = float(self.rect.y)

        # Movement Direction: 1 for down, -1 for up
        self.movement_direction = 1

    def set_position(self):
        """ Set correct position """
        self.rect.midright = self.screen_rect.midright

    def update(self):
        """Move up & down the screen."""
        self._on_horizontal_edges()

        # Update the exact position of the bullet.
        self.y += self.speed * self.movement_direction

        # Update the rect position.
        self.rect.y = self.y

    def _on_horizontal_edges(self):
        """ Change direction on horizontal edges """
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= self.screen_rect.top:
            self.movement_direction *= -1

    def draw_self(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Button():
    """ Button Class. """

    def __init__(self, game, text) :
        """ Initialize button attributes. """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_text(text)

    def _prep_text(self, text):
        """ Turn text into a rendered image and center text on the button. """
        self.text_image = self.font.render(text, True, self.text_color,
                                          self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button and then draw message. """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)


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
        pygame.display.set_caption("Target Practice")

        self.shooter = SidewaysShooter(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Start Alien Invasion in an inactive state.
        self.is_game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run(self):
        """  """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.is_game_active:
                # Update shooter's position
                self.shooter.update()

                #  update bullets
                self._update_bullets()

                #  update target
                self.target.update()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """ Start a new game when the player clicks Play. """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.is_game_active:
            self._start_game()

    def _start_game(self):
        """ Start the game. """
        # Reset the game statistics.
        self.shooter.target_hit_count = 0
        self.shooter.target_miss_count = 0
        self.is_game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # re-position target & shooter
        self.target.set_position()
        self.shooter.set_position()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # update the position of the bullets
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        # we use the copy() method to allow us safely modify the bullets
        # This also means that the shooter missed the target
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)
                self._on_target_missed()

        self._check_bullet_target_collisions()

    def _check_bullet_target_collisions(self):
        """ Respond to bullet-target collisions. """
        # Look for bullet-target collisions.
        hit_bullet = pygame.sprite.spritecollideany(self.target, self.bullets)
        if hit_bullet:
            self.shooter.target_hit_count += 1
            self.bullets.remove(hit_bullet)

    def _on_target_missed(self):
        """Respond to the target missed."""
        # Increment target miss left.
        self.shooter.target_miss_count += 1

        # Pause.
        sleep(0.3)

        if self.shooter.target_miss_count >= self.shooter.target_miss_limit:
            self.is_game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.screen_bg_color)

        # We place this loop before the line that draws the shooter,
        # so the bullets don’t start out on top of the shooter.
        for bullet in self.bullets.sprites():
            bullet.draw_self()

        self.shooter.draw_self()

        #  draws each bug at the position defined by its rect
        self.target.draw_self()

        # Draw the play button if the game is inactive.
        if not self.is_game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()

