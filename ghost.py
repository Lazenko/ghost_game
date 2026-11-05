import pygame


class Ghost:
    """A class to manage the ghost."""

    def __init__(self, ghost_game):
        """Initialize the ghost and set its starting position."""
        self.screen = ghost_game.screen
        self.screen_rect = ghost_game.screen.get_rect()

        self.image = pygame.image.load("images/ghost.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ghost at its current location."""
        self.screen.blit(self.image, self.rect)
