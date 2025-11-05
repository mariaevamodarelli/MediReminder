"""Patrón Singleton, gestiona unica instancia centralizada para todos los recordatorios activos."""

class ReminderManager:
    """Controlador central de recordatorios (Singleton)."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ReminderManager, cls).__new__(cls)
            cls._instancia._recordatorios = []
        return cls._instancia

    # ------------------------------------------------------------
    # Métodos de gestión
    # ------------------------------------------------------------

    def registrar_recordatorio(self, recordatorio):
        """Agrega un recordatorio al sistema."""
        self._recordatorios.append(recordatorio)
        print(f"[INFO] Recordatorio registrado: {recordatorio.get_medicamento().get_nombre()}")

    def eliminar_recordatorio(self, recordatorio):
        """Elimina un recordatorio existente."""
        if recordatorio in self._recordatorios:
            self._recordatorios.remove(recordatorio)
            print(f"[INFO] Recordatorio eliminado: {recordatorio.get_medicamento().get_nombre()}")

    def get_recordatorios(self):
        """Devuelve todos los recordatorios activos."""
        return list(self._recordatorios)

    def __str__(self):
        return f"ReminderManager con {len(self._recordatorios)} recordatorios activos."
