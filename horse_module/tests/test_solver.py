from ..solver import *


def test_correct_values_knight_move():
    assert knight_move((4, 6), 'A2') == 3
