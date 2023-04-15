from utils import sort_state_data, sort_data, formatted_data
def test_state_data(test_data):
    test_sort_state = sort_state_data(test_data)
    assert [x for x in test_sort_state if 'state' in x and x['state'] == 'EXECUTED'] == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
    ]

def test_state_data_1(test_data):
    test_data = []
    test_sort_state = sort_state_data(test_data)
    assert [x for x in test_sort_state if 'state' in x and x['state'] == 'EXECUTED'] == []
def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == [
        '2019-08-26T10:50:58.294041',
        "2019-07-03T18:35:29.512364",
        "2018-06-30T02:08:58.425572"
    ]

def test_formatted_data(test_data):
    tests_formatted_data = formatted_data(test_data)
    assert tests_formatted_data == ['\n'
         '26.08.2019 Перевод организации\n'
         'Maestro 1596 83** **** 5199 -> Счет **9589 \n'
         '31957.58 руб.\n'
         '         ',
         '\n'
         '03.07.2019 Перевод организации\n'
         'MasterCard 7158 30** **** 6758 -> Счет **5560 \n'
         '8221.37 USD\n'
         '         ',
         '\n'
         '30.06.2018 Перевод организации\n'
         'Счет 7510 68** **** 6952 -> Счет **6702 \n'
         '9824.07 USD\n'
         '         '
    ]
