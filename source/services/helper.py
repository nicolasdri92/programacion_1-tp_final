from datetime import datetime
from dateutil.relativedelta import relativedelta
from services.handlerIO import writeJSON
from lib.common import clear


def searchDict(codigo: str, list: list) -> dict:
    for item in list:
        if (item['id'] == codigo):
            return item


def searchIndex(codigo: str, list: list) -> int:
    i = 0
    for i in range(len(list)):
        if (list[i]['id'] == codigo):
            return (i)
        i += 1


def getFormattedDate(date):
    return datetime.strptime(date, "%d/%m/%Y")


def getEdad(nacimiento: str) -> str:
    fecha_nacimiento = getFormattedDate(nacimiento)
    edad = relativedelta(datetime.now(), fecha_nacimiento)
    return edad.years


def save(data: list, filename: str) -> None:
    writeJSON(data, filename)
    clear()
