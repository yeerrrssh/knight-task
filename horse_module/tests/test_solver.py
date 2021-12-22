from ..solver import *


def test_correct_creature_of_counter_and_position():
    assert add_values_for_test() == (1, [])


def test_count_3():
    assert solve('D6', 'A2', '3') == (3, 2)


def test_count_1():
    assert solve('D6', 'A2', '1') == (3, 2)


def test_count_2():
    assert solve('D6', 'A2', '2') == (3, 2)


def test_correct_values_knight_move():
    assert knight_move((4, 6), 'A2') == 3


def test_correct_values_knights_collision():
    assert knights_collision((4, 6), (1, 2)) == 2
