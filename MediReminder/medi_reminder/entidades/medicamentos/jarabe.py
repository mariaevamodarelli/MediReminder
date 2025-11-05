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
