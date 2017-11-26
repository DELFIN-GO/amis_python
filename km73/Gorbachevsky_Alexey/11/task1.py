"""
\mainpage Домашнее задание 11
"""

"""
Тема лабораторной работы 3:
Дан одномерный массив числовых значений. Вставить группу новых эллементов начиная с позиции K.
"""


def is_int_positive(text):
    """
    Проверяет является ли заданная строка положительным целым числом.

    Args:
        text: string

    Returns:
         bool
    """
    result = True
    allowed_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for current_symbol in text:
        if current_symbol not in allowed_digits:
            result = False

    return result


def is_int(text):
    """
    Проверяет является ли заданная строка целым числом.

    Args:
        text: string

    Returns:
        bool
    """
    if text[0] == '-':
        text = text[1:]
    result = is_int_positive(text)
    return result


def validate_input(checked_list, iteration=0):
    """
    Проверяет являются ли все эллементы списка целыми числами.

    Args:
        checked_list: list
        iteration: number is current iteration

    Returns:
        bool
    """
    result = True
    if iteration == len(checked_list):
        return result
    result = is_int(checked_list[iteration]) & validate_input(checked_list, iteration + 1)

    return result


def convert_list(converted_list, iteration=0):
    """
    Конвертирует заданный список в список чисел.

    Args:
        converted_list: list
        iteration: int - текущая итерация

    Returns:
        list
    """
    result = []
    if iteration == len(converted_list):
        return result
    result += [int(converted_list[iteration])] + convert_list(converted_list, iteration + 1)
    return result


def get_input():
    """
    Получает от пользователя 2 списка чисел и номер,начиная с которого в первый список нужно вставить второй.

    Returns:
        tuple - 2 списка и число
    """
    first_list = input("Enter first list: ").split()
    second_list = input("Enter second list: ").split()
    number_list = input("Enter position: ")
    while (not validate_input(first_list)) \
            | (not validate_input(second_list)) \
            | (not is_int_positive(number_list)):
        print("Bad input")
        first_list = input("Enter first list: ").split()
        second_list = input("Enter second list: ").split()
        number_list = input("Enter position: ")

    convert_list(first_list)
    convert_list(second_list)
    number = int(number_list)

    return first_list, second_list, number


def insert_list(first_list, second_list, position):
    """
    Вставляет second_list в first_list начиная с позиции position.

    Args:
        first_list: list
        second_list: list
        position: int

    Returns:
        list - новый список
    """
    return first_list[:position] + second_list + first_list[position:]


def print_list(printed_list, iteration=0):
    """
    Выводит printed_list.

    Args:
        printed_list: list
        iteration: int - текущая итерация

    Returns:
        None
    """
    if iteration == len(printed_list):
        print()
        return
    print(printed_list[iteration], end=' ')
    print_list(printed_list, iteration + 1)
    return


def test_insert_list():
    """
    Тестировка функции insert_list.

    Returns:
        None
    """
    assert (insert_list([1, 2, 3], [0, 0], 1) == [1, 0, 0, 2, 3])
    assert (insert_list([0], [1], 1) == [0, 1])


test_insert_list()
print_list(insert_list(*get_input()))
