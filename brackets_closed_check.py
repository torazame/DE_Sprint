### Проверка закрытия скобок

import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()

brackets_open = ('(', '[', '{')
brackets_closed = (')', ']', '}')
bracket_pairs = {br_o: br_cl for br_o, br_cl in zip(brackets_open, brackets_closed)}


# Функция проверки пар скобок по количеству
def bracket_count_check(s):
    '''
    Сравнение количества открывающих и закрывающих скобок.
    Если эти количества различаются, то в строке есть незакрытая скобка.

    Parameters
    ----------
    s : str
        Строка для проверки скобок.

    Returns
    -------
    bool
        True, если количества открывающих и закрывающих скобок не равны. Иначе False.

    '''
    brackets_count = []
    for open_bracket, closed_bracket in bracket_pairs.items():
        open_brackets_cnt = s.count(open_bracket)
        closed_bracket_cnt = s.count(closed_bracket)
        brackets_count.append(open_brackets_cnt != closed_bracket_cnt)
    return any(brackets_count)


# Проверка скобок по расположению в строке
def bracket_index_check(s):
    '''
    Проверка расположения пар скобок.
    Если закрывающая скобка расположена левее открывающей,
    то функция возвращает True. Это сигнализирует о том, что
    в строке есть назакрытая скабка.

    Parameters
    ----------
    s : str
        Строка для проверки расположения скобок.

    Returns
    -------
    bool
        True, если в строке есть закрывающая скобка, росположенная левее своей открывающей пары. Иначе False/
    '''
    bracket_index_dict = defaultdict(list)
    for i, b in enumerate(s):
        bracket_index_dict[b].append(i)

    comparison_results = []
    for open_bracket, closed_bracket in bracket_pairs.items():
        try:
            comparison_results.append(min(bracket_index_dict[open_bracket]) > min(bracket_index_dict[closed_bracket]))
        except ValueError:
            continue
    return any(comparison_results)


# Проверка строки на наличие назакрытых скобок
def check_brackets_closed(s):
    '''
    Функция проверки закрытия все открытых скобок в строке.

    Parameters
    ----------
    s : str
        Строка для проверки

    Returns
    -------
    bool
        True, если все открытые скобки закрыты. Иначе False.

    '''
    if s == '':
        return False

    if bracket_count_check(s):
        return False

    if bracket_index_check(s):
        return False

    return True


parser.add_argument('string', type=str, help='Строка, в которой нужно проверить закрытие скобок')

args = parser.parse_args()

if __name__ == '__main__':
    result = check_brackets_closed(args.string)
    print(result)
