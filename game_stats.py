class GameStats():
    """Отслеживание статистики"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Создаем флаг чтобы игра запускалась в неактивном состоянии
        self.game_active = False

        # Рекорд не сбрасывается
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
