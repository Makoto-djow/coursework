"""
## Задача

Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>


# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.


### Требования

+ Последние 5 выполненных (EXECUTED) операций выведены на экран.
+ Операции разделены пустой строкой.
+ Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
+ Сверху списка находятся самые последние операции (по дате).
+ Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
  (видны первые 6 цифр и последние 4,
  разбито по блокам по 4 цифры, разделенных пробелом).
+ Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).

## Данные

По каждой операции есть следующие данные:

- `id` — id транзакциии
- `date` — информация о дате совершения операции
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутстовать)
- `to` — куда

## Критерии выполнения

- [ + ]  Проект выложили на GitHub.
- [ + ]  Есть файл .gitignore
- [ + ]  Оформили файл README.md.
- [ + ]  В проекте есть минимум 2 ветки, причем разработка ведется в `develop`,
         а стабильная версия на момент сдачи проекта лежит в ветке `main`.
- [ + ]  Разработка проекта ведется в виртуальном окружении,
         в проекте есть информация о требованиях проекта (зависимостях).
- [ + ]  К проекту написали тесты с покрытием не менее 80%.
- [ + ]  Тесты написали на `pytest` или `unittest`.
- [ + ]  Проект структурированный, читаемый, каждая функция — не более 50 строк.
- [ + ]  Работа с файлом ведется через библиотеку json
"""

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
