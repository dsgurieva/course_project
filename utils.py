import json
from datetime import datetime


def get_load(path):
    """
    Загрузка списка операций
    :param path: путь к файлу
    :return: возвращает список словарей
    """
    with open(path, "rt", encoding="utf8") as file:
        operations = json.load(file)
        return operations

def sort_state_data(data):
    """
    Функция создат словарь со значением операции "EXECUTED"
    :param data: данные по операциям
    :return: список словарей
    """
    sort_state = []
    for row in data:
        if row.get("state", True) != True:
            if row["state"] == "EXECUTED":
                sort_state.append(row)
    return sort_state


def sort_data(data):
    """
    Функция сортирует операции по дате
    :param data: список словарей
    :return: пять последних по дате операций
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def formatted_data(data):
    """
    Функиция принимает выполненные операии
    :return:возвращает отформатированный список
    """
    formatted_datas = []

    for operation in data:
        date_formatted = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = operation["description"]
        amount = operation["operationAmount"]
        to_sender = operation["to"]
        to_info = f'Счет **{to_sender[-4:]}'

        if "from" in operation:
            sender = operation["from"].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        else:
            sender_info = "Открыт новый счёт"
            sender_bill = ""


        formatted_datas.append(f"""
{date_formatted} {description}
{sender_info} {sender_bill} -> {to_info} 
{amount["amount"]} {amount["currency"]["name"]}
         """)
    return formatted_datas

