import argparse

parser = argparse.ArgumentParser()


def check_palindrome(word):
    '''
    Функция, позволяющая определить, является ли введенное слово палиндромом.

    Parameters
    ----------
    word : str
        Слово или словосочетание (пробелы не будут учитываться)

    Returns
    -------
    bool
        True, если введенное слово или выражение является палиндромом. Иначе False.

    '''
    if not isinstance(word, str):
        try:
            word = str(word)
        except ValueError:
            print('Введите слово в текстовом формате')
            return
    w = word.replace(' ', '').lower()
    if len(w) < 3:
        return False
    elif (len(w) % 2) > 0:
        split_length = len(w) // 2
        w1 = w[:split_length]
        w2 = w[-split_length:]
    else:
        split_length = int(len(w) / 2)
        w1 = w[:split_length]
        w2 = w[-split_length:]
    if w1 == w2[::-1]:
        print(f'{word} - это палиндром')
        return True
    else:
        print(f'{word} - это НЕ палиндром')
        return False


parser.add_argument('word', help='Слово или выражение для проверки, является ли оно палиндромом',
                    type=str)

args = parser.parse_args()

if __name__ == '__main__':
    result = check_palindrome(args.word)
    print(f'Результат проверки - {result}')
