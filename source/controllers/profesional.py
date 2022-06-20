from services.handlerIO import readTXT, readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *


class Profesional:

    def __init__(self) -> None:
        breakLine()
        self.apellido = input("Apellido: ")
        self.nombre = input("Nombre: ")
        self.especialidad = input("Especialidad: ")

    def listar() -> None:
        breakLine()
        print("CODIGO  APELLIDO  NOMBRE  ESPECIALIDAD")
        print("-----------------------------------------")
        if (len(dataProfesional) > 0):
            for item in dataProfesional:
                print(
                    f"{item['id']}       {item['apellido']}      {item['nombre']} {item['especialidad']}")
        else:
            breakLine()
            print("No hay profesionales cargados")

    def update(index: int, new_data: dict) -> None:
        dataProfesional[index].update(new_data)

    def remove(index: int) -> None:
        dataProfesional.pop(index)


def menuCrear() -> None:
    clear()
    print("#### NUEVO PROFESIONAL ####")
    profesional = Profesional()
    id = readTXT(PROFESIONALES)
    dataProfesional.append(iProfesional(profesional, id))
    save(dataProfesional, PROFESIONALES)
    print(input("Profesional creado. Presione Enter..."))


def menuListar() -> None:
    clear()
    print("#### LISTA DE PROFESIONALES ####")
    Profesional.listar()
    breakLine()
    print(input("Presione Enter para continuar..."))


def menuEditar() -> None:
    clear()
    print("#### ACTUALIZAR PROFESIONAL ####")
    Profesional.listar()
    breakLine()
    if len(dataProfesional) > 0:
        codigo = input("Codigo del profesional: ")
        if not (isValid(dataProfesional, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            id = searchDict(codigo, dataProfesional)['id']
            profesional = Profesional()
            index = searchIndex(
                codigo, dataProfesional)
            Profesional.update(index, iProfesional(profesional, id))
            save(dataProfesional, PROFESIONALES)
            print(input("Profesional actualizado. Presione Enter..."))
    else:
        print(input("Presione Enter para continuar..."))


def menuRemover() -> None:
    clear()
    print("#### ELIMINAR PROFESIONAL ####")
    Profesional.listar()
    breakLine()
    if len(dataProfesional) > 0:
        codigo = input("Codigo del profesional: ")
        if not (isValid(dataProfesional, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuRemover()
        else:
            Profesional.remove(searchIndex(codigo, dataProfesional))
            save(dataProfesional, PACIENTES)
            print(input("Profesional eliminado. Presione Enter..."))
    else:
        print(input("Presione Enter para continuar..."))


def iProfesional(entidad: Profesional, id: str) -> dict:
    return {
        'id': id,
        'apellido': entidad.apellido,
        'nombre': entidad.nombre,
        'especialidad': entidad.especialidad
    }


def menu() -> str:
    clear()
    print("#### Sección Profesionales ####")
    breakLine()
    print("1 - Listar Profesionales")
    print("2 - Nuevo Profesional")
    print("3 - Editar Profesional")
    print("4 - Eliminar Profesional")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def loadData() -> None:
    global dataProfesional
    dataProfesional = readJSON(PROFESIONALES)
    if dataProfesional == '[]':
        dataProfesional = []


def handlerProfesional() -> None:
    retorno = '1'
    while (retorno != '0'):
        loadData()
        retorno = menu()
        if retorno in "01234":
            if retorno == '1':
                menuListar()
            elif retorno == '2':
                menuCrear()
            elif retorno == '3':
                menuEditar()
            elif retorno == '4':
                menuRemover()
        else:
            clear()
            print(input(INVALID_CODE))
