"""
Patrón Factory Method
Crea instancias concretas de medicamentos según el tipo solicitado.
"""

from medi_reminder.entidades.medicamentos.medicamento import Medicamento
from medi_reminder.entidades.medicamentos.pastilla import Pastilla
from medi_reminder.entidades.medicamentos.jarabe import Jarabe
from medi_reminder.entidades.medicamentos.inyeccion import Inyeccion
from medi_reminder.excepciones.tipo_medicamento_invalido import TipoMedicamentoInvalido


class MedicationFactory:
    """Fábrica de medicamentos."""

    @staticmethod
    def crear_medicamento(tipo: str, nombre: str, dosis: str, indicaciones: str) -> Medicamento:
        tipo = tipo.lower().strip()

        if tipo == "pastilla":
            return Pastilla(nombre, dosis, indicaciones)
        elif tipo == "jarabe":
            return Jarabe(nombre, dosis, indicaciones)
        elif tipo == "inyeccion":
            return Inyeccion(nombre, dosis, indicaciones)
        else:
            raise TipoMedicamentoInvalido(tipo)