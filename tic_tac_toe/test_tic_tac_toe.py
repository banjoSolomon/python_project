import unittest

from tic_tac_toe.tic_tac_toes import MyTicTacToes, TickTackToeValues


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = MyTicTacToes()

    def test_the_game_is_empty(self):
        for row in range(3):
            for col in range(3):
                self.assertEqual(TickTackToeValues.EMPTY, self.game.get_board()[row][col])

    def test_two_players_can_play_the_game(self):
        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())
        self.game.make_move(0, 0)
        self.assertEqual(TickTackToeValues.O, self.game.get_current_player())

    def test_for_valid_move(self):
        self.assertEqual(TickTackToeValues.EMPTY, self.game.get_board()[0][0])
        self.game.make_move(0, 0)
        self.assertEqual(TickTackToeValues.X, self.game.get_board()[0][0])
        self.assertEqual(TickTackToeValues.O, self.game.get_current_player())

    def test_game_progres(self):
        self.assertEqual(TickTackToeValues.EMPTY, self.game.get_board()[0][0])
        self.game.make_move(0, 0)
        self.assertEqual(TickTackToeValues.X, self.game.get_board()[0][0])
        self.game.make_move(1, 1)

        self.assertEqual(TickTackToeValues.O, self.game.get_board()[1][1])
        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())
        self.game.make_move(0, 1)

        self.assertEqual(TickTackToeValues.X, self.game.get_board()[0][1])
        self.assertEqual(TickTackToeValues.O, self.game.get_current_player())

    def test_winning_condition(self):
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        self.game.make_move(0, 1)
        self.game.make_move(1, 2)
        self.game.make_move(0, 2)
        self.assertTrue(TickTackToeValues.X, self.game.get_winner())

    def test_for_draw(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(0, 2)
        self.game.make_move(0, 2)
        self.game.make_move(1, 0)
        self.game.make_move(1, 1)
        self.game.make_move(1, 2)
        self.game.make_move(2, 0)
        self.game.make_move(2, 1)
        self.game.make_move(2, 2)
        self.assertTrue(self.game.draw())

    def test_game_after_move(self):
        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())
        self.assertEqual(TickTackToeValues.EMPTY, self.game.get_board()[0][0])
        self.game.make_move(0, 0)
        self.assertEqual(TickTackToeValues.O, self.game.get_current_player())
        self.assertEqual(TickTackToeValues.X, self.game.get_board()[0][0])
        self.game.make_move(1, 1)

        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())

        self.assertEqual(TickTackToeValues.O, self.game.get_board()[1][1])

    def test_switching_players(self):
        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())
        self.game.make_move(0, 0)
        self.assertEqual(TickTackToeValues.O, self.game.get_current_player())
        self.game.make_move(1, 1)
        self.assertEqual(TickTackToeValues.X, self.game.get_current_player())
