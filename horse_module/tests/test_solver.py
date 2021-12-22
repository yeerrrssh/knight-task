from ..solver import *


def test_correct_values_knight_move():
    assert knight_move((4, 6), 'A2') == 3


def test_correct_values_knights_collision():
    assert knights_collision((4, 6), (1, 2)) == 2