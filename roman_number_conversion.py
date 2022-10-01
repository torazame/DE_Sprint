import itertools as it
import argparse


parser = argparse.ArgumentParser()

class ArabicRoman:
    def __init__(self):
        self.roman_number = None
        self._arabic_number = None
        self.mapper = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        self.ranks = ['thousands', 'hundreds', 'tens', 'ones']

    @property
    def arabic_number(self):
        return self._arabic_number

    @arabic_number.setter
    def arabic_number(self, n):
        if n > 3999:
            raise ValueError('Слишком большое число. Ввод должен быть в диапазоне от 1 до 3999.')
        self._arabic_number = n

    def _get_roman(self, n, rank):
        '''
        Функция перевода арабского числа в римское не уровне разряда.

        :param n: Число от 1 до 9.
        :type n: str | int
        :param rank: Наименование разряда. Принимает одно из значений: ones, tens, hundreds, thousands
        :type rank: str
        :return: Римское число
        :rtype: str
        '''
        key_mapper = {'ones': 1, 'tens': 10, 'hundreds': 100, 'thousands': 1000}
        key = key_mapper.get(rank, 0)

        n = int(n)
        if n <= 3:
            n_roman = self.mapper.get(key) * n
        elif n == 4:
            n_roman = self.mapper.get(key) + self.mapper.get(key * 5)
        elif n == 5:
            n_roman = self.mapper.get(key * n)
        elif 9 > n > 5:
            n_roman = self.mapper.get(key * 5) + self.mapper.get(key) * (n - 5)
        elif n == 9:
            n_roman = self.mapper.get(key) + self.mapper.get(key * 10)
        else:
            n_roman = 'Не удалось конвертировать...'
        return n_roman

    def _convert_to_roman(self):
        str_n = str(self.arabic_number)
        n_split = list(str_n)
        number_and_register = zip(n_split, self.ranks[-len(n_split):])
        self.roman_number = ''.join(it.starmap(self._get_roman, number_and_register))
        return self.roman_number

    def __call__(self, n):
        self.arabic_number = n
        return self._convert_to_roman()


converter = ArabicRoman()

parser.add_argument('number', type=int, help='Арабское число для конвертации в римскую систему счисления')

args = parser.parse_args()

if __name__ == '__main__':
    converter(args.number)
    print(f'\nАрабское число {converter.arabic_number} в римской системе счисления равно {converter.roman_number}\n')
