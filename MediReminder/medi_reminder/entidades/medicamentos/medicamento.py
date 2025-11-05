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
