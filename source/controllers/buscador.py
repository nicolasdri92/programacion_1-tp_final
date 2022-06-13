from controllers.paciente import loadData
from controllers.historial import loadData
from controllers.profesional import loadData
from services.handlerIO import readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *


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


def menu() -> str:
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    print("1 - Apellido y/o Nombre")
    print("2 - Fecha de Consulta")
    print("3 - Enfermedad")
    print("4 - Médico")
    print("5 - Nacionalidad")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def loadData() -> None:
    global dataPaciente, dataHHCC, dataProfesional
    dataPaciente = readJSON(PACIENTES)
    dataHHCC = readJSON(HHCC)
    dataProfesional = readJSON(PROFESIONALES)
    if dataPaciente == '[]':
        dataPaciente = []
    if len(dataHHCC) == 0:
        dataHHCC = {}
    if dataProfesional == '[]':
        dataProfesional = []


def handlerBuscador() -> None:
    retorno = '1'
    while (retorno != '0'):
        loadData()
        retorno = menu()
        if retorno in "012345":
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
