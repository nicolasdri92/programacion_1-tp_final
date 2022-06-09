import os
import sys

from controllers.paciente import handlerPaciente


def menu():
    os.system("clear")
    print("#### Instituto Médico Las Luciérnagas ####")
    print("\n")
    print("1 - Sección Paciente")
    print("2 - Sección Historia Clinica")
    print("3 - Sección Profesional")
    print("0 - Salir")
    print("\n")
    return input("Ingrese una accion: ")


def main() -> None:
    try:
        retorno = '1'
        while (retorno != '0'):
            retorno = menu()
            if retorno in "0123":
                if (retorno == '1'):
                    handlerPaciente()
                elif (retorno == '2'):
                    handlerPaciente()
                elif (retorno == '3'):
                    handlerPaciente()
            else:
                os.system("clear")
                print(input("Codigo Invalido. Presione Enter..."))
    except KeyboardInterrupt:
        os.system("clear")
        print("\nEjecución finalizada por el usuario")
    except Exception as err:
        print(err)


if __name__ == '__main__':
    sys.exit(main())
