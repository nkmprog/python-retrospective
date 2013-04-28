class InvalidKey(Exception):
    def __init__(self, message):
        self.message = message


class InvalidValue(Exception):
    def __init__(self, message):
        self.message = message


class InvalidMove(Exception):
    def __init__(self, message):
        self.message = message


class NotYourTurn(Exception):
    def __init__(self, message):
        self.message = message


class TicTacToeBoard:
    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ',
                      'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.values = ('X', 'O')
        self.last_move = ' '
        self.winner_determined = False
        self.winner = ' '

    def __setitem__(self, key, value):
        if key in self.board.keys():
            if value in self.values:
                if self.board[key] == ' ':
                    if value != self.last_move:
                        self.board[key] = value
                        self.last_move = value
                    else:
                        raise NotYourTurn('Not your turn')
                else:
                    raise InvalidMove('An invalid move has been attempted')
            else:
                raise InvalidValue('An invalid value has been entered')
        else:
            raise InvalidKey('An invalid key has been entered')

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return '\n  -------------\n' +\
            '3 |   |   |   |\n' +\
            '  -------------\n' +\
            '2 |   |   |   |\n' +\
            '  -------------\n' +\
            '1 |   |   |   |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def check_draw(self):
        for position in self.board.values():
            if position == ' ':
                return False
        return True

    def game_status(self):
        '''Determine the status of the game'''

        winning_combinations = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'],
                                ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'],
                                ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
                                ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']]

        if not self.winner_determined:
            if self.check_draw():
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
            ('{} wins!').format(self.winner)

        return 'Game in progress.'
