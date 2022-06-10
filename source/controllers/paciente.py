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
        self.nacionalidad = input("Nacionalidad: ")

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
            print(input("No hay pacientes cargados. Presione Enter..."))

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
    codigo = input("Codigo del paciente: ")
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


def menuRemover() -> None:
    clear()
    print("#### ELIMINAR PACIENTE ####")
    Paciente.list()
    breakLine()
    codigo = input("Codigo del paciente: ")
    if not (isValid(data[PACIENTES], codigo)):
        clear()
        print(input(INVALID_CODE))
        menuRemover()
    else:
        Paciente.remove(searchIndex(codigo, data[PACIENTES]))


def iPaciente(entidad: Paciente, id: str) -> dict:
    return {
        'id': id,
        'documento': entidad.doc,
        'apellido': entidad.apellido,
        'nombre': entidad.nombre,
        'nacimiento': entidad.nacimiento,
        'nacionalidad': entidad.nacionalidad
    }


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
            if (retorno == '1'):
                menuListar()
            elif (retorno == '2'):
                menuCrear()
                save(data, PACIENTES)
                clear()
                print(input("Paciente creado. Presione Enter..."))
            elif (retorno == '3'):
                menuEditar()
                save(data, PACIENTES)
                clear()
                print(input("Paciente actualizado. Presione Enter..."))
            elif (retorno == '4'):
                menuRemover()
                save(data, PACIENTES)
                clear()
                print(input("Paciente eliminado. Presione Enter..."))
        else:
            clear()
            print(input(INVALID_CODE))
