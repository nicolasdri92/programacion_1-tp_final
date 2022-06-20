from datetime import datetime
from controllers.profesional import loadData
from services.handlerIO import readTXT, readJSON
from services.helper import *
from services.validation import isValid
from lib.common import *
from lib.constants import *


class Historial:

    def __init__(self) -> None:
        self.fecha = input("Fecha: ")
        self.enfermedad = input("Enfermedad/afección que padece: ")
        Historial.listarProfesional()
        breakLine()
        if len(dataProfesional) > 0:
            breakLine()
            codigo = input("Codigo del Médico del instituto que lo trató: ")
            if not (isValid(dataProfesional, codigo)):
                clear()
                print(input(INVALID_CODE))
                menuCrear()
            else:
                clear()
                self.medico = searchDict(codigo, dataProfesional)['id']
        else:
            print(input("Presione Enter para continuar..."))
        clear()
        self.observacion = input("Observaciones: ")

    def listarConsulta(id) -> None:
        print("CODIGO  FECHA      ENFERMEDAD  MÉDICO         OBSERVACIÓN")
        print("------------------------------------------------")
        if (len(dataHHCC[id]) > 0):
            for item in dataHHCC[id]:
                print(
                    f"{item['id']}       {item['fecha']} {item['enfermedad']}   {getMedico(item['medico'])}  {item['observacion']}")
        else:
            breakLine()
            print("No hay consultas cargadas")

    def listarPaciente() -> None:
        breakLine()
        print("CODIGO  DOCUMENTO  APELLIDO  NOMBRE  EDAD  NACIMIENTO  NACIONALIDAD")
        print("-----------------------------------------------------------------------")
        if (len(dataPaciente) > 0):
            for item in dataPaciente:
                print(
                    f"{item['id']}       {item['documento']} {item['apellido']}     {item['nombre']}  {getEdad(item['nacimiento'])}    {item['nacimiento']}  {item['nacionalidad']}")
        else:
            breakLine()
            print("No hay pacientes cargados")

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

    def update(id: str, index: int, new_data: dict) -> None:
        dataHHCC[id][index].update(new_data)


def menuCrear() -> None:
    clear()
    print("#### NUEVA CONSULTA ####")
    Historial.listarPaciente()
    breakLine()
    if len(dataPaciente) > 0:
        codigo = input("Codigo del paciente: ")
        if not (isValid(dataPaciente, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuCrear()
        else:
            clear()
            paciente_id = searchDict(codigo, dataPaciente)['id']
            historial = Historial()
            id = readTXT(HHCC)
            dataHHCC[paciente_id].append(iHistorial(historial, id))
            save(dataHHCC, HHCC)
            print(input("Consulta creada. Presione Enter..."))
    else:
        print(input("Presione Enter para continuar..."))


def menuListar() -> None:
    clear()
    print("#### LISTAR HISTORIA CLINICA ####")
    Historial.listarPaciente()
    breakLine()
    if len(dataPaciente) > 0:
        codigo = input("Codigo del paciente: ")
        if not (isValid(dataPaciente, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            id = searchDict(codigo, dataPaciente)['id']
            Historial.listarConsulta(id)
            breakLine()
            print(input("Presione Enter para continuar..."))
    else:
        print(input("Presione Enter para continuar..."))


def menuEditar() -> None:
    clear()
    print("#### ACTUALIZAR CONSULTA ####")
    Historial.listarPaciente()
    breakLine()
    if len(dataPaciente) > 0:
        codigo = input("Codigo del paciente: ")
        if not (isValid(dataPaciente, codigo)):
            clear()
            print(input(INVALID_CODE))
            menuEditar()
        else:
            clear()
            paciente_id = searchDict(codigo, dataPaciente)['id']
            Historial.listarConsulta(paciente_id)
            breakLine()
            if len(dataHHCC[paciente_id]) > 0:
                codigo = input("Codigo de la consulta: ")
                if not (isValid(dataHHCC[paciente_id], codigo)):
                    clear()
                    print(input(INVALID_CODE))
                    menuEditar()
                else:
                    clear()
                    consulta_id = searchDict(
                        codigo, dataHHCC[paciente_id])['id']
                    historial = Historial()
                    index = searchIndex(codigo, dataHHCC[paciente_id])
                    Historial.update(consulta_id, index,
                                     iHistorial(historial, consulta_id))
                    save(dataHHCC, HHCC)
                    print(input("Consulta actualizada. Presione Enter..."))
            else:
                print(input("Presione Enter para continuar..."))
    else:
        print(input("Presione Enter para continuar..."))


def iHistorial(entidad: Historial, id: str) -> dict:
    return {
        'id': id,
        'fecha': entidad.fecha,
        'enfermedad': entidad.enfermedad,
        'medico': entidad.medico,
        'observacion': entidad.observacion
    }


def getMedico(id: str) -> str:
    for item in dataProfesional:
        if (item['id'] == id):
            return f"{item['apellido']}, {item['nombre']}"


def menu() -> str:
    clear()
    print("#### Sección Historias Clinicas ####")
    breakLine()
    print("1 - Listar Historia Clinica")
    print("2 - Nueva Consulta")
    print("3 - Editar Consulta")
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


def handlerHistorial() -> None:
    retorno = '1'
    while retorno != '0':
        loadData()
        retorno = menu()
        if retorno in "0123":
            if retorno == '1':
                menuListar()
            elif retorno == '2':
                menuCrear()
            elif retorno == '3':
                menuEditar()
        else:
            clear()
            print(input(INVALID_CODE))
