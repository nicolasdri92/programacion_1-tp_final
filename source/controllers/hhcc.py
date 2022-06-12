from controllers.paciente import *
from services.handlerIO import readTXT, readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *


class HISTORIA_CLINICA:

    def __init__(self) -> None:
        breakLine()
        self.fecha = input("Fecha: ")
        self.afeccion = input("Enfermedad/afección que padece: ")
        self.profesional = input("Medico: ")
        self.observacion = input("Observaciones: ")

    def listar() -> None:
        breakLine()
        print("CODIGO    DOCUMENTO    APELLIDO    NOMBRE    NACIMIENTO    NACIONALIDAD")
        print("-----------------------------------------------------------------------")
        if (len(readJSON(PACIENTES)) > 0):
            for item in readJSON(PACIENTES):
                print(
                    f"{item['id']}         {item['documento']} {item['apellido']}  {item['nombre']}    {item['nacimiento']}    {item['nacionalidad']}")
        else:
            breakLine()
            print("No hay pacientes cargados")

    def update(index: int, new_data: dict) -> None:
        readJSON(PACIENTES)[index].update(new_data)

    def remove(index: int) -> None:
        readJSON(PACIENTES).pop(index)


def menuCrear() -> None:
    clear()
    HISTORIA_CLINICA.listar()
    breakLine()
    # if len(readJSON(PACIENTES)) > 0 :
    codigo = inputCode()
    #     if not (isValid(readJSON(PACIENTES), codigo)):
    #         clear()
    #         print(input(INVALID_CODE))
    #         menuEditar()
    #     else:
    #         clear()
    # id = searchDict(codigo, readJSON(PACIENTES))
    #         paciente = Paciente()
    #         index = searchIndex(
    #             codigo, readJSON(PACIENTES))
    #         Paciente.update(index, iPaciente(paciente, id))
    #         save(data, PACIENTES)
    #         print(input("Paciente actualizado. Presione Enter..."))
    # else: 
    #     print(input("Presione Enter para continuar..."))

    hhcc = HISTORIA_CLINICA()
    clear()
    print("#### NUEVA CONSULTA ####")
    dataHHCC.append(iHHCC(hhcc, codigo))
    save(dataHHCC, HHCC)
    print(input("Historia clinica creada. Presione Enter..."))


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
    if len(readJSON(PACIENTES)) > 0 :
        codigo = inputCode()
        if not (isValid(readJSON(PACIENTES), codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            id = searchDict(codigo, readJSON(PACIENTES))
            paciente = Paciente()
            index = searchIndex(
                codigo, readJSON(PACIENTES))
            Paciente.update(index, iHHCC(paciente, id))
            save(data, PACIENTES)
            print(input("Historia clinica actualizado. Presione Enter..."))
    else: 
        print(input("Presione Enter para continuar..."))

def menuRemover() -> None:
    clear()
    print("#### ELIMINAR PACIENTE ####")
    Paciente.list()
    breakLine()
    if len(readJSON(PACIENTES)) > 0 :
        codigo = inputCode()
        if not (isValid(readJSON(PACIENTES), codigo)):
            clear()
            print(input(INVALID_CODE))
            menuRemover()
        else:
            Paciente.remove(searchIndex(codigo, readJSON(PACIENTES)))
            save(data, PACIENTES)
            print(input("Historia clinica eliminado. Presione Enter..."))
    else: 
        print(input("Presione Enter para continuar..."))



def iHHCC(entidad: HHCC, id) -> dict:
    return {
        'id': id, 
        'fecha': entidad.fecha,
        'afeccion': entidad.afeccion,
        'profesional': entidad.profesional,
        'observacion': entidad.observacion
    }

def inputCode():
    value = input("Codigo del paciente: (Cancelar) ")
    return handlerHHCC() if(value == '') else value


def menu() -> str:
    clear()
    print("#### Sección Historia Clinica ####")
    breakLine()
    print("1 - Buscar Historia Clinica")
    print("2 - Nueva Consulta")
    print("3 - Editar Consulta")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def handlerHHCC() -> None:
    retorno = '1'
    while (retorno != '0'):
        retorno = menu()
        if retorno in "0123":
             if (retorno == '1'):
                menuListar()
             elif (retorno == '2'):
                menuCrear()
             elif (retorno == '3'):
                menuEditar()
        else:
            clear()
            print(input(INVALID_CODE))

dataHHCC = readJSON(HHCC)
if (len(dataHHCC) == 0):
    dataHHCC = []
