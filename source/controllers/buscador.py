from controllers.paciente import loadData, getEdad
from controllers.historial import loadData
from controllers.profesional import loadData
from services.handlerIO import readJSON
from services.helper import *
from lib.common import *
from lib.constants import *


def listar(items) -> None:
    print("CODIGO    DOCUMENTO    APELLIDO    NOMBRE    EDAD    NACIMIENTO    NACIONALIDAD")
    print("-----------------------------------------------------------------------")
    if (len(items) > 0):
        for item in items:
            print(
                f"{item['id']}       {item['documento']} {item['apellido']}     {item['nombre']}  {getEdad(item['nacimiento'])}    {item['nacimiento']}  {item['nacionalidad']}")
    else:
        breakLine()
        print("Sin resultados para la busqueda")


def listarProfesional() -> None:
    print("CODIGO   APELLIDO    NOMBRE  ESPECIALIDAD")
    print("-----------------------------------------")
    if (len(dataProfesional) > 0):
        for item in dataProfesional:
            print(
                f"{item['id']}  {item['apellido']}  {item['nombre']}    {item['especialidad']}")
    else:
        breakLine()
        print("No hay pacientes cargados")


def filtroNombre():
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    value = input("Apellido y/o Nombre: ")

    clear()
    pacientes = []

    for item in dataPaciente:
        if (item['apellido'] == value or item['nombre'] == value):
            pacientes.append(item)

    listar(pacientes)
    breakLine()
    input("Presione Enter para continuar...")


def filtroFecha():
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    min_date = getFormattedDate(input("Rango de Fecha inferior: "))
    max_date = getFormattedDate(input("Rango de Fecha superior: "))

    clear()
    pacientes = []

    i = 0
    for i in range(len(dataHHCC)):
        for item in dataHHCC[f'{i}']:
            if (getFormattedDate(item['fecha']) >= min_date and getFormattedDate(item['fecha']) <= max_date):
                paciente = searchDict(f'{i}', dataPaciente)
                pacientes.append(paciente)
        i += 1

    listar(pacientes)
    breakLine()
    input("Presione Enter para continuar...")


def filtroEnfermedad():
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    enfermedad = set()
    for values in dataHHCC.values():
        for item in values:
            enfermedad.add(item['enfermedad'])
    for item in enfermedad:
        print(item)
    breakLine()
    value = input("Enfermedad: ")

    clear()
    pacientes = []

    i = 0
    for i in range(len(dataHHCC)):
        for item in dataHHCC[f'{i}']:
            if (item['enfermedad'] == value):
                paciente = searchDict(f'{i}', dataPaciente)
                pacientes.append(paciente)
        i += 1

    listar(pacientes)
    breakLine()
    input("Presione Enter para continuar...")


def filtroMedico():
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    listarProfesional()
    breakLine()
    value = input("Médico: ")

    clear()
    pacientes = []

    i = 0
    for i in range(len(dataHHCC)):
        for item in dataHHCC[f'{i}']:
            if (item['medico'] == value):
                paciente = searchDict(f'{i}', dataPaciente)
                pacientes.append(paciente)
        i += 1

    listar(pacientes)
    breakLine()
    input("Presione Enter para continuar...")


def filtroNacionalidad():
    clear()
    print("#### Buscador de Paciente ####")
    breakLine()
    nacionalidad = set()
    for item in dataPaciente:
            nacionalidad.add(item['nacionalidad'])
    for item in nacionalidad:
        print(item)
    breakLine()
    value = input("Nacionalidad: ")

    clear()
    pacientes = []

    for item in dataPaciente:
        if (item['nacionalidad'] == value):
            pacientes.append(item)

    listar(pacientes)
    breakLine()
    input("Presione Enter para continuar...")


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
                filtroNombre()
            elif retorno == '2':
                filtroFecha()
            elif retorno == '3':
                filtroEnfermedad()
            elif retorno == '4':
                filtroMedico()
            elif retorno == '5':
                filtroNacionalidad()
        else:
            clear()
            print(input(INVALID_CODE))
