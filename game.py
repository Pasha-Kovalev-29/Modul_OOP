from models import Player

def play():
    name_player=input('Please enter name: ')
    player=Player(name=name_player,allowed_attacks=None) #что то надо ввести в алловед атакс

if __name__ == '__main__':
    try:
        play()

    except:
        """обрабатывает два исключения:
         GameOver - выводит сообщение об ошибке, записывает результат в таблицу рекордов.
          KeyboardInterrupt - pass"""



