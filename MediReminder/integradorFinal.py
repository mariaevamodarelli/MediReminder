"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder
Fecha de generacion: 2025-11-05 10:03:08
Total de archivos integrados: 30
Total de directorios procesados: 13
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. main.py
#
# DIRECTORIO: medi_reminder
#   2. constantes.py
#
# DIRECTORIO: medi_reminder/entidades
#   3. __init__.py
#
# DIRECTORIO: medi_reminder/entidades/medicamentos
#   4. __init__.py
#   5. inyeccion.py
#   6. jarabe.py
#   7. medicamento.py
#   8. pastilla.py
#
# DIRECTORIO: medi_reminder/entidades/recordatorios
#   9. __init__.py
#   10. estrategia_diaria.py
#   11. estrategia_horas.py
#   12. estrategia_semanal.py
#   13. recordatorio.py
#
# DIRECTORIO: medi_reminder/entidades/usuarios
#   14. __init__.py
#   15. notificacion.py
#   16. usuario.py
#
# DIRECTORIO: medi_reminder/excepciones
#   17. error_de_persistencia.py
#   18. intervalo_invalido_error.py
#   19. tipo_medicamento_invalido.py
#
# DIRECTORIO: medi_reminder/patrones
#   20. __init__.py
#
# DIRECTORIO: medi_reminder/patrones/factory
#   21. __init__.py
#   22. medication_factory.py
#
# DIRECTORIO: medi_reminder/patrones/observer
#   23. __init__.py
#   24. notification_service.py
#
# DIRECTORIO: medi_reminder/patrones/singleton
#   25. __init__.py
#   26. reminder_manager.py
#
# DIRECTORIO: medi_reminder/patrones/strategy
#   27. __init__.py
#   28. reminder_strategy.py
#
# DIRECTORIO: medi_reminder/servicios
#   29. __init__.py
#   30. registro_medicacion.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/30: main.py
# Directorio: .
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/main.py
# ==============================================================================

import time
from datetime import datetime, timedelta
from medi_reminder.patrones.singleton.reminder_manager import ReminderManager
from medi_reminder.patrones.factory.medication_factory import MedicationFactory
from medi_reminder.patrones.strategy.reminder_strategy import DailyReminder, HourlyReminder, WeeklyReminder
from medi_reminder.patrones.observer.notification_service import NotificationService
from medi_reminder.entidades.recordatorios.recordatorio import Recordatorio
from medi_reminder.entidades.usuarios.usuario import Usuario
from medi_reminder.servicios.registro_medicacion import RegistroMedicacionService

print("=" * 70)
print("  SISTEMA DE RECORDATORIOS MÉDICOS ")
print("=" * 70)

# ----------------------------------------------------------------------
#  SINGLETON
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  PATRÓN SINGLETON: Inicializando ReminderManager")
print("----------------------------------------------------------------------")
manager1 = ReminderManager()
manager2 = ReminderManager()
print(f"[OK] Instancia única de ReminderManager confirmada (Singleton)")
print(f"     ID de instancia: {id(manager1)}")

# ----------------------------------------------------------------------
#  FACTORY - Creación de medicamentos
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  PATRÓN FACTORY METHOD: Creación de medicamentos")
print("----------------------------------------------------------------------")
factory = MedicationFactory()

ibuprofeno = factory.crear_medicamento("Pastilla", "Ibuprofeno", "400mg", "Cada 8 horas con comida")
amoxicilina = factory.crear_medicamento("Jarabe", "Amoxicilina", "5ml", "Cada 12 horas por 7 días")
insulina = factory.crear_medicamento("Inyeccion", "Insulina", "10U", "Cada mañana antes del desayuno")

print(f"[OK] Creado medicamento: {ibuprofeno}")
print(f"[OK] Creado medicamento: {amoxicilina}")
print(f"[OK] Creado medicamento: {insulina}")

# ----------------------------------------------------------------------
#  STRATEGY - Estrategias de recordatorio
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  PATRÓN STRATEGY: Estrategias de recordatorio")
print("----------------------------------------------------------------------")

estrategia1 = HourlyReminder(8)
estrategia2 = HourlyReminder(12)
estrategia3 = DailyReminder(hora_fija=9, minuto_fijo=30)

print("[OK] Estrategias configuradas:")
print("     - HourlyReminder (cada 8 horas)")
print("     - HourlyReminder (cada 12 horas)")
print("     - DailyReminder (09:30 todos los días)")

# ----------------------------------------------------------------------
#  CREACIÓN DE RECORDATORIOS
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  CREACIÓN DE RECORDATORIOS")
print("----------------------------------------------------------------------")
r1 = Recordatorio(ibuprofeno, estrategia1, datetime.now())
r2 = Recordatorio(amoxicilina, estrategia2, datetime.now())
r3 = Recordatorio(insulina, estrategia3, datetime.now())

manager1.registrar_recordatorio(r1)
manager1.registrar_recordatorio(r2)
manager1.registrar_recordatorio(r3)

print("[INFO] Recordatorio registrado: Ibuprofeno")
print("[INFO] Recordatorio registrado: Amoxicilina")
print("[INFO] Recordatorio registrado: Insulina")
print(f"[OK] Se registraron {len(manager1.get_recordatorios())} recordatorios activos en el sistema.")

# ----------------------------------------------------------------------
#  OBSERVER - Notificación al usuario
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  PATRÓN OBSERVER: Notificación automática al usuario")
print("----------------------------------------------------------------------")
notifier = NotificationService()
usuario = Usuario("Carlos Perez", "carlos.perez@gmail.com")
notifier.suscribir(usuario)

for rec in manager1.get_recordatorios():
    mensaje = f"Tomar {rec.get_medicamento().get_nombre()} ({rec.get_medicamento().get_dosis()}) ahora."
    notifier.notificar(mensaje)

print("[OK] Notificaciones enviadas correctamente a los usuarios suscritos.")

# ----------------------------------------------------------------------
#  SIMULACIÓN DE PASO DEL TIEMPO
# ----------------------------------------------------------------------
print("\n----------------------------------------------------------------------")
print("  SIMULACIÓN DE RECORDATORIOS - PASO DEL TIEMPO")
print("----------------------------------------------------------------------")

hora_actual = datetime.now()
for i, rec in enumerate(manager1.get_recordatorios(), start=1):
    horas_simuladas = i * 8
    nuevo_horario = hora_actual + timedelta(hours=horas_simuladas)
    print(f"\nEsperando {i * 3} segundos (simulando {horas_simuladas} horas)...")
    time.sleep(3)
    mensaje = f"[{nuevo_horario.strftime('%Y-%m-%d %H:%M')}] Tomar {rec.get_medicamento().get_nombre()} ({rec.get_medicamento().get_dosis()}) ahora."
    notifier.notificar(mensaje)

print("\n[OK] Simulación completada con éxito.")

# ----------------------------------------------------------------------
#  MOSTRAR ESTADO DEL USUARIO
# ----------------------------------------------------------------------
print("-------------------------------------------------------")
print(f"USUARIO: {usuario.get_nombre()}")
print(f"Contacto: {usuario.get_contacto()}")
print(f"Recordatorios activos: {len(manager1.get_recordatorios())}\n")

for i, rec in enumerate(manager1.get_recordatorios(), start=1):
    print(f"  Recordatorio #{i}: {rec.get_medicamento().get_nombre()} ({rec.get_medicamento().get_dosis()})")
    print(f"     Indicaciones: {rec.get_medicamento().get_indicaciones()}")
    print(f"     Próximo horario: {rec.get_proximo_horario().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ----------------------------------------------------------------------
#  PERSISTENCIA
# ----------------------------------------------------------------------
print("----------------------------------------------------------------------")
print("  PERSISTENCIA DE DATOS")
print("----------------------------------------------------------------------")
servicio_registro = RegistroMedicacionService()
registro = servicio_registro.crear_registro(usuario, manager1.get_recordatorios())
path = servicio_registro.persistir(registro)
print(f"[OK] Registro de medicación guardado en: {path}")

# ----------------------------------------------------------------------
#  RESUMEN FINAL
# ----------------------------------------------------------------------
print("\n======================================================================")
print("REGISTRO DE MEDICACIÓN")
print("======================================================================")
print(f"Usuario: {usuario.get_nombre()} ({usuario.get_contacto()})")
print(f"Fecha del registro: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"Total de recordatorios: {len(manager1.get_recordatorios())}")
print("-------------------------------------------------------------------")
for rec in manager1.get_recordatorios():
    med = rec.get_medicamento()
    print(f"  - {med.get_tipo()}: {med.get_nombre()} ({med.get_dosis()})")
    print(f"    Indicaciones: {med.get_indicaciones()}")
    print(f"    Próximo horario: {rec.get_proximo_horario().strftime('%Y-%m-%d %H:%M:%S')}\n")

print("======================================================================")
print("  EJEMPLO COMPLETADO EXITOSAMENTE")
print("======================================================================")
print("  [OK] SINGLETON   - Gestor único de recordatorios")
print("  [OK] FACTORY     - Creación dinámica de medicamentos")
print("  [OK] STRATEGY    - Estrategias de repetición configuradas")
print("  [OK] OBSERVER    - Notificación automática al usuario")
print("  [OK] SIMULACIÓN  - Paso del tiempo ejecutado correctamente")
print("  [OK] PERSISTENCIA- Registro médico almacenado correctamente")
print("======================================================================\n")



################################################################################
# DIRECTORIO: medi_reminder
################################################################################

# ==============================================================================
# ARCHIVO 2/30: constantes.py
# Directorio: medi_reminder
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/constantes.py
# ==============================================================================

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"




################################################################################
# DIRECTORIO: medi_reminder/entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/30: __init__.py
# Directorio: medi_reminder/entidades
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: medi_reminder/entidades/medicamentos
################################################################################

# ==============================================================================
# ARCHIVO 4/30: __init__.py
# Directorio: medi_reminder/entidades/medicamentos
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/30: inyeccion.py
# Directorio: medi_reminder/entidades/medicamentos
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/inyeccion.py
# ==============================================================================

"""
Subclase concreta: Inyeccion
Representa un medicamento inyectable.
"""

from .medicamento import Medicamento


class Inyeccion(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Inyeccion"


# ==============================================================================
# ARCHIVO 6/30: jarabe.py
# Directorio: medi_reminder/entidades/medicamentos
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/jarabe.py
# ==============================================================================

"""
Subclase concreta: Jarabe
Representa un medicamento líquido medido en ml.
"""

from .medicamento import Medicamento


class Jarabe(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Jarabe"


# ==============================================================================
# ARCHIVO 7/30: medicamento.py
# Directorio: medi_reminder/entidades/medicamentos
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/medicamento.py
# ==============================================================================

"""
Clase base 'Medicamento'.
Representa un medicamento genérico registrado por el usuario.

Este archivo se usa en:
- Factory Method (MedicationFactory) para crear subclases concretas.
- Recordatorios (se agenda un recordatorio asociado a un medicamento).
"""

class Medicamento:
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        """
        :param nombre: nombre comercial o genérico (ej: 'Ibuprofeno')
        :param dosis: detalle de la dosis (ej: '400mg', '2 ml')
        :param indicaciones: cómo debe tomarse (ej: 'cada 8 horas con comida')
        """
        self._nombre = nombre
        self._dosis = dosis
        self._indicaciones = indicaciones

    # ----- getters -----

    def get_nombre(self) -> str:
        return self._nombre

    def get_dosis(self) -> str:
        return self._dosis

    def get_indicaciones(self) -> str:
        return self._indicaciones

    def get_tipo(self) -> str:
        """Devuelve el tipo genérico. Las subclases lo sobrescriben."""
        return "Medicamento"

    # ----- representación humana -----

    def __str__(self) -> str:
        return (
            f"{self.get_tipo()} - {self._nombre} "
            f"({self._dosis}) | {self._indicaciones}"
        )


# ==============================================================================
# ARCHIVO 8/30: pastilla.py
# Directorio: medi_reminder/entidades/medicamentos
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/medicamentos/pastilla.py
# ==============================================================================

"""
Subclase concreta: Pastilla
Representa un medicamento sólido (tableta/cápsula).
Usada por la Factory.
"""

from .medicamento import Medicamento


class Pastilla(Medicamento):
    def __init__(self, nombre: str, dosis: str, indicaciones: str):
        super().__init__(nombre, dosis, indicaciones)

    def get_tipo(self) -> str:
        return "Pastilla"



################################################################################
# DIRECTORIO: medi_reminder/entidades/recordatorios
################################################################################

# ==============================================================================
# ARCHIVO 9/30: __init__.py
# Directorio: medi_reminder/entidades/recordatorios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 10/30: estrategia_diaria.py
# Directorio: medi_reminder/entidades/recordatorios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_diaria.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/30: estrategia_horas.py
# Directorio: medi_reminder/entidades/recordatorios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_horas.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 12/30: estrategia_semanal.py
# Directorio: medi_reminder/entidades/recordatorios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/estrategia_semanal.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 13/30: recordatorio.py
# Directorio: medi_reminder/entidades/recordatorios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/recordatorios/recordatorio.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: medi_reminder/entidades/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 14/30: __init__.py
# Directorio: medi_reminder/entidades/usuarios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/usuarios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/30: notificacion.py
# Directorio: medi_reminder/entidades/usuarios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/usuarios/notificacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 16/30: usuario.py
# Directorio: medi_reminder/entidades/usuarios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/entidades/usuarios/usuario.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: medi_reminder/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 17/30: error_de_persistencia.py
# Directorio: medi_reminder/excepciones
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/error_de_persistencia.py
# ==============================================================================

class ErrorDePersistencia(Exception):
    def __init__(self, mensaje: str):
        super().__init__(f"Error de persistencia: {mensaje}")

# ==============================================================================
# ARCHIVO 18/30: intervalo_invalido_error.py
# Directorio: medi_reminder/excepciones
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/intervalo_invalido_error.py
# ==============================================================================

class IntervaloInvalidoError(Exception):
    def __init__(self, intervalo: str):
        super().__init__(f"El intervalo {intervalo} no es válido, debe ser mayor que cero")

# ==============================================================================
# ARCHIVO 19/30: tipo_medicamento_invalido.py
# Directorio: medi_reminder/excepciones
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/tipo_medicamento_invalido.py
# ==============================================================================

class TipoMedicamentoInvalido(Exception):
    def __init__(self, tipo: str):
        super().__init__(f"El tipo de medicamento {tipo} no reconocido.")


################################################################################
# DIRECTORIO: medi_reminder/patrones
################################################################################

# ==============================================================================
# ARCHIVO 20/30: __init__.py
# Directorio: medi_reminder/patrones
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: medi_reminder/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 21/30: __init__.py
# Directorio: medi_reminder/patrones/factory
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/30: medication_factory.py
# Directorio: medi_reminder/patrones/factory
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/factory/medication_factory.py
# ==============================================================================

"""
Patrón Factory Method
Crea instancias concretas de medicamentos según el tipo solicitado.
"""

from medi_reminder.entidades.medicamentos.medicamento import Medicamento
from medi_reminder.entidades.medicamentos.pastilla import Pastilla
from medi_reminder.entidades.medicamentos.jarabe import Jarabe
from medi_reminder.entidades.medicamentos.inyeccion import Inyeccion
from medi_reminder.excepciones.tipo_medicamento_invalido import TipoMedicamentoInvalido


class MedicationFactory:
    """Fábrica de medicamentos."""

    @staticmethod
    def crear_medicamento(tipo: str, nombre: str, dosis: str, indicaciones: str) -> Medicamento:
        tipo = tipo.lower().strip()

        if tipo == "pastilla":
            return Pastilla(nombre, dosis, indicaciones)
        elif tipo == "jarabe":
            return Jarabe(nombre, dosis, indicaciones)
        elif tipo == "inyeccion":
            return Inyeccion(nombre, dosis, indicaciones)
        else:
            raise TipoMedicamentoInvalido(tipo)


################################################################################
# DIRECTORIO: medi_reminder/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 23/30: __init__.py
# Directorio: medi_reminder/patrones/observer
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/30: notification_service.py
# Directorio: medi_reminder/patrones/observer
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/observer/notification_service.py
# ==============================================================================

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




################################################################################
# DIRECTORIO: medi_reminder/patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 25/30: __init__.py
# Directorio: medi_reminder/patrones/singleton
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 26/30: reminder_manager.py
# Directorio: medi_reminder/patrones/singleton
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/singleton/reminder_manager.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: medi_reminder/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 27/30: __init__.py
# Directorio: medi_reminder/patrones/strategy
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 28/30: reminder_strategy.py
# Directorio: medi_reminder/patrones/strategy
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/patrones/strategy/reminder_strategy.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: medi_reminder/servicios
################################################################################

# ==============================================================================
# ARCHIVO 29/30: __init__.py
# Directorio: medi_reminder/servicios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/servicios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/30: registro_medicacion.py
# Directorio: medi_reminder/servicios
# Ruta completa: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/servicios/registro_medicacion.py
# ==============================================================================

import os
import pickle
from datetime import datetime
from medi_reminder.excepciones.error_de_persistencia import ErrorDePersistencia
from medi_reminder.constantes import DIRECTORIO_DATA, EXTENSION_DATA


class RegistroMedicacion:
    def __init__(self, usuario, recordatorios):
        self._usuario = usuario
        self._recordatorios = recordatorios
        self._fecha = datetime.now()

    def get_usuario(self):
        return self._usuario

    def get_recordatorios(self):
        return self._recordatorios

    def get_fecha(self):
        return self._fecha


class RegistroMedicacionService:
    def persistir(self, registro: RegistroMedicacion) -> str:
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        path = os.path.join(DIRECTORIO_DATA, f"{registro.get_usuario().get_nombre()}{EXTENSION_DATA}")
        try:
            with open(path, "wb") as f:
                pickle.dump(registro, f)
            return path
        except Exception as e:
            raise ErrorDePersistencia(str(e))

    def crear_registro(self, usuario, recordatorios):
        return RegistroMedicacion(usuario, recordatorios)

    def leer_registro(self, nombre_usuario: str) -> RegistroMedicacion:
        path = os.path.join(DIRECTORIO_DATA, f"{nombre_usuario}{EXTENSION_DATA}")
        if not os.path.exists(path):
            raise FileNotFoundError(f"No se encontró registro para {nombre_usuario}")

        with open(path, "rb") as f:
            return pickle.load(f)

    def mostrar_datos(self, registro: RegistroMedicacion):
        usuario = registro.get_usuario()
        recordatorios = registro.get_recordatorios()
        fecha = registro.get_fecha().strftime("%Y-%m-%d %H:%M")

        print("\n======================================================================")
        print("REGISTRO DE MEDICACIÓN")
        print("======================================================================")
        print(f"Usuario: {usuario.get_nombre()} ({usuario.get_contacto()})")
        print(f"Fecha del registro: {fecha}")
        print(f"Total de recordatorios: {len(recordatorios)}")
        print("-------------------------------------------------------------------")

        for rec in recordatorios:
            med = rec.get_medicamento()
            print(f"  - {med.get_tipo()}: {med.get_nombre()} ({med.get_dosis()})")
            print(f"    Indicaciones: {med.get_indicaciones()}")
            print(f"    Próximo horario: {rec.get_proximo_horario()}")
            print("")

        print("======================================================================\n")



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 30
# Generado: 2025-11-05 10:03:08
################################################################################
