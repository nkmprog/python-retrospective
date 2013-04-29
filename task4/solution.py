class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ',
                      'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.values = ('X', 'O')
        self.last_move = ' '
        self.winner_determined = False
        self.winner = ' '

    def __setitem__(self, key, value):
        if key not in self.board.keys():
            raise InvalidKey('An invalid key has been entered')

        if value not in self.values:
            raise InvalidValue('An invalid value has been entered')

        if self.board[key] != ' ':
            raise InvalidMove('An invalid move has been attempted')

        if value != self.last_move:
            self.board[key] = value
            self.last_move = value
        else:
            raise NotYourTurn('Not your turn')

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return '\n  -------------\n' +\
            '3 | {} | {} | {} |\n'.format(self.board["A3"],
                                          self.board["B3"],
                                          self.board["C3"]) +\
            '  -------------\n' +\
            '2 | {} | {} | {} |\n'.format(self.board["A2"],
                                          self.board["B2"],
                                          self.board["C2"]) +\
            '  -------------\n' +\
            '1 | {} | {} | {} |\n'.format(self.board["A1"],
                                          self.board["B1"],
                                          self.board["C1"]) +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def _check_draw(self):
        for position in self.board.values():
            if position == ' ':
                return False
        return True

    def game_status(self):
        '''Determine the status of the game'''

        winning_combinations = (('A1', 'A2', 'A3'), ('B1', 'B2', 'B3'),
                                ('C1', 'C2', 'C3'), ('A1', 'B1', 'C1'),
                                ('A2', 'B2', 'C2'), ('A3', 'B3', 'C3'),
                                ('A1', 'B2', 'C3'), ('A3', 'B2', 'C1'))

        if not self.winner_determined:
            if self._check_draw():
                return 'Draw!'
            else:
                for winnig_combination in winning_combinations:
                    outcome = [self.board[position]
                               for position in winnig_combination
                               if self.board[position] != ' ']

                    if len(outcome) != 0 and outcome.count(outcome[0]) == 3:
                        self.winner_determined = True
                        self.winner = outcome[0]
                        return ('{} wins!').format(self.winner)
        else:
            return ('{} has already won!').format(self.winner)

        return 'Game in progress.'
