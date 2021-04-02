class GameOver(Exception):


    def __init__(self, name, score_player):
        """class constructor """
        self.name = name
        self.score_player = score_player
        self.write_score(self.name, score_player)

    @staticmethod
    def write_score(name, score_player):
        """writing points to a file """
        with open('scores.txt', 'a+') as files:
            files.write(name + " score: " + str(score_player) + '\n')


class EnemyDown(Exception):
    """functionality is not important"""
    print("----------------------------------")
