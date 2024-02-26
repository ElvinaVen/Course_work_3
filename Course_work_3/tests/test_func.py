import pytest

from Course_work_3.course_work_3.func import *


@pytest.fixture
def src():
    return {'id': 782295999, 'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824',
            'operationAmount': {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'Счет 24763316288121894080',
            'to': 'Счет 96291777776753236930'}


def test_get_currency(src):
    assert get_currency(src) == 'USD'


def test_get_amount(src):
    assert get_amount(src) == '54280.01'


def test_get_mask_receiver_account_number():
    assert get_mask_receiver_account_number('96291777776753236930') == '**6930'
    assert get_mask_receiver_account_number('962917777753237745') == '**7745'


def test_get_receiver_account(src):
    assert get_receiver_account(src) == 'Счет 96291777776753236930'


def test_split_sender_account_number():
    assert split_sender_account_number('247633**********4080') == '2476 33** **** **** 4080'


def test_get_mask_sender_account_number():
    assert get_mask_sender_account_number('24763316288121894080') == '247633**********4080'


def test_get_number_account():
    assert get_number_account('Счет 24763316288121894080') == '24763316288121894080'
    assert get_number_account('Счет 96291777776753236930') == '96291777776753236930'


def test_get_name_account():
    assert get_name_account('Счет 24763316288121894080') == 'Счет'
    assert get_name_account('Счет 96291777776753236930') == 'Счет'


def test_get_description(src):
    assert get_description(src) == 'Перевод организации'


def test_get_formatted_date(src):
    assert get_formatted_date(src) == '11.09.2019'


def test_get_sender_account(src):
    assert get_sender_account(src) == 'Счет 24763316288121894080'


def test_get_transaction_info(src):
    date_formatted, description = get_transaction_info(src)
    assert date_formatted == '11.09.2019'
    assert description == 'Перевод организации'


def test_get_sender_info(src):
    sender_account_name, sender_account_number = get_sender_info(src)
    assert sender_account_name == 'Счет'
    assert sender_account_number == '2476 33** **** **** 4080'


def test_get_receiver_info(src):
    receiver_account_name, masked_receiver_account = get_receiver_info(src)
    assert receiver_account_name == 'Счет'
    assert masked_receiver_account == '**6930'
