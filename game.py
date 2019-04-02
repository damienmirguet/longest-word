import random
import string

MAX_LETTERS = 9

class Game(object):
    """docstring for Game"""


    def __init__(self):
        super(Game, self).__init__()
        self.grid = [random.choice(string.ascii_letters[1:26]).upper() for i in range(MAX_LETTERS)]

#    def _genGrid(self):
#        return [random.choice(string.ascii_letters[1:26]).upper() for i in range(MAX_LETTERS)]


#    if __name__ == '__main__':
#        self.grid=_genGrid()

    def is_valid(self, word, grid):
        if not word:
            return False
        list_word = list(word)
        for i in range(len(word)):
            try:
                grid.remove(list_word[i])
            except ValueError as e:
                return False

        return True
