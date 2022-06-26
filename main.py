# Задание:
# Дан двумерный массив размером n*m, заполненный случайным образом.
# 1. Заменить максимальный элемент каждой строки нулем
# 2. Вставить после каждого столбца, содержащего максимальный элемент массива, столбец из
# нулей.
# 3. Удалить все столбцы, в которых встретится нечетный положительный элемент.
# 4. Поменять местами первый и предпоследний столбцы.

# Начинаем написание кода с тестов. Директория tests. Создаем пустые функции по заданию.


import random


def menu():
    using_array = []
    print("""
    Приложение, разработанное в ходе прохождения учебной практики.
    Выполнил: Студент ЗКИ21-16Б. Филин Дмитрий Алексеевич.
    Вариант №7.
    Задание:
Дан двумерный массив размером n*m, заполненный случайным образом.
1. Заменить максимальный элемент каждой строки нулем
2. Вставить после каждого столбца, содержащего максимальный элемент массива, столбец из
нулей.
3. Удалить все столбцы, в которых встретится нечетный положительный элемент.
4. Поменять местами первый и предпоследний столбцы.         
""")
    while True:
        if not using_array:
            m = get_number_from_input('Для начала работы необходимо сгенерировать массив.\n'
                  'Это можно сделать по нескольким параметрам.\n'
                  'Для начала введите длинну строки (размер подмассива)\n'
                  'Макисмальное значение: 1000, минимальное: 3\n'
                  'Введите значение:', 3, 1000)

            n = get_number_from_input('Введите количество столбцов (размер массива)\n'
                  'Макисмальное значение: 1000, минимальное: 3\n'
                  'Введите значение:', 3, 1000)

            min_random = get_number_from_input('Введите минимальное значение, возможное для двумерного массива\n'
                  'Минимальное значение: -1.000.000.000, максимальное: 500.000.000\n'
                  'Введите значение:', -1000000000, 500000000)

            max_random = get_number_from_input('Введите максимальное значение, возможное для двумерного массива\n'
                  f'Минимальное значение: {min_random+10}, максимальное: 1.000.000.000\n'
                  'Введите значение:', min_random+10, 1000000000)

            using_array = generate_2d_array(n, m, min_random, max_random)
        print('Ваш текущий массив:')
        for row in using_array:
            print(row)
        choice = get_number_from_input('Выберите операцию по пункту меню:\n'
              '1. Заменить максимальный элемент каждой строки нулем\n'
              '2. Вставить после каждого столбца, содержащего максимальный элемент массива'
              'столбец из нулей\n'
              '3. Удалить все столбцы, в которых встретиться нечетный положительный элемент\n'
              '4. Поменять местами первый и предпоследний столбцы\n'
              '5. Перегенерировать массив\n'
              '0. Выйти\n', 0, 5)
        if choice == 0:
            exit(0)
        if choice == 1:
            using_array = replace_every_max_element_with_zero(using_array)
            continue
        if choice == 2:
            using_array = insert_zero_column_after_column_with_max_element(using_array)
            continue
        if choice == 3:
            using_array = delete_column_with_odd_positive_element(using_array)
            continue
        if choice == 4:
            using_array = replace_first_with_before_last_column(using_array)
            continue
        if choice == 5:
            using_array = []
            continue


def get_number_from_input(message: str, min_value: int, max_value: int) -> int:
    print(message)
    first_attempt = True
    choice = None
    while first_attempt or (int(choice) < min_value or int(choice) > max_value):
        try:
            choice = int(input())
            first_attempt = False
            if choice < min_value or choice > max_value:
                raise ValueError
        except ValueError:
            print('Неверное значение, попробуйте еще раз:')
            continue
    return choice

def generate_2d_array(n: int, m: int, min_random: int, max_random: int) -> [[int]]:
    """Генерирует двумерный массив случайных чисел. n - количество массивов в массиве, m - размер одного массива
    min - минимальное число для генерации, max - макисмальное число для генерации. Размер массива не больше 1000x1000"""
    # Выходим, если n и m не валидны
    if n <= 0 or m <= 0 or n > 1000 or m > 1000:
        return []
    generated_array = []
    for _ in range(0, n):
        second_dimension_array = []
        for _ in range(0, m):
            second_dimension_array.append(random.randint(min_random, max_random))
        generated_array.append(second_dimension_array)
    return generated_array


def replace_every_max_element_with_zero(twod_array: [[int]]) -> [[int]]:
    """Заменяет максимальный элемент каждой строки нулем. (Каждого массива с числами внутри массива)"""
    for row in twod_array:
        row[row.index(max(row))] = 0
    return twod_array


def insert_zero_column_after_column_with_max_element(twod_array: [[int]]) -> [[int]]:
    """Вставляет столбец из 0 (добавление 0 в каждый массив в двумерном массиве на определенный индекс), если
    предыдущий столбец содержит максимальное значение в массиве"""
    # Получаем максимальное число из всего массива
    max_value = get_absolute_max_value_in_array(twod_array)
    # Находим индексы, после которых вставляем нули
    indexes_to_place_zeros_after = set()
    for row in twod_array:
        if max_value in row:
            last_found_index = -1
            while True:
                try:
                    last_found_index = row.index(max_value, last_found_index + 1)
                except ValueError:
                    break
                indexes_to_place_zeros_after.add(last_found_index)
    # Вставляем нули
    for row in twod_array:
        inserted = 0
        for index in indexes_to_place_zeros_after:
            if index+inserted == len(row)-1:
                row.append(0)
                inserted += 1
            else:
                row.insert(index+inserted+1, 0)
                inserted += 1
    return twod_array


def get_absolute_max_value_in_array(twod_array: [[int]]) -> int:
    tmp_max = 0
    for row in twod_array:
        tmp_max_local = max(row)
        if tmp_max_local > tmp_max:
            tmp_max = tmp_max_local
    return tmp_max


def delete_column_with_odd_positive_element(twod_array: [[int]]) -> [[int]]:
    """Удаляет столбец (один и тот же индекс каждого массива в массиве, если среди этих значений есть положительное,
    нечетное число)"""
    # Находим все столбцы, которые нужно удалить
    columns_to_delete = set()
    for row in twod_array:
        for element in row:
            if element > 0 and element % 2 != 0:
                columns_to_delete.add(row.index(element))
    # Удаляем столбцы
    for row in twod_array:
        deleted = 0
        for index in columns_to_delete:
            try:
                del row[index-deleted]
            except IndexError:
                break
            deleted += 1
    return twod_array


def replace_first_with_before_last_column(twod_array: [[int]]) -> [[int]]:
    """Заменяет первый с предпоследним столбцом (один и тот же индекс каждого массива в массиве)"""
    # Выходим, если в массиве меньше 3 массивов. Перестановка бессмысленна
    if len(twod_array) < 3:
        return twod_array
    before_last_index = len(twod_array[0]) - 2
    for row in twod_array:
        row[0], row[before_last_index] = row[before_last_index], row[0]
    return twod_array


if __name__ == "__main__":
    menu()
