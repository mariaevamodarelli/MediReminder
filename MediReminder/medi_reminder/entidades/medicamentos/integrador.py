"""
Archivo integrador generado automaticamente
Directorio: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos
Fecha: 2025-11-05 10:03:08
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: inyeccion.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/inyeccion.py
# ================================================================================

"""
Subclase concreta: Inyeccion
Representa un medicamento inyectable.
"""

from .medicamento import Medicamento


class Inyeccion(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Inyeccion"


# ================================================================================
# ARCHIVO 3/5: jarabe.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/jarabe.py
# ================================================================================

"""
Subclase concreta: Jarabe
Representa un medicamento líquido medido en ml.
"""

from .medicamento import Medicamento


class Jarabe(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Jarabe"


# ================================================================================
# ARCHIVO 4/5: medicamento.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/medicamento.py
# ================================================================================

"""
Clase base 'Medicamento'.
Representa un medicamento genérico registrado por el usuario.

Este archivo se usa en:
- Factory Method (MedicationFactory) para crear subclases concretas.
- Recordatorios (se agenda un recordatorio asociado a un medicamento).
"""

class Medicamento:
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        """
        :param nombre: nombre comercial o genérico (ej: 'Ibuprofeno')
        :param dosis: detalle de la dosis (ej: '400mg', '2 ml')
        :param indicaciones: cómo debe tomarse (ej: 'cada 8 horas con comida')
        """
        self._nombre = nombre
        self._dosis = dosis
        self._indicaciones = indicaciones

    # ----- getters -----

    def get_nombre(self) -> str:
        return self._nombre

    def get_dosis(self) -> str:
        return self._dosis

    def get_indicaciones(self) -> str:
        return self._indicaciones

    def get_tipo(self) -> str:
        """Devuelve el tipo genérico. Las subclases lo sobrescriben."""
        return "Medicamento"

    # ----- representación humana -----

    def __str__(self) -> str:
        return (
            f"{self.get_tipo()} - {self._nombre} "
            f"({self._dosis}) | {self._indicaciones}"
        )


# ================================================================================
# ARCHIVO 5/5: pastilla.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/pastilla.py
# ================================================================================

"""
Subclase concreta: Pastilla
Representa un medicamento sólido (tableta/cápsula).
Usada por la Factory.
"""

from .medicamento import Medicamento


class Pastilla(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Pastilla"


