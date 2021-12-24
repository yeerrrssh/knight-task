"""
This module is the entry point
"""

from horse_module.solver import solve


def main():
    """
    Entry point of program
    :return: None
    """
    move = input('Введите номер желаемого действия (1 - от коня до клетки, 2 - встреча двух коней, 3 - обе задачи): ')
    start_position = 'D2'
    final_position = 'D6'
    solve(start_position, final_position, move)


if __name__ == '__main__':
    main()
