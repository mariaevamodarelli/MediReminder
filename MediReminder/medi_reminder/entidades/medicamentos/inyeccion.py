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
