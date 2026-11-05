import sys

import pygame

from ghost import Ghost
from settings import Settings


class GhostGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Ghost")

        self.ghost = Ghost(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ghost.blitme()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    gg = GhostGame()
    gg.run_game()
