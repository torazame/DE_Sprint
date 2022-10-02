### Умножение чисел в двоичном формате

import argparse


parser = argparse.ArgumentParser()


def convert_from_decimal(num, system):
    '''
    Функция перевода из десятичной системы в двоичную, восьмеричную или шестнадцатеричную.

    Parameters
    ----------
    num : int
        Число в десятичном формате.
    system : str
        Система счисления, в которую нужно перевести. Принимает одно из значений: {'bin', 'oct', 'hex'}

    Returns
    -------
    str
        Число в указанной системе счисления в виде строки.

    '''
    if system not in ['bin', 'oct', 'hex']:
        raise ValueError('Система счисления указана неверно')
    funcs ={
        'hex': lambda x: hex(x),
        'oct': lambda x: oct(x),
        'bin': lambda x: bin(x)
        }
    res = funcs[system](num)
    return res#[2:]


def convert_to_decimal(num, system):
    '''
    Функция перевод из двоичной, восьмеричной или шестнадцатеричной систем в десятичную.

    Parameters
    ----------
    num : str
        Число исходной системы счисления в формате строки
    system : str
        Система счисления, из которой нужно перевести. Принимает одно из значений: {'bin', 'oct', 'hex'}

    Returns
    -------
    int
        Число в десятичной системе счисления.

    '''
    if system not in ['bin', 'oct', 'hex']:
        raise ValueError('Система счисления указана неверно')

    funcs = {
        'hex': lambda x: '0x' + str(x),
        'oct': lambda x: '0o' + str(x),
        'bin': lambda x: '0b' + str(x)
        }
    res = funcs[system](num)
    return eval(res)


def multiply_binary(x1, x2, system='bin'):
    '''
    Умножение чисел в двоичной системе счисления.

    Parameters
    ----------
    x1 : str
        Первый множитель в формате строки.
    x2 : str
        Второй множитель в формате строки.
    system : str
        Система счисления. По умолчанию 'bin'.

    Returns
    -------
    str
        Результат умножения в виде строки.

    '''
    x1_converted = convert_to_decimal(x1, system)
    x2_converted = convert_to_decimal(x2, system)
    result = x1_converted * x2_converted
    return convert_from_decimal(result, system)


parser.add_argument('binary_number_1', type=str, help='Первый множитель в двоичном формате')
parser.add_argument('binary_number_2', type=str, help='Второй множитель в двоичном формате')

args = parser.parse_args()

if __name__ == '__main__':
    res = multiply_binary(args.binary_number_1, args.binary_number_2)
    print(res[2:])
