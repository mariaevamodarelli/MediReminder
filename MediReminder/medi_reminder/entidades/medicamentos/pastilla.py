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
