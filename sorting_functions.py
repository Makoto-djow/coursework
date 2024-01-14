from open_json import open_json_file

def sorted_executed():
    """
    Создаёт лист с операциями EXECUTED
    """

    executed_list = []
    operations = open_json_file()
    for operation in operations:
        if 'state' in operation:
            if operation["state"] == "EXECUTED":
                executed_list.append(operation)

    return executed_list


def sorted_date():
    """
    Сортирует по дате и создаёт список с пятью последними операциями по дате
    """

    date_list = sorted_executed()
    date_sorted_list = sorted(date_list, key=lambda x: x["date"])
    return date_sorted_list[-1:-6:-1]

print(*sorted_date(), sep='\n\n')
