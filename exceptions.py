
class GameOver(Exception):
    """mechanism for saving the final result """
    def __init__(self, name, score_player):
        self.name=name
        self.score_player=score_player
        self.write_score(self.name, score_player)

    def write_score(self, name, score_player):
        with open('scores.txt', 'a+') as fp:
            fp.write(name + " score: " + str(score_player) + '\n')



class EnemyDown(Exception):
    """functionality is not important"""
    pass
