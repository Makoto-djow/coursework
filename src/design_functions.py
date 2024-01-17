from src.sorting_functions import sorted_date
from datetime import datetime


def date_operation():
    """
    Оформление даты операции
    в формате ДД.ММ.ГГГГ
    """

    list_date = []
    operations = sorted_date()

    for op in operations:
        operation_date = datetime.fromisoformat(op['date'])
        list_date.append(operation_date.strftime('%d.%m.%Y'))

    return list_date


def display_description():
    """
    Отображает description операции
    """
    operation_description = []
    operations = sorted_date()
    for operation in operations:
        operation_description.append(operation['description'])

    return operation_description


def operation_sender():
    """
    Разделяет и частично показывает номер отправителя,
    если его нет, то передаёт пустую строку
    """

    senders = []
    operations = sorted_date()
    for operation in operations:
        if 'from' in operation:
            numbers = operation['from'][-16:-1]
            blocks = f'{numbers[0:4]} {numbers[4:6]}** **** {numbers[12:]}'
            result = operation['from'].replace(operation['from'][-16:-1], blocks)
            senders.append(result)

        else:
            senders.append('')

    return senders


def operation_recipient():
    """
    Частично показывает счёт
    """

    recipients = []
    operations = sorted_date()
    for operation in operations:
        hidden_account = operation['to'].replace(operation['to'][-20:-4], '**')
        recipients.append(hidden_account)

    return recipients


def operation_total_amount():
    """
    Показывает итоговую сумму
    """

    amounts = []
    operations = sorted_date()
    for operation in operations:
        amounts.append(operation['operationAmount']['amount'])

    return amounts


def operation_currency():
    """
    Показывает валюту
    """

    currencies = []
    operations = sorted_date()
    for operation in operations:
        currencies.append(operation['operationAmount']['currency']['name'])

    return currencies
