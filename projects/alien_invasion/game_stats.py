import json
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """ Initialize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.load_high_score()

    def load_high_score(self):
        """ Load high score from json file """
        self.high_score_filepath = Path('high_score.json')
        if self.high_score_filepath.exists():
            self.high_score = json.loads(self.high_score_filepath.read_text())
        else:
            self.high_score = 0

    def save_high_score(self):
        """ Save high score to json file """
        self.high_score_filepath.write_text(json.dumps(self.high_score))

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
