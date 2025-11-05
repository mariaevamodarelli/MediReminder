"""
Archivo integrador generado automaticamente
Directorio: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/factory
Fecha: 2025-11-05 10:03:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: medication_factory.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/factory/medication_factory.py
# ================================================================================

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

