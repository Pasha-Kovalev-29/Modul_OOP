from random import randint
from exceptions import EnemyDown
from settings import LIVES_PLAYER

class Enemy:
    level=1
    lives=level

    def __init__(self, level):
        self.level=level
        self.lives=level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        try:
            """decreases lives
            if lives <0 causes EnemyDown"""
            pass
        except:
            raise EnemyDown


class Player:
    lives=LIVES_PLAYER
    score=0
    def __init__(self, name, allowed_attacks):
        self.name=name

    @staticmethod
    def fight(attack, defense):
        """возвращает результат раунда - 0 если ничья, -1 если атака неуспешна, 1 если атака успешна"""
        pass

    def decrease_lives(self):
        try:
            """decreases lives
            if lives <0 causes EnemyDown"""
            pass
        except:
            raise EnemyDown

    def attack(self, enemy_obj):
        """выбирает атаку противника из объекта enemy_obj; вызывает метод fight();
         Если результат боя 0 - вывести "It's a draw!", если 1 = "You attacked successfully!"
          и уменьшает количество жизней противника на 1, если -1 = "You missed!"""фвв"
        pass

    def defence(self, enemy_obj):
        """то же самое, что и метод attack(), только в метод fight первым передается атака противника,
         и при удачной атаке противника вызывается метод decrease_lives игрока"""
        pass

# a=Enemy(5)
#
# print(a.__dict__)
# print(a.select_attack())

