from tic_tac_toe.tick_values import TickTackToeValues


class MyTicTacToes:

    def __init__(self):
        self.board = [[TickTackToeValues.EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = TickTackToeValues.X

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

    def make_move(self, row, col):
        if self.board[row][col] == TickTackToeValues.EMPTY:
            self.board[row][col] = self.current_player
            self.current_player = TickTackToeValues.O if self.current_player == TickTackToeValues.X else TickTackToeValues.X

    def get_winner(self):
        for number in range(3):

            if self.board[number][0] == self.board[number][1] == self.board[number][2] != TickTackToeValues.EMPTY:
                return self.board[number][0]

            if self.board[0][number] == self.board[1][number] == self.board[2][number] != TickTackToeValues.EMPTY:
                return self.board[0][number]

            if self.board[0][0] == self.board[1][1] == self.board[2][2] != TickTackToeValues.EMPTY:
                return self.board[0][0]

            if self.board[0][2] == self.board[1][1] == self.board[2][0] != TickTackToeValues.EMPTY:
                return self.board[0][2]

        return None

    def draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == TickTackToeValues.EMPTY:
                    return False
        else:
            return True
