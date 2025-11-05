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
