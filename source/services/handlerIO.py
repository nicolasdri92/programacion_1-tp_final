import os
import json


def readTXT():
    with open("source\\data\\pacienteNext.txt", "r", encoding='utf-8') as archivo:
        archivo_read = archivo.read()
    archivo_read = archivo_read
    writeTXT(archivo_read)
    return archivo_read


def writeTXT(value):
    value = str(int(value) + 1)
    with open(f"source\\data\\pacienteNext.txt", "w", encoding='utf-8') as archivo:
        archivo.write(value)


def readJSON(filename):
    file = f"source\\data\\{filename}.json"
    archivo_read = json.dumps({})
    if os.path.isfile(file):
        with open(file, "r", encoding='utf-8') as archivo:
            archivo_read = json.load(archivo)
    else:
        with open(file, 'w', encoding='utf-8') as archivo:
            archivo.write(archivo_read)
        archivo_read = json.loads(json.dumps({}))
    return archivo_read


def writeJSON(value, filename):
    file = f"source\\data\\{filename}.json"
    with open(file, "w", encoding='utf-8') as archivo:
        json.dump(value, archivo)
