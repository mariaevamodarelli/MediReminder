class TipoMedicamentoInvalido(Exception):
    def __init__(self, tipo: str):
        super().__init__(f"El tipo de medicamento {tipo} no reconocido.")