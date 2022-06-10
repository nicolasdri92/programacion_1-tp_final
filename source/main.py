import sys

from controllers.paciente import handlerPaciente
from lib.common import *
from lib.constants import *


def menu() -> str:
    clear()
    print("#### Instituto Médico Las Luciérnagas ####")
    breakLine()
    print("1 - Sección Paciente")
    print("2 - Sección Historia Clinica")
    print("3 - Sección Profesional")
    print("0 - Salir")
    breakLine()
    return input(INPUT_ACTION)


def main() -> None:
    try:
        retorno = '1'
        while (retorno != '0'):
            retorno = menu()
            if retorno in "0123":
                match retorno:
                    case '1':
                        handlerPaciente()
                    case '2':
                        return
                    # handlerHistoriaClinica()
                    case '3':
                        return
                    # handlerProfesional()
                    case '0':
                        return
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
