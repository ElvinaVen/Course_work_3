import datetime
import json
from datetime import datetime

OPERATIONS_SOURCE = "operations.json"


def load_operations_from_json():  # ф-ия чтения файла json
    with open(OPERATIONS_SOURCE, 'r', encoding='utf-8') as file:
        operations_list = json.load(file)  # загрузка из файла
    return operations_list


def get_executed_operations(operation_list):  # ф-ия формирования нового списка только из выполненных операций
    executed_state_list = []  # создаем пустой список
    for operation in operation_list:
        if operation.get('state') == "EXECUTED":  # если статус выполнен
            executed_state_list.append(operation)  # формируем новый список только из выполненных операций
    return executed_state_list


def sort_data(executed_state_list):  # сортируем список
    # выполненных операций по убыванию даты
    executed_state_list.sort(key=lambda operation: datetime.fromisoformat(operation.get('date')), reverse=True)  #
    # сортировка
    sort_list = executed_state_list  # создаем новый сортированный список
    return sort_list


def get_five_operations(sort_list):  # ф-ия получения последних пяти выполненных операций клиента
    last_operations_list = sort_list[0:5]
    return last_operations_list


def get_formatted_date(one_operation):  # ф-ия получения форматированной даты из словаря
    date = datetime.strptime(one_operation['date'], "%Y-%m-%dT%H:%M:%S.%f")  # разбираем значение даты по ключу
    date_formatted = date.strftime("%d.%m.%Y")  # форматируем в нужном нам формате дд.мм.гггг.
    return date_formatted


def get_description(one_operation):  # ф-ия получения описания из словаря операции
    description = one_operation['description']
    return description


def get_from_account(one_operation):
    from_account = one_operation.get('from')
    return from_account


def get_from_account_alpha(from_account):
    just_alpha = []
    from_account = str(from_account).split(" ")
    for word in from_account:
        if word.isalpha():
            just_alpha.append(word)
    return ' '.join(just_alpha)


def get_from_account_digit(from_account):
    just_digit = []
    from_account = str(from_account).split(" ")
    for word in from_account:
        if word.isdigit():
            just_digit.append(word)
    return ' '.join(just_digit)


def mask_number_account(split_result_account):
    a = len(split_result_account)
    result_account = ''
    for i in range(a):
        if i >= 6 and i < (a-4):
            result_account += "*"
        else:
            result_account += split_result_account[i]
    return result_account


def split_number_account(result_account):
    a = len(result_account)
    split_result_account = [result_account[i:i+4] for i in range(0, a, 4)]
    split_result_account2 =' '.join(split_result_account)

    return split_result_account2


def get_to_account(one_operation):
    to_account = one_operation.get('to')
    return to_account


def mask_number_to_account(digit_to):
    a = digit_to[-6:]
    result_account_to = ''
    for i in range(len(a)):
        if i < 2:
            result_account_to += "*"
        else:
            result_account_to += digit_to[i]
    return result_account_to


def get_operation_amount_amount(one_operation):
    return one_operation["operationAmount"]["amount"]


def get_operation_amount_name(one_operation):
    return one_operation["operationAmount"]["currency"]["name"]
