class GameStats():
    """Отслеживание статистики"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Создаем флаг
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit