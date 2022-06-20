import sys

from controllers.paciente import handlerPaciente
from controllers.historial import handlerHistorial
from controllers.profesional import handlerProfesional
from controllers.buscador import handlerBuscador
from lib.common import *
from lib.constants import *


def menu() -> str:
    clear()
    print("#### Instituto Médico Las Luciérnagas ####")
    breakLine()
    print("1 - Sección Paciente")
    print("2 - Sección Historia Clinica")
    print("3 - Sección Profesional")
    print("4 - Buscador")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def main() -> None:
    try:
        retorno = '1'
        while (retorno != '0'):
            retorno = menu()
            if retorno in "01234":
                if retorno == '1':
                    handlerPaciente()
                elif retorno == '2':
                    handlerHistorial()
                elif retorno == '3':
                    handlerProfesional()
                elif retorno == '4':
                    handlerBuscador()
            else:
                clear()
                print(input(INVALID_CODE))
    except KeyboardInterrupt:
        clear()
        breakLine()
        print("Ejecución finalizada por el usuario")
    except Exception as err:
        print(err)


if __name__ == '__main__':
    sys.exit(main())
