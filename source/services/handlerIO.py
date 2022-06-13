import os
import json


def readTXT(filename: str) -> str:
    with open(f"source\\data\\{filename}_next.txt", "r", encoding='utf-8') as archivo:
        archivo_read = archivo.read()
    writeTXT(str(int(archivo_read) + 1), filename)
    return archivo_read


def writeTXT(value: str, filename: str) -> None:
    with open(f"source\\data\\{filename}_next.txt", "w", encoding='utf-8') as archivo:
        archivo.write(value)


def readJSON(filename: str) -> dict:
    file = f"source\\data\\{filename}.json"
    archivo_read = json.dumps([])
    if os.path.isfile(file):
        with open(file, "r", encoding='utf-8') as archivo:
            archivo_read = json.load(archivo)
    else:
        writeJSON(archivo_read, filename)
        archivo_read = json.loads(json.dumps([]))
    return archivo_read


def writeJSON(value: list, filename: str) -> None:
    file = f"source\\data\\{filename}.json"
    with open(file, "w", encoding='utf-8') as archivo:
        json.dump(value, archivo)
