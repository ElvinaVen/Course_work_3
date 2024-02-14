from func import *

TRANSACTIONS_SOURCE = "operations.json"
TRANSACTION_COUNT = 5

transactions_list = load_transactions_from_json(TRANSACTIONS_SOURCE)  # чтение файла json
transactions_sort_list = get_sort_list(get_executed_transactions(transactions_list))  # сортированный список выполненных операций
selected_transactions_list = get_last_transactions(transactions_sort_list, TRANSACTION_COUNT)  # выборка TRANSACTION_COUNT транзакций

for transaction in selected_transactions_list:

    date_formatted, description = get_transaction_info(transaction)  # получение инф-ии о транзакции
    sender_account_name, sender_account_number = get_sender_info(transaction)  # получение инф-ии об отправителе
    receiver_account_name, masked_receiver_account = get_receiver_info(transaction)  # получение инф-ии о получателе

    amount = get_amount(transaction)  # получение суммы перевода
    currency = get_currency(transaction)  # получение валюты

    print(f"{date_formatted} {description}\n"
          f"{sender_account_name} {sender_account_number} -> {receiver_account_name} {masked_receiver_account}\n"
          f"{amount} {currency}\n")
