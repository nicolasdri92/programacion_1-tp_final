from controllers.hhcc import *
from services.handlerIO import readTXT, readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *

class Paciente:

    def __init__(self) -> None:
        breakLine()
        self.doc = input("Documento de identidad: ")
        self.apellido = input("Apellido: ")
        self.nombre = input("Nombre: ")
        self.nacimiento = input("Fecha de nacimiento: ")
        self.nacionalidad = getNacionalidad()

    def listar() -> None:
        breakLine()
        print("CODIGO    DOCUMENTO    APELLIDO    NOMBRE    NACIMIENTO    NACIONALIDAD")
        print("-----------------------------------------------------------------------")
        if (len(dataPaciente) > 0):
            for item in dataPaciente:
                print(
                    f"{item['id']}         {item['documento']} {item['apellido']}  {item['nombre']}    {item['nacimiento']}    {item['nacionalidad']}")
        else:
            breakLine()
            print("No hay pacientes cargados")

    def update(index: int, new_data: dict) -> None:
        dataPaciente[index].update(new_data)

    def remove(index: int) -> None:
        dataPaciente.pop(index)


def menuCrear() -> None:
    clear()
    print("#### NUEVO PACIENTE ####")
    paciente = Paciente()
    id = readTXT()
    dataPaciente.append(iPaciente(paciente, id))
    save(dataPaciente, PACIENTES)
    print(input("Paciente creado. Presione Enter..."))


def menuListar() -> None:
    clear()
    print("#### LISTA DE PACIENTES ####")
    Paciente.listar()
    breakLine()
    print(input("Presione Enter para continuar..."))


def menuEditar() -> None:
    clear()
    print("#### ACTUALIZAR PACIENTE ####")
    Paciente.listar()
    breakLine()
    if len(dataPaciente) > 0 :
        codigo = inputCode()
        if not (isValid(dataPaciente, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            id = searchDict(codigo, dataPaciente)
            paciente = Paciente()
            index = searchIndex(
                codigo, dataPaciente)
            Paciente.update(index, iPaciente(paciente, id))
            save(dataPaciente, PACIENTES)
            print(input("Paciente actualizado. Presione Enter..."))
    else: 
        print(input("Presione Enter para continuar..."))

def menuRemover() -> None:
    clear()
    print("#### ELIMINAR PACIENTE ####")
    Paciente.listar()
    breakLine()
    if len(dataPaciente) > 0 :
        codigo = inputCode()
        if not (isValid(dataPaciente, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuRemover()
        else:
            Paciente.remove(searchIndex(codigo, dataPaciente))
            save(dataPaciente, PACIENTES)
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
            if (retorno == '1'):
                menuListar()
            elif (retorno == '2'):
                menuCrear()
            elif (retorno == '3'):
                menuEditar()
            elif (retorno == '4'):
                menuRemover()
        else:
            clear()
            print(input(INVALID_CODE))

dataPaciente = readJSON(PACIENTES)
if (len(dataPaciente) == 0):
    dataPaciente = []
