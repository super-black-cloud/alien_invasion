import json
from pathlib import Path
# import json
class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        content=ai_game.path.read_text()
        self.high_score=json.loads(content)
    def reset_stats(self):
        """初始化在游戏运行期间可能的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level=1
