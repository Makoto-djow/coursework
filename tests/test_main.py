from src.main import final_lists, list_date_, list_description_, list_from_, list_to_, list_sum_, list_currency_


def test_final_lists():
    assert final_lists(list_date_, list_description_, list_from_, list_to_, list_sum_, list_currency_) == [
        '\n08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD',
        '\n07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD',
        '\n19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.',
        '\n13.11.2019 Перевод со счета на счет\nСчет 38611439 52** **** 9794 -> Счет **8125\n62814.53 руб.',
        '\n05.11.2019 Открытие вклада\nСчет **8381\n21344.35 руб.'
    ]
