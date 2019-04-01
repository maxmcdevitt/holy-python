import pygame.font
from pygame.sprite import Group
from knight import Knight
from user import Bow        
import os


class Scoreboard(object):

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        cwd =os.getcwd()
        self.knight = Knight(cwd)
        self.bow = Bow(screen)
        # Font settings for scoring information.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.screen_rect = self.screen.get_rect()
        self.screen_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_health(self):
        """Draw score to the screen."""
        self.hi = self.font.render(str(self.knight.health) ,True, self.text_color, (250,250,250))
        self.score_rect = self.hi.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        self.screen.blit(self.hi, self.score_rect)
        #        self.screen.blit(self.stats[1], (1300, 600))