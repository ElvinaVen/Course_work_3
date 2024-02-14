from func import get_executed_operations, get_five_operations, sort_data, load_operations_from_json, get_formatted_date
from func import get_description, get_from_account_alpha, get_from_account_digit, get_from_account, get_operation_amount_name
from func import mask_number_account, split_number_account, get_to_account, mask_number_to_account, get_operation_amount_amount

operations_list = load_operations_from_json()  # запуск ф-ии чтения файла json
executed_state_list = get_executed_operations(
    operations_list)  # запуск ф-ии формирования нового списка только из выполненных операций
sort_list = sort_data(executed_state_list)  # запуск ф-ии сортировки списка выполненных операций по убыванию даты
last_operations_list = get_five_operations(sort_list)

for one_operation in last_operations_list:
    date_formatted = get_formatted_date(one_operation)  # вызов ф-ии получения форматированной даты из словаря операции
    description = get_description(one_operation)  # вызов ф-ии получения описания из словаря операции
    from_account = get_from_account(one_operation)
    alpha = get_from_account_alpha(from_account)
    digit = get_from_account_digit(from_account)
    result_account = mask_number_account(digit)
    split_result_account = split_number_account(result_account)
    to_account = get_to_account(one_operation)

    alpha_to = get_from_account_alpha(to_account)
    digit_to = get_from_account_digit(to_account)
    result_account_to = mask_number_to_account(digit_to)
    amount = get_operation_amount_amount(one_operation)  #!!!!!
    name = get_operation_amount_name(one_operation)

    print(f"{date_formatted} {description}\n"
          f"{alpha} {split_result_account} -> {alpha_to} {result_account_to}\n"
          f"{amount} {name}")
    print()
