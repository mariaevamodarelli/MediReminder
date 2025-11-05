"""
Archivo integrador generado automaticamente
Directorio: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/strategy
Fecha: 2025-11-05 10:03:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: reminder_strategy.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/strategy/reminder_strategy.py
# ================================================================================

# patrones/strategy/reminder_strategy.py
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from medi_reminder.excepciones.intervalo_invalido_error import IntervaloInvalidoError




class ReminderStrategy(ABC):
    @abstractmethod
    def siguiente_disparo(self, ultimo_disparo: datetime) -> datetime:
        """Dado el último disparo, devuelve el próximo horario."""
        pass


class DailyReminder(ReminderStrategy):
    def __init__(self, hora_fija: int, minuto_fijo: int):
        # ej: hora_fija=9 -> todos los días 09:00
        self._hora = hora_fija
        self._minuto = minuto_fijo

    def siguiente_disparo(self, ultimo_disparo: datetime) -> datetime:
        prox = ultimo_disparo.replace(hour=self._hora, minute=self._minuto, second=0)
        if prox <= ultimo_disparo:
            # si ya pasó hoy, es mañana
            prox = prox + timedelta(days=1)
        return prox


class HourlyReminder(ReminderStrategy):
    def __init__(self, intervalo_horas: int):
        if intervalo_horas <= 0:
            raise IntervaloInvalidoError(intervalo_horas)
        self._intervalo = intervalo_horas

    def siguiente_disparo(self, ultimo_disparo: datetime) -> datetime:
        return ultimo_disparo + timedelta(hours=self._intervalo)


class WeeklyReminder(ReminderStrategy):
    def __init__(self, dia_semana: int, hora: int, minuto: int):
        """
        dia_semana: 0=lunes ... 6=domingo
        """
        self._dia_semana = dia_semana
        self._hora = hora
        self._minuto = minuto

        # Nota: la lógica de próximo disparo se calcula en runtime.
    def siguiente_disparo(self, ultimo_disparo: datetime) -> datetime:
        from datetime import timedelta

        # armamos candidato esta semana
        prox = ultimo_disparo.replace(
            hour=self._hora,
            minute=self._minuto,
            second=0
        )
        # ajustamos al día pedido
        diferencia = self._dia_semana - prox.weekday()
        if diferencia < 0:
            diferencia += 7
        prox = prox + timedelta(days=diferencia)

        # si ya pasó esta semana, sumamos 7 días
        if prox <= ultimo_disparo:
            prox = prox + timedelta(days=7)
        return prox


