from models import Player, Enemy
from exceptions import GameOver, EnemyDown


def play():
    name_player=input('Please enter name: ')
    start=input('Please enter START: ')
    if start == 'START':

        player = Player(name=name_player, allowed_attacks=None)  # что то надо ввести в алловед атакс
        try:
            level_game=1
            enemy = Enemy(level_game)

            def start_game():
                while True:
                    player.attack(enemy)
                    player.defence(enemy)
            start_game()

        except EnemyDown:
            player.score+=5
            print(player.score)
            level_game+=1
            print(level_game)
            enemy = Enemy(level_game)
            start_game()



    else:
        print('ERROR')

if __name__ == '__main__':
    try:
        play()

    except GameOver:
        print("GameOver")

    except KeyboardInterrupt:
        pass
        """обрабатывает два исключения:
         GameOver - выводит сообщение об ошибке, записывает результат в таблицу рекордов.
          KeyboardInterrupt - pass"""

    finally:
        print('Good bye')



