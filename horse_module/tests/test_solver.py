from ..solver import *
import pytest


def test_correct_creature_of_counter_and_position():
    assert add_values_for_test() == (1, [])


testbase = [('1', (3, 2)), ('2', (3, 2)), ('3', (3, 2))]


@pytest.mark.parametrize('num_3, result', testbase)
def test_count_3(num_3, result):
    assert solve('D6', 'A2', num_3) == result


def test_correct_values_knight_move():
    assert knight_move((4, 6), 'A2') == 3


def test_correct_values_knights_collision():
    assert knights_collision((4, 6), (1, 2)) == 2


def test_correct_data():
    add_values_for_test()
    assert move(4, 6) == ['43', '52', '45', '56', '76', '85', '83', '72']


def test_research():
    add_values_for_test()
    assert research((4, 6)) == ['C4', 'E4', 'B5', 'F5', 'B7', 'F7', 'C8', 'E8']
