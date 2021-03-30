from random import randint
from exceptions import EnemyDown, GameOver
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
        self.lives-=1
        print("Enemy have lives: " + str(self.lives))
        if self.lives==0:
            raise EnemyDown



class Player:
    lives=LIVES_PLAYER
    score=0
    def __init__(self, name, allowed_attacks):
        self.name=name

    @staticmethod
    def fight(attack, defense):
        """возвращает результат раунда - 0 если ничья, -1 если атака неуспешна, 1 если атака успешна
        Волшебник-1 побеждает воина-2. Воин-2 побеждает разбойника-3. Разбойник-3 побеждает волшебника-1"""
        if attack==1 and defense == 2:
            return 1
        elif attack==1 and defense ==3:
            return -1
        elif attack == 1 and defense == 1:
            return 0
        elif attack == 2 and defense == 1:
            return -1
        elif attack == 2 and defense == 2:
            return 0
        elif attack == 2 and defense == 3:
            return 1
        elif attack == 3 and defense == 1:
            return 1
        elif attack == 3 and defense == 2:
            return -1
        elif attack == 3 and defense == 3:
            return 0

    def decrease_lives(self):
        self.lives-=1
        print("You have lives: " + str(self.lives))
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        """выбирает атаку противника из объекта enemy_obj; вызывает метод fight();
         Если результат боя 0 - вывести "It's a draw!", если 1 = "You attacked successfully!"
          и уменьшает количество жизней противника на 1, если -1 = "You missed!"""
        player_class = int(input("Choose who to attack : 1-Wizard, 2-Warrior, 3-Rogue. Please enter number: "))
        enemy_class=Enemy.select_attack()
        result= Player.fight(player_class, enemy_class)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            self.score+=1
            print("Score: "+ str(self.score))
            enemy_obj.decrease_lives()
        else:
            print("You missed!")


    def defence(self, enemy_obj):
        """то же самое, что и метод attack(), только в метод fight первым передается атака противника,
         и при удачной атаке противника вызывается метод decrease_lives игрока"""
        player_class = int(input("Choose by whom you defend  : 1-Wizard, 2-Warrior, 3-Rogue. Please enter number: "))
        enemy_class = Enemy.select_attack()
        result = Player.fight(enemy_class, player_class)
        if result == 0:
            print("It's a draw!")
        elif result == 1: #че по цифрам?
            print("You missed!")
            self.decrease_lives()
        else:
            print("You defended yourself!")



