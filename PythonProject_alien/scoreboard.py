import json

import pygame.font
from pathlib import Path
# import json
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    """<UNK>"""
    def __init__(self,ai_game):
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats
        self.text_color=(30,30,30)
        self.font = pygame.font.SysFont("comicsans", 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """"将得分渲染为图像"""
        rounded_score=round(self.stats.score,-1)
        score_str=f"{rounded_score:,}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    def prep_high_score(self):
        high_score=round(self.stats.high_score,-1)
        high_score_str=f"{high_score:,}"
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top
    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
    def _check_high_score(self):
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            content = json.dumps(self.stats.high_score)
            content = str(content)
            self.ai_game.path.write_text(content)
            self.prep_high_score()
    def prep_level(self):
        level_str=f"{self.stats.level}"
        self.level_image=self.font.render(level_str,True,self.text_color,self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10
    def prep_ships(self):
        """显示还剩多少飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=30+ship_number * ship.rect.width
            ship.rect.y=5
            self.ships.add(ship)
