"""
Patrón Observer
Permite suscribir usuarios al sistema de notificaciones y avisarles automáticamente.
"""

class NotificationService:
    """Sujeto del patrón Observer."""

    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        """Agrega un nuevo observador (usuario)."""
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"[INFO] Usuario suscrito: {observador.get_nombre()}")

    def desuscribir(self, observador):
        """Elimina un observador de la lista."""
        if observador in self._observadores:
            self._observadores.remove(observador)
            print(f"[INFO] Usuario desuscrito: {observador.get_nombre()}")

    def notificar(self, mensaje: str):
        """Envía una notificación a todos los usuarios suscritos."""
        for observador in self._observadores:
            observador.recibir_notificacion(mensaje)

