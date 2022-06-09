data = {}
data['historias_clinicas'] = []


class Historia_Clinica:

    def __init__(self):
        self.fecha = input("Fecha: ")
        self.enfermedad = input("Enfermedad/afección que padece: ")
        self.medico = input("Médico del instituto que lo trató: ")
        self.observacion = input("Observaciones: ")


def addHistoriaClinica(id):
    print("#### NUEVA HISTORIA CLINICA ####")
    historiaClinica = Historia_Clinica()
    data['historias_clinicas'][id].append({
        'fecha': historiaClinica.fecha,
        'enfermedad': historiaClinica.enfermedad,
        'medico': historiaClinica.medico,
        'observacion': historiaClinica.observacion
    })
