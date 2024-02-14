import json
from datetime import datetime


def load_transactions_from_json(TRANSACTIONS_SOURCE):
    """
    Функция чтения файла json
    :param TRANSACTIONS_SOURCE: "operations.json" - файл, откуда считываем
    :return: transactions_list - список всех транзакций из файла
    """
    with open(TRANSACTIONS_SOURCE, 'r', encoding='utf-8') as file:
        transactions_list = json.load(file)  # загрузка из файла
    return transactions_list


def get_executed_transactions(transactions_list):
    """
    Функция формирования нового списка только из выполненных транзакций
    :param transactions_list: список всех транзакций из файла
    :return: executed_state_list - список транзакций со статусом "EXECUTED"
    """
    executed_state_list = []  # создаем пустой список
    for transaction in transactions_list:
        if transaction.get('state') == "EXECUTED":  # если статус "EXECUTED"
            executed_state_list.append(transaction)  # формируем новый список только из выполненных транзакций
    return executed_state_list


def get_sort_list(executed_state_list):
    """
    Функция сортировки списка транзакций по убыванию даты
    :param executed_state_list: список транзакций со статусом "EXECUTED"
    :return: transactions_sort_list - список транзакций сортированный по дате убывания
    """
    executed_state_list.sort(key=lambda operation: datetime.fromisoformat(operation.get('date')), reverse=True)  #
    # сортировка
    transactions_sort_list = executed_state_list  # создаем новый сортированный список
    return transactions_sort_list


def get_last_transactions(transactions_sort_list, TRANSACTION_COUNT):
    """
    Функция получения последних выполненных транзакций клиента
    :param transactions_sort_list: список транзакций сортированный по дате убывания
    :param TRANSACTION_COUNT: количество транзакций, которые необходимо вывести
    :return: selected_transactions_list - отобранный список транзакций
    """
    selected_transactions_list = transactions_sort_list[0:TRANSACTION_COUNT]
    return selected_transactions_list


def get_formatted_date(transaction):
    """
    Функция получения форматированной даты из транзакции
    :param transaction: единичная транзакция
    :return: date_formatted - отформатированная дата в виде дд.мм.гггг.
    """
    date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f")  # разбираем значение даты по ключу
    date_formatted = date.strftime("%d.%m.%Y")  # форматируем в нужном нам формате дд.мм.гггг.
    return date_formatted


def get_description(transaction):
    """
     Функция получения описания транзакции
    :param transaction: единичная транзакция
    :return: description - описание транзакции
    """
    description = transaction['description']
    return description


def get_sender_account(transaction):
    """
    Функция получения счета отправителя в формате "Visa Classic 2842878893689012"
    :param transaction: единичная транзакция
    :return: sender_account - счет отправителя
    """
    sender_account = transaction.get('from')
    return sender_account


def get_name_account(account):
    """
    Функция получения имени счета
    :param account: счет отправителя\получателя
    :return: pay_system_name - тип платежной системы отправителя\получателя
    """
    name_account = []
    account_string = str(account).split(" ")  # разделяем строку на подстроки по пробелам
    for word in account_string:
        if word.isalpha():  # если это слово, то добавляем в список name_account
            name_account.append(word)
    pay_system_name = ' '.join(name_account)  # объединяем подстроки в строку через пробел
    return pay_system_name


def get_number_account(account):
    """
    Функция получения номера счета
    :param account: счет отправителя\получателя
    :return: number_account - номер счета отправителя\получателя
    """
    just_digit = []
    account_string = str(account).split(" ")  # разделяем строку на подстроки по пробелам
    for word in account_string:
        if word.isdigit():  # если это цифра, то добавляем в список just_digit
            just_digit.append(word)
    number_account = ' '.join(just_digit)  # объединяем подстроки в строку через пробел
    return number_account


def get_mask_sender_account_number(sender_account_number):
    """
    Функция маскировки номера счета отправителя
    :param sender_account_number: номер счета отправителя
    :return: masked_sender_account - замаскированный номер счета отправителя в формате "284287******9012"
    """
    a = len(sender_account_number)
    masked_sender_account = ''
    for i in range(a):
        if (i >= 6) and (i < (a - 4)):
            masked_sender_account += "*"
        else:
            masked_sender_account += sender_account_number[i]
    return masked_sender_account


def split_sender_account_number(masked_sender_account):
    """
    Функция разделения номера счета на 4 части
    :param masked_sender_account: замаскированный номер счета отправителя в формате "284287******9012"
    :return: sender_account_number - результирующий номер счета отправителя
    """
    a = len(masked_sender_account)
    split_sender_account = [masked_sender_account[i:i + 4] for i in range(0, a, 4)]
    sender_account_number = ' '.join(split_sender_account)  # объединяем подстроки в строку через пробел
    return sender_account_number


def get_receiver_account(transaction):
    """
    Функция получения счета получателя
    :param transaction: единичная транзакция
    :return: receiver_account - счет получателя
    """
    receiver_account = transaction.get('to')
    return receiver_account


def get_mask_receiver_account_number(receiver_account_number):
    """
    Функция маскировки номера счета получателя
    :param receiver_account_number: номер счета получателя
    :return: masked_receiver_account - замаскированный номер счета получателя в формате "**5907"
    """
    a = receiver_account_number[-6:]
    masked_receiver_account = ''
    for i in range(len(a)):
        if i < 2:
            masked_receiver_account += "*"
        else:
            masked_receiver_account += a[i]
    return masked_receiver_account


def get_amount(transaction):
    """
    Функция получения суммы перевода
    :param transaction: единичная транзакция
    :return: amount - сумма перевода
    """
    amount = transaction["operationAmount"]["amount"]
    return amount


def get_currency(transaction):
    """
    Функция получения валюты
    :param transaction: единичная транзакция
    :return: currency - валюта
    """
    currency = transaction["operationAmount"]["currency"]["name"]
    return currency
