import os

from services.handlerIO import readTXT, readJSON, writeJSON
from lib.constants import PACIENTES
from lib.common import cls

data = readJSON(PACIENTES)
if (len(data) == 0):
    data[PACIENTES] = []


class Paciente:

    def __init__(self):
        print("\n")
        self.doc = input("Documento de identidad: ")
        self.apellido = input("Apellido: ")
        self.nombre = input("Nombre: ")
        self.nacimiento = input("Fecha de nacimiento: ")
        self.nacionalidad = input("Nacionalidad: ")


def addPaciente():
    cls()
    print("#### NUEVO PACIENTE ####")
    paciente = Paciente()
    data[PACIENTES].append({
        'id': readTXT(),
        'documento': paciente.doc,
        'apellido': paciente.apellido,
        'nombre': paciente.nombre,
        'nacimiento': paciente.nacimiento,
        'nacionalidad': paciente.nacionalidad
    })


def editPaciente():
    cls()
    print("#### ACTUALIZAR PACIENTE ####")
    codigo = printPacientes()


def deletePaciente():
    cls()
    print("#### ELIMINAR PACIENTE ####")
    codigo = printPacientes()
    if not (isValid(codigo)):
        cls()
        print(input("Codigo Invalido. Presione Enter..."))
        printPacientes()
    else:
        data[PACIENTES].pop(searchIndexPaciente(codigo))


def searchIndexPaciente(codigo: str) -> int:
    i = 0
    for i in range(len(data[PACIENTES])):
        if (data[PACIENTES][i]['id'] == codigo):
            return (i)
        i += 1


def isValid(value: str) -> bool:
    for item in data[PACIENTES]:
        if (item['id'] == value):
            return True
    return False


def printPacientes() -> str | None:
    cls()
    print("CODIGO    DOCUMENTO    APELLIDO    NOMBRE    NACIMIENTO    NACIONALIDAD")
    print("-----------------------------------------------------------------------")
    if (len(data[PACIENTES]) > 0):
        for item in data[PACIENTES]:
            print(f"{item['id']}        {item['documento']}    {item['apellido']}         {item['nombre']} {item['nacimiento']}   {item['nacionalidad']}")
        print("\n")
        return input("Codigo del paciente: ")
    else:
        print("\n")
        print(input("No hay pacientes cargados. Presione Enter..."))
        handlerPaciente()


def savePaciente(paciente: dict):
    writeJSON(paciente, PACIENTES)


def menu():
    cls()
    print("#### Sección Pacientes ####")
    print("\n")
    print("1 - Nuevo Paciente")
    print("2 - Editar Paciente")
    print("3 - Eliminar Paciente")
    print("0 - Salir")
    print("\n")
    return input("Ingrese una accion: ")


def handlerPaciente():
    retorno = '1'
    while (retorno != '0'):
        retorno = menu()
        if retorno in "0123":
            if (retorno == '1'):
                addPaciente()
                savePaciente(data)
                # cls()
                print(input("Paciente creado. Presione Enter..."))
            elif (retorno == '2'):
                editPaciente()
                savePaciente(data)
                cls()
                print(input("Paciente actualizado. Presione Enter..."))
            elif (retorno == '3'):
                deletePaciente()
                savePaciente(data)
                cls()
                print(input("Paciente eliminado. Presione Enter..."))
        else:
            cls()
            print(input("Codigo Invalido. Presione Enter..."))
