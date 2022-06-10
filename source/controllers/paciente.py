import math
from services.handlerIO import readTXT, readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *

data = readJSON(PACIENTES)
if (len(data) == 0):
    data[PACIENTES] = []


class Paciente:

    def __init__(self) -> None:
        breakLine()
        self.doc = input("Documento de identidad: ")
        self.apellido = input("Apellido: ")
        self.nombre = input("Nombre: ")
        self.nacimiento = input("Fecha de nacimiento: ")
        self.nacionalidad = getNacionalidad()

    def list() -> None:
        breakLine()
        print("CODIGO    DOCUMENTO    APELLIDO    NOMBRE    NACIMIENTO    NACIONALIDAD")
        print("-----------------------------------------------------------------------")
        if (len(data[PACIENTES]) > 0):
            for item in data[PACIENTES]:
                print(
                    f"{item['id']}         {item['documento']} {item['apellido']}  {item['nombre']}    {item['nacimiento']}    {item['nacionalidad']}")
        else:
            breakLine()
            print("No hay pacientes cargados")

    def update(index: int, new_data: dict) -> None:
        data[PACIENTES][index].update(new_data)

    def remove(index: int) -> None:
        data[PACIENTES].pop(index)


def menuCrear() -> None:
    clear()
    print("#### NUEVO PACIENTE ####")
    paciente = Paciente()
    id = readTXT()
    data[PACIENTES].append(iPaciente(paciente, id))
    save(data, PACIENTES)
    print(input("Paciente creado. Presione Enter..."))


def menuListar() -> None:
    clear()
    print("#### LISTA DE PACIENTES ####")
    Paciente.list()
    breakLine()
    print(input("Presione Enter para continuar..."))


def menuEditar() -> None:
    clear()
    print("#### ACTUALIZAR PACIENTE ####")
    Paciente.list()
    breakLine()
    if len(data[PACIENTES]) > 0 :
        codigo = inputCode()
        if not (isValid(data[PACIENTES], codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            id = searchDict(codigo, data[PACIENTES])
            paciente = Paciente()
            index = searchIndex(
                codigo, data[PACIENTES])
            Paciente.update(index, iPaciente(paciente, id))
            save(data, PACIENTES)
            print(input("Paciente actualizado. Presione Enter..."))
    else: 
        print(input("Presione Enter para continuar..."))

def menuRemover() -> None:
    clear()
    print("#### ELIMINAR PACIENTE ####")
    Paciente.list()
    breakLine()
    if len(data[PACIENTES]) > 0 :
        codigo = inputCode()
        if not (isValid(data[PACIENTES], codigo)):
            clear()
            print(input(INVALID_CODE))
            menuRemover()
        else:
            Paciente.remove(searchIndex(codigo, data[PACIENTES]))
            save(data, PACIENTES)
            print(input("Paciente eliminado. Presione Enter..."))
    else: 
        print(input("Presione Enter para continuar..."))



def iPaciente(entidad: Paciente, id: str) -> dict:
    return {
        'id': id,
        'documento': entidad.doc,
        'apellido': entidad.apellido,
        'nombre': entidad.nombre,
        'nacimiento': entidad.nacimiento,
        'nacionalidad': entidad.nacionalidad
    }

def inputCode():
    value = input("Codigo del paciente: (Cancelar) ")
    return handlerPaciente() if(value == '') else value

def getNacionalidad() -> str:
    value = input("Nacionalidad: (Argentina) ")
    return 'Argentina' if(value == '') else value


def menu() -> str:
    clear()
    print("#### Sección Pacientes ####")
    breakLine()
    print("1 - Listar Paciente")
    print("2 - Nuevo Paciente")
    print("3 - Editar Paciente")
    print("4 - Eliminar Paciente")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def handlerPaciente() -> None:
    retorno = '1'
    while (retorno != '0'):
        retorno = menu()
        if retorno in "01234":
            match retorno:
                case '1':
                    menuListar()
                case '2':
                    menuCrear()
                case '3':
                    menuEditar()
                case '4':
                    menuRemover()
                case '0':
                    return
        else:
            clear()
            print(input(INVALID_CODE))
