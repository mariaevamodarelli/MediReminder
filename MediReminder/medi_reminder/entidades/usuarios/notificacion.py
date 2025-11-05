"""
Objeto simple para representar una notificación enviada al usuario.
Esto es lo que el servicio Observer podría 'emitir'.
"""

from datetime import datetime


class Notificacion:
    def __init__(self, mensaje: str, timestamp: datetime | None = None):
        self._mensaje = mensaje
        self._timestamp = timestamp or datetime.now()

    def get_mensaje(self) -> str:
        return self._mensaje

    def get_timestamp(self) -> datetime:
        return self._timestamp

    def __str__(self) -> str:
        ts = self._timestamp.strftime("%Y-%m-%d %H:%M")
        return f"[{ts}] {self._mensaje}"
