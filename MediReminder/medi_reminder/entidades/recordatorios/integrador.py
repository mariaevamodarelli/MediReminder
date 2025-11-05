"""
Archivo integrador generado automaticamente
Directorio: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios
Fecha: 2025-11-05 10:03:08
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: estrategia_diaria.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_diaria.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: estrategia_horas.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_horas.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/5: estrategia_semanal.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_semanal.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: recordatorio.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/recordatorio.py
# ================================================================================

"""
Representa un recordatorio concreto de medicación.

Un recordatorio sabe:
- qué medicamento corresponde tomar
- bajo qué estrategia de repetición (Strategy)
- cuál es el próximo horario programado
"""

from datetime import datetime
from medi_reminder.patrones.strategy.reminder_strategy import ReminderStrategy


class Recordatorio:
    def __init__(self, medicamento, estrategia: ReminderStrategy, proximo_horario: datetime):
        """
        :param medicamento: instancia de una subclase de Medicamento
        :param estrategia: instancia de una Strategy concreta
               (DailyReminder, HourlyReminder, WeeklyReminder, etc.)
        :param proximo_horario: datetime del próximo disparo programado
        """
        self._medicamento = medicamento
        self._estrategia = estrategia
        self._proximo_horario = proximo_horario

    # --- getters básicos ---

    def get_medicamento(self):
        return self._medicamento

    def get_estrategia(self) -> ReminderStrategy:
        return self._estrategia

    def get_proximo_horario(self) -> datetime:
        return self._proximo_horario

    # --- comportamiento ---

    def reagendar(self):
        """
        Avanza el recordatorio según la estrategia asociada.
        Calcula el siguiente horario y lo guarda.
        """
        self._proximo_horario = self._estrategia.siguiente_disparo(self._proximo_horario)

    def __str__(self) -> str:
        return (
            f"Recordatorio -> {self._medicamento} | "
            f"Próximo: {self._proximo_horario}"
        )


