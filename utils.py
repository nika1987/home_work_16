import json


def open_json(file_name):
    """
    функция возвращает данные из файла

    """
    with open(file_name, encoding='UTF-8') as json_file:
        data = json.load(json_file)
    return data


def get_name(id):
    """
    функция возвращает имя пользователя по id

    """
    data = open_json('data/users.json')
    for user in data:
        if user['id'] == id:
            return user


#print(open_json('data/offers.json'))
