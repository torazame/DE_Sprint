### Проверка закрытия скобок

import argparse


parser = argparse.ArgumentParser()

brackets_open = ('(', '[', '{')
brackets_closed = (')', ']', '}')
bracket_pairs = {br_o: br_cl for br_o, br_cl in zip(brackets_open, brackets_closed)}


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

    check_res = []
    for bracket in brackets_open:
        if bracket in s:
            bracket_position = s.index(bracket)
            if bracket_pairs[bracket] in s[bracket_position+1:]:
                check_res.append(True)
            else:
                check_res.append(False)
    if len(check_res) == 0:
        return False
    return True if all(check_res) else False


parser.add_argument('string', type=str, help='Строка, в которой нужно проверить закрытие скобок')

args = parser.parse_args()

if __name__ == '__main__':
    result = check_brackets_closed(args.string)
    print(result)
