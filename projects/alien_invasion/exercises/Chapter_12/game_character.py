import sys

import pygame


class GameCharacter:
    """ Game character class """

    def __init__(self, game):
        """  """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the character's image and get its rect.
        self.image = pygame.image.load('assets/game_character.bmp')
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center
        
    def draw(self):
        """  """
        self.screen.blit(self.image, self.rect)


class Game:
    """ Game class """

    def __init__(self):
        """  """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")

        self.character = GameCharacter(self)

    def run(self):
        """  """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((255, 255, 255))

            self.character.draw()

            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()

