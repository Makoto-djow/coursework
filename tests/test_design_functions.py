from src.design_functions import (date_operation, display_description, operation_sender, operation_recipient,
                                  operation_total_amount, operation_currency)


def test_date_operation():
    assert date_operation() == ['08.12.2019', '07.12.2019', '19.11.2019', '13.11.2019', '05.11.2019']


def test_display_description():
    assert display_description() == ['Открытие вклада', 'Перевод организации', 'Перевод организации',
                                     'Перевод со счета на счет', 'Открытие вклада']


def test_operation_sender():
    assert operation_sender() == ['', 'Visa Classic 2842 87** **** 9012', 'Maestro 7810 84** **** 5568',
                                  'Счет 38611439 52** **** 9794', '']


def test_operation_recipient():
    assert operation_recipient() == ['Счет **5907', 'Счет **3655', 'Счет **2869', 'Счет **8125', 'Счет **8381']


def test_operation_total_amount():
    assert operation_total_amount() == ['41096.24', '48150.39', '30153.72', '62814.53', '21344.35']


def test_operation_currency():
    assert operation_currency() == ['USD', 'USD', 'руб.', 'руб.', 'руб.']

