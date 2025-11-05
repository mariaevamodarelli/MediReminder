"""
Adaptador/conveniencia para estrategia cada X horas.
"""

from patrones.strategy.reminder_strategy import HourlyReminder


def crear_estrategia_cada_horas(intervalo_horas: int) -> HourlyReminder:
    """
    Devuelve una instancia de HourlyReminder que se repite cada N horas.
    Ejemplo: crear_estrategia_cada_horas(8) -> cada 8 horas
    """
    return HourlyReminder(intervalo_horas=intervalo_horas)
