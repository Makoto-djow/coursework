from src.design_functions import date_operation, display_description, operation_sender, operation_recipient, \
    operation_total_amount, operation_currency

# Переданы результаты всех функций оформления
list_date_ = date_operation()
list_description_ = display_description()
list_from_ = operation_sender()
list_to_ = operation_recipient()
list_sum_ = operation_total_amount()
list_currency_ = operation_currency()


def final_lists(list_date, list_description, list_from, list_to, list_sum, list_currency):
    """
    Склеивает все элементы всех списков.
    Операции без "from" склеиваются отдельно.
    """
    number = -1
    operations = []
    while number != 4:
        if list_from[number + 1] == '':
            final_operations = (f'\n{list_date[number + 1]} {list_description[number + 1]}\n{list_from[number + 1]}'
                                f'{list_to[number + 1]}\n{list_sum[number + 1]} {list_currency[number + 1]}')
        else:
            final_operations = (f'\n{list_date[number + 1]} {list_description[number + 1]}\n{list_from[number + 1]}'
                                f' -> {list_to[number + 1]}\n{list_sum[number + 1]} {list_currency[number + 1]}')
        operations.append(final_operations)
        number += 1

    return operations


# Переменная содержащая результат функции склеивания
final_list = (final_lists(list_date_, list_description_, list_from_, list_to_, list_sum_, list_currency_))

# Финальный перебор операций и их последовательный вывод
for final_operation in final_list:
    print(final_operation)
