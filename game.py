from models import Player, Enemy

def play():
    name_player=input('Please enter name: ')
    start=input('Please enter START: ')
    if start == 'START':
        # player_class=input("Choose who you play: 1-Wizard, 2-Warrior, 3-Rogue. Please enter number: ")
        player = Player(name=name_player, allowed_attacks=None)  # что то надо ввести в алловед атакс
        level_enemy = 1
        enemy = Enemy(level_enemy)
        while True:
            player.attack(enemy)
            player.defence(enemy)
    else:
        print('ERROR')

    player=Player(name=name_player,allowed_attacks=None) #что то надо ввести в алловед атакс
    level_enemy=1
    enemy=Enemy(level_enemy)
    player.attack(enemy)
    player.defence(enemy)

if __name__ == '__main__':
    try:
        play()

    except:
        """обрабатывает два исключения:
         GameOver - выводит сообщение об ошибке, записывает результат в таблицу рекордов.
          KeyboardInterrupt - pass"""



