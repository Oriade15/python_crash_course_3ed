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

        # Track number of times hit
        self.hit_count = 0

        self.hit_limit = 3

        # Movement flags; start with a shooter that's not moving.
        self.is_moving_down = False
        self.is_moving_up = False

    def set_position(self):
        """ Set position  on the screen """
        # Place at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the exact vertical position.
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
        """ Draw the shooter at its current location. """
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


class Bug(Sprite):
    """ Bug class """

    def __init__(self, game):
        """ Inintialize Bug """
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.crawl_speed = 0.5
        self.jump_speed = 4.0

        # Load image and set its rect attribute.
        self.image = pygame.image.load('assets/sideways_bug.bmp')
        self.rect = self.image.get_rect()

        # Place near the top right of the screen.
        self.rect.x = self.screen.get_rect().width - (2 * self.rect.width)
        self.rect.y = self.rect.height

        # Store exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Track number of times hit
        self.hit_count = 0

    def check_horizontal_edges(self):
        """ Return True if at horizontal edge of screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= 0) or (self.rect.bottom >= screen_rect.bottom)

    def update(self):
        """ Crawl the up or down. """
        self.crawl_vertical()

    def crawl_vertical(self):
        """ Crawl vertically """
        self.y += self.crawl_speed * self.game.swarm_direction
        self.rect.y = self.y

    def jump_horizontal(self):
        """ Jump horizontally. """
        self.x -= self.jump_speed
        self.rect.x = self.x


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
        pygame.display.set_caption("Game Over")

        self.shooter = SidewaysShooter(self)

        self.bullets = pygame.sprite.Group()

        self.bugs = pygame.sprite.Group()

        # swarm_direction of -1 represents up; 1 represents down.
        self.swarm_direction = -1

        self._create_swarm()

        # Start game in active state
        self.is_game_active = True

    def _create_swarm(self):
        """ Create the swarm of bugs. """
        # Create a bug and keep adding bugs until there's no room left.
        # Spacing between bugs is one bug width and one bug height.
        bug = Bug(self)
        bug_width, bug_height = bug.rect.size

        current_x, current_y = (
            self.screen_width - (2 * bug_width)), bug_height
        while current_x >= (10 * bug_width) and current_x <= (self.screen_width - 2 * bug_width):
            while current_y >= bug_height and current_y <= (self.screen_height - 2 * bug_height):
                self._create_bug(current_x, current_y)
                current_y += 2 * bug_height

            # Finished a row; decrement x value, and reset y value.
            current_x -= 2 * bug_width
            current_y = bug_height

    def _create_bug(self, x_position, y_position):
        """ Create a bug and place it in the swarm. """
        new_bug = Bug(self)
        new_bug.rect.x = x_position
        new_bug.rect.y = y_position

        new_bug.x = x_position
        new_bug.y = y_position

        self.bugs.add(new_bug)

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

                #  update bugs
                self._update_bugs()

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

        self._check_bullet_bug_collisions()

    def _check_bullet_bug_collisions(self):
        """ Respond to bullet-bug collisions. """
        # Remove any bullets and bugs that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.bugs, True, True)

        if not self.bugs:
            # Destroy existing bullets and create new swarm.
            self.bullets.empty()
            self._create_swarm()

    def _update_bugs(self):
        """ Check if the swarm is at an horizontal edge, then update positions. """
        self._check_swarm_horizontal_edges()
        self.bugs.update()

        # Look for bug-shooter collisions.
        hit_bug = pygame.sprite.spritecollideany(self.shooter, self.bugs)
        if hit_bug:
            hit_bug.hit_count += 1
            self.shooter.hit_count += 1
            self._bug_hit_shooter()

    def _bug_hit_shooter(self):
        """Respond to the shooter being hit by an bug."""
        if self.shooter.hit_count < self.shooter.hit_limit:
            # Get rid of any remaining bullets and bugs.
            self.bullets.empty()
            self.bugs.empty()

            # Create a new swarm and repositon the shooter.
            self._create_swarm()
            self.shooter.set_position()

            # Pause.
            sleep(0.5)
        else:
            self.is_game_active = False

    def _check_swarm_horizontal_edges(self):
        """ Respond appropriately if any bugs have reached an horizontal edge. """
        for bug in self.bugs.sprites():
            if bug.check_horizontal_edges():
                self._jump_swarm_horizontal()

                #  change swarm direction
                self.swarm_direction *= -1
                break

    def _jump_swarm_horizontal(self):
        """ Cause the entire swarm to jump horizontally. """
        for bug in self.bugs.sprites():
            bug.jump_horizontal()

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.screen_bg_color)

        # We place this loop before the line that draws the shooter,
        # so the bullets don’t start out on top of the shooter.
        for bullet in self.bullets.sprites():
            bullet.draw_self()

        self.shooter.draw_self()

        #  draws each bug at the position defined by its rect
        self.bugs.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
