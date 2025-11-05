"""
Adaptador/conveniencia para estrategia diaria.
Crea una estrategia DailyReminder lista para usar en Recordatorio.
"""

from patrones.strategy.reminder_strategy import DailyReminder


def crear_estrategia_diaria(hora: int, minuto: int) -> DailyReminder:
    """
    Devuelve una instancia de DailyReminder que suena todos los días
    a la misma hora y minuto.
    Ejemplo: crear_estrategia_diaria(9, 0) -> 09:00 todos los días
    """
    return DailyReminder(hora_fija=hora, minuto_fijo=minuto)
