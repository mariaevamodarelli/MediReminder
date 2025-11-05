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
