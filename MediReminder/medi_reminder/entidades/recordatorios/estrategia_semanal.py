"""
Adaptador/conveniencia para estrategia semanal.
"""

from patrones.strategy.reminder_strategy import WeeklyReminder


def crear_estrategia_semanal(dia_semana: int, hora: int, minuto: int) -> WeeklyReminder:
    """
    Devuelve una instancia de WeeklyReminder que suena un día fijo de la semana.

    :param dia_semana: 0 = Lunes ... 6 = Domingo
    :param hora: hora objetivo (0-23)
    :param minuto: minuto objetivo (0-59)

    Ejemplo: crear_estrategia_semanal(0, 9, 30)
    -> Lunes 09:30
    """
    return WeeklyReminder(dia_semana=dia_semana, hora=hora, minuto=minuto)
