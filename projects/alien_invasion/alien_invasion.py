import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ Initialize the game, and create game resources. """
        #  initialize game resources
        pygame.init()
        
        # Initialize game clock
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Initialize Display in Fullscreen window mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Initialiize display in Normal Window mode 
        # self.screen = pygame.display.set_mode((self.settings.screen_width, 
        #     self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

        # Difficulty Level Select Buttons (Beginner, Intermediate, Pro).
        self.beginner_button = Button(self, "Beginner", (255, 255, 255), (144, 238, 144), 24)
        self.beginner_button.rect.midleft = self.screen.get_rect().midleft
        self.beginner_button.rect.x += 20
        self.intermediate_button = Button(self, "Intermediate", (0, 0, 0), (255, 193, 37), 24)
        self.intermediate_button.rect.center = self.screen.get_rect().center
        self.pro_button = Button(self, "Pro", (255, 255, 255), (128, 0, 128), 24)
        self.pro_button.rect.midright = self.screen.get_rect().midright
        self.pro_button.rect.x -= 20

        # Track whether user is selecting difficulty level
        self.is_selecting_difficulty_level = False

    def _create_fleet(self):
        """ Create the fleet of aliens. """
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """ Create an alien and place it in the fleet. """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
    
        self.aliens.add(new_alien)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.game_active:
                # Update ship's position
                self.ship.update()
                
                #  update bullets
                self._update_bullets()

                #  update aliens
                self._update_aliens()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

            # Ensure the loop runs 150 times per sec (150 fps)
            self.clock.tick(150)

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._quit_game()
        elif event.key ==  pygame.K_p:
            if not self.game_active:
                self.is_selecting_difficulty_level = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_buttons(self, mouse_pos):
        """ Check whether any of these buttons is selected """
        if self.is_selecting_difficulty_level:
            # Set the appropriate difficulty level for the game
            if self.beginner_button.rect.collidepoint(mouse_pos):
                self.settings.initialize_dynamic_settings("beginner")
                self._start_game()
            elif self.intermediate_button.rect.collidepoint(mouse_pos):
                self.settings.initialize_dynamic_settings("intermediate")
                self._start_game()
            elif self.pro_button.rect.collidepoint(mouse_pos):
                self.settings.initialize_dynamic_settings("pro")
                self._start_game()
        else:
            if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
                # Prompt to select difficulty level
                self.is_selecting_difficulty_level = True

    def _start_game(self):
        """ Start the game. """
        self._reset_game()

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _reset_game(self):
        """ Reset the game statistics. """
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ship_left()
        self.game_active = True
        self.is_selecting_difficulty_level = False

    def _quit_game(self):
        """ Save progress and quit the game. """
        self.stats.save_high_score()
        sys.exit()

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # update the position of the bullets
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        # we use the copy() method to allow us safely modify the bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Respond to bullet-alien collisions. """
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """ Starts a new level """
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()


    def _update_aliens(self):
        """ Check if the fleet is at an edge, then update positions. """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ship_left()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """ Check if any aliens have reached the bottom of the screen. """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """ Respond appropriately if any aliens have reached an edge. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the entire fleet and change the fleet's direction. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)

        # We place this loop before the line that draws the ship,
        # so the bullets don’t start out on top of the ship.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        #  draws each alien at the position defined by its rect
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive 
        # and not selecting difficulty level.
        if not self.game_active:
            if self.is_selecting_difficulty_level:
                self.beginner_button.draw_button()
                self.intermediate_button.draw_button()
                self.pro_button.draw_button()
            else:
                self.play_button.draw_button()


        # Make the most recently drawn screen visible.
        pygame.display.flip()

    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()