class IntervaloInvalidoError(Exception):
    def __init__(self, intervalo: str):
        super().__init__(f"El intervalo {intervalo} no es válido, debe ser mayor que cero")