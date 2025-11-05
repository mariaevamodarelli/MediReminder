"""
Representa un usuario del sistema MediReminder.
El usuario:
- tiene un nombre
- puede tener varios recordatorios asociados
- puede recibir notificaciones (Observer)
"""

from typing import List
from medi_reminder.entidades.recordatorios.recordatorio import Recordatorio
from .notificacion import Notificacion


class Usuario:
    def __init__(self, nombre: str, contacto: str):
        """
        :param nombre: nombre del usuario final
        :param contacto: medio de contacto (ej: 'SMS +54...', 'email algo@dominio')
        """
        self._nombre = nombre
        self._contacto = contacto
        self._recordatorios: List[Recordatorio] = []
        self._historial_notificaciones: List[Notificacion] = []

    # ----- getters -----

    def get_nombre(self) -> str:
        return self._nombre

    def get_contacto(self) -> str:
        return self._contacto

    def get_recordatorios(self) -> List[Recordatorio]:
        return list(self._recordatorios)

    def get_historial_notificaciones(self) -> List[Notificacion]:
        return list(self._historial_notificaciones)

    # ----- manejo de recordatorios -----

    def agregar_recordatorio(self, recordatorio: Recordatorio):
        """Asocia un nuevo recordatorio de medicación a este usuario."""
        self._recordatorios.append(recordatorio)

    # ----- observer-style -----

    def recibir_notificacion(self, mensaje: str):
        """
        Método que puede ser llamado por NotificationService (Observer)
        para avisar al usuario que tiene que tomar algo.
        """
        notif = Notificacion(mensaje)
        self._historial_notificaciones.append(notif)
        # Para el parcial/imprimir en consola:
        print(f"[NOTIFICACION] -> {self._nombre}: {notif}")

    # ----- representación -----

    def mostrar_resumen(self):
        """
        Imprime un resumen parecido a lo que hacías con el Trabajador en PythonForestal.
        """
        print("-------------------------------------------------------")
        print(f"USUARIO: {self._nombre}")
        print(f"Contacto: {self._contacto}")
        print(f"Recordatorios activos: {len(self._recordatorios)}")
        print("")

        for idx, rec in enumerate(self._recordatorios, start=1):
            med = rec.get_medicamento()
            print(f"  Recordatorio #{idx}: {med.get_nombre()} ({med.get_dosis()})")
            print(f"     Indicaciones: {med.get_indicaciones()}")
            print(f"     Próximo horario: {rec.get_proximo_horario()}")
            print("")

        print("Historial de notificaciones recientes:")
        if not self._historial_notificaciones:
            print("  (sin notificaciones aún)")
        else:
            for n in self._historial_notificaciones[-5:]:
                print(f"  - {n}")
        print("-------------------------------------------------------")

    def __str__(self) -> str:
        return f"{self._nombre} ({self._contacto})"
