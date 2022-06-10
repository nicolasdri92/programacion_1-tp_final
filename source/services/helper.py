from services.handlerIO import writeJSON


def searchDict(codigo: str, list: list) -> dict:
    for item in list:
        if (item['id'] == codigo):
            return item['id']


def searchIndex(codigo: str, list: list) -> int:
    i = 0
    for i in range(len(list)):
        if (list[i]['id'] == codigo):
            return (i)
        i += 1


def save(data: list, filename: str) -> None:
    writeJSON(data, filename)
