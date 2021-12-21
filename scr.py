documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def person_search(doc_number):
    name = ""
    for search in documents:
        if doc_number == search["number"]:
            name = search["name"]
    if name == "":
        return f"документа под номером {doc_number} в базе нет"
    else:
        return name


def spot_search(doc_number):
    spot_number = ""
    for search in directories:
        if doc_number in directories[search]:
            spot_number = search
    if spot_number == "":
        return f"документа под номером {doc_number} в базе нет"
    else:
        return spot_number


def show_all():
    for search in documents:
        if search == documents[-1]:
            return f"{search['type']} '{search['number']}' '{search['name']}'"
        else:
            return f"{search['type']} '{search['number']}' '{search['name']}'"


def add_new(number, type, name, spot_number):
    if spot_number in directories:
        directories[spot_number].append(number)
        documents.append({"type": type, "number": number, "name": name})
        return "новый документ создан"
    else:
        return f"{spot_number} полки не существует"



def del_from_base(doc_number):
    crutch = {}
    crutch_2 = ""
    for search in documents:
        if search["number"] == doc_number:
            crutch = search
    for search_2 in directories:
        if doc_number in directories[search_2]:
            crutch_2 = search_2
    if crutch != {}:
        if crutch_2 != "":
            documents.remove(crutch)
            directories[crutch_2].remove(doc_number)
            return "документ успешно удален"
        else:
            return "Ошибка в базе данный! Проверте 'directories' и полки!"
    else:
        return f"Документа под номером {doc_number} нет в базе данных!"


def move_item():
    doc_number = input("Введите номер документа: ")
    spot_number = input("Введите номер целевой полки: ")
    crutch = ""
    if spot_number not in directories:
        print("такой полки не существует")
    else:
        for search in directories:
            if doc_number in directories[search]:
                crutch = search
        if crutch != "":
            directories[crutch].remove(doc_number)
            directories[spot_number].append(doc_number)
        else:
            print(f"Документа под номером {doc_number} нет в базе данных!")


def new_spot():
    spot_number = input("Введите номер новой полки: ")
    if spot_number in directories:
        print("Это не новая полка!!!!!")
    else:
        directories[spot_number] = []

