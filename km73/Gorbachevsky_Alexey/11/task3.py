def get_input():
    """
    Получает от пользователя список в который требуется вывести в обратном порядке.

    Returns:
        list
    """
    first_list = input("Enter list: ").split()

    return first_list


def print_reverse(printed_list, iteration=0):
    """
    Выводит printed_list в обратном порядке.

    Args:
        printed_list: list
        iteration: int - текущая итерация

    Returns:
        None
    """
    if iteration == len(printed_list):
        return
    print_reverse(printed_list, iteration + 1)
    print(printed_list[iteration], end=' ')
    return


print_reverse(get_input())
