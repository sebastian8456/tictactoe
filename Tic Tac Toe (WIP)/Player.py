# Player.py
# Class to represent the human player

class Player():
    def __init__(self, number):
        self.player = self.player_input(number)

    def player_input(self, number):
        marker = ''
        while marker not in['X','O']:
            marker = input(f'Player {number}, choose a marker X/O: ').upper()
        return marker
    