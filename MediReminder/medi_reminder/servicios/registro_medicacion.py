import os
import pickle
from datetime import datetime
from medi_reminder.excepciones.error_de_persistencia import ErrorDePersistencia

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"


class RegistroMedicacion:
    def __init__(self, usuario, recordatorios):
        self._usuario = usuario
        self._recordatorios = recordatorios
        self._fecha = datetime.now()

    def get_usuario(self):
        return self._usuario

    def get_recordatorios(self):
        return self._recordatorios

    def get_fecha(self):
        return self._fecha


class RegistroMedicacionService:
    def persistir(self, registro: RegistroMedicacion) -> str:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        path = os.path.join(DIRECTORIO_DATA, f"{registro.get_usuario().get_nombre()}{EXTENSION_DATA}")
        try:
            with open(path, "wb") as f:
                pickle.dump(registro, f)
            return path
        except Exception as e:
            raise ErrorDePersistencia(str(e))

    def crear_registro(self, usuario, recordatorios):
        return RegistroMedicacion(usuario, recordatorios)

    def leer_registro(self, nombre_usuario: str) -> RegistroMedicacion:
        path = os.path.join(DIRECTORIO_DATA, f"{nombre_usuario}{EXTENSION_DATA}")
        if not os.path.exists(path):
            raise FileNotFoundError(f"No se encontró registro para {nombre_usuario}")

        with open(path, "rb") as f:
            return pickle.load(f)

    def mostrar_datos(self, registro: RegistroMedicacion):
        usuario = registro.get_usuario()
        recordatorios = registro.get_recordatorios()
        fecha = registro.get_fecha().strftime("%Y-%m-%d %H:%M")

        print("\n======================================================================")
        print("REGISTRO DE MEDICACIÓN")
        print("======================================================================")
        print(f"Usuario: {usuario.get_nombre()} ({usuario.get_contacto()})")
        print(f"Fecha del registro: {fecha}")
        print(f"Total de recordatorios: {len(recordatorios)}")
        print("-------------------------------------------------------------------")

        for rec in recordatorios:
            med = rec.get_medicamento()
            print(f"  - {med.get_tipo()}: {med.get_nombre()} ({med.get_dosis()})")
            print(f"    Indicaciones: {med.get_indicaciones()}")
            print(f"    Próximo horario: {rec.get_proximo_horario()}")
            print("")

        print("======================================================================\n")
