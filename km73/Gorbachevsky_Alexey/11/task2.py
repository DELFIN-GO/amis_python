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
    Получает от пользователя список в котором требуется найти минимум.

    Returns:
        list
    """
    first_list = input("Enter list: ").split()
    while not validate_input(first_list):
        print("Bad input")
        first_list = input("Enter list: ").split()

    convert_list(first_list)

    return first_list


def min_of_list(list_, iteration=0):
    """
    Возвращает минимум в списке.

    Args:
        list_: list
        iteration: int

    Returns:
        int - минимум в списке
    """
    if iteration == len(list_) - 1:
        return list_[iteration]
    return min(list_[iteration], min_of_list(list_, iteration + 1))


def test_min_of_list():
    """
    Тестировка функции min_of_list.

    Returns:
        None
    """
    assert (min_of_list([1, 2, 3]) == 1)
    assert (min_of_list([0]) == 0)
    assert (min_of_list([10, 0, 5]) == 0)


test_min_of_list()
print(min_of_list(get_input()))
