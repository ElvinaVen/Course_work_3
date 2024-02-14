from func import *

TRANSACTIONS_SOURCE = "operations.json"
TRANSACTION_COUNT = 8

transactions_list = load_transactions_from_json(TRANSACTIONS_SOURCE)  # запуск ф-ии чтения файла json
transactions_sort_list = get_sort_list(get_executed_transactions(
    transactions_list))  # запуск ф-ий формирования нового списка только из выполненных операций и его дальнейшей
# сортировки по убыванию даты
selected_transactions_list = get_last_transactions(transactions_sort_list, TRANSACTION_COUNT)  # запуск ф-ии отбора
# определенного количества последних транзакций из сортированного списка

for transaction in selected_transactions_list:
    date_formatted = get_formatted_date(transaction)  # вызов ф-ии получения форматированной даты из транзакции
    description = get_description(transaction)  # вызов ф-ии получения описания из транзакции

    sender_account = get_sender_account(transaction)  # вызов ф-ии получения счета отправителя
    sender_account_name = get_name_account(sender_account)  # вызов ф-ии получения типа платежной системы
    masked_sender_account = get_mask_sender_account_number(get_number_account(sender_account))  # вызов ф-ии маскировки
    # номер счета отправителя
    sender_account_number = split_sender_account_number(masked_sender_account)  # вызов ф-ии разделения номера счета
    # на 4 части

    receiver_account = get_receiver_account(transaction)  # вызов ф-ии получения счета получателя
    receiver_account_name = get_name_account(receiver_account)  # вызов ф-ии получения типа платежной системы
    masked_receiver_account = get_mask_receiver_account_number(get_number_account(receiver_account))  # вызов ф-ии
    # маскировки номера счета получателя

    amount = get_amount(transaction)  # вызов ф-ии получения суммы перевода
    currency = get_currency(transaction)  # вызов ф-ии получения валюты

    print(f"{date_formatted} {description}\n"
          f"{sender_account_name} {sender_account_number} -> {receiver_account_name} {masked_receiver_account}\n"
          f"{amount} {currency}\n")
