class ErrorDePersistencia(Exception):
    def __init__(self, mensaje: str):
        super().__init__(f"Error de persistencia: {mensaje}")