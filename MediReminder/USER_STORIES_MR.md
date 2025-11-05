# USER_STORIES.md

## ÉPICA PRINCIPAL

**Como usuario del sistema MediReminder**,  
quiero registrar y recibir recordatorios de mis medicamentos,  
para asegurarme de tomar mis dosis correctamente y no olvidar ningún tratamiento.

---

## HISTORIA DE USUARIO 1 – PATRÓN SINGLETON

**Título:** Control central de recordatorios  
**Patrón aplicado:** Singleton  
**Clase principal:** `ReminderManager`

### Descripción
Como usuario, quiero que el sistema gestione todos mis recordatorios desde una única instancia global,  
para que no haya duplicaciones o conflictos entre mis alarmas activas.

### Criterios de aceptación
- Debe existir una única instancia de `ReminderManager` en ejecución.  
- Todas las operaciones de registro y notificación deben acceder a la misma instancia.  
- Si se intenta crear otra instancia, el sistema debe devolver la ya existente.  

### Clases involucradas
- `ReminderManager` (Singleton)
- `NotificationService` (Observer)
- `MedicationFactory` (Factory)

### Pseudocódigo

```python
from patrones.singleton.reminder_manager import ReminderManager

manager1 = ReminderManager()
manager2 = ReminderManager()

assert id(manager1) == id(manager2)
print("[OK] Instancia única de ReminderManager activa.")
```

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-001 | Singleton | `reminder_manager.py` | `ReminderManager` |

---

## HISTORIA DE USUARIO 2 – PATRÓN FACTORY METHOD

**Título:** Creación de medicamentos dinámicos  
**Patrón aplicado:** Factory Method  
**Clase principal:** `MedicationFactory`

### Descripción
Como usuario, quiero poder registrar distintos tipos de medicamentos (pastillas, jarabes, inyecciones),  
para adaptar mi tratamiento a las distintas presentaciones que utilizo.

### Criterios de aceptación
- El sistema debe permitir crear medicamentos a partir de un tipo ingresado.  
- Cada tipo de medicamento debe heredar de una clase base común `Medication`.  
- Si el tipo solicitado no existe, el sistema debe informar el error.

### Clases involucradas
- `MedicationFactory` (Factory)
- `Medication` (Clase base)
- `Pill`, `Syrup`, `Injection` (Subclases concretas)

### Ejemplo de código

```python
from patrones.factory.medication_factory import MedicationFactory

pill = MedicationFactory.crear_medicamento("Pill", "Ibuprofeno", "400mg", "cada 8 horas")
print(f"[OK] Medicamento creado: {pill.get_nombre()} ({pill.get_dosis()})")
```

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-002 | Factory Method | `medication_factory.py` | `MedicationFactory` |

---

## HISTORIA DE USUARIO 3 – PATRÓN STRATEGY

**Título:** Estrategias de recordatorio flexibles  
**Patrón aplicado:** Strategy  
**Clase principal:** `ReminderStrategy`

### Descripción
Como usuario, quiero poder elegir diferentes estrategias de recordatorio,  
para definir si mis alertas son diarias, cada cierto número de horas o semanales.

### Criterios de aceptación
- El sistema debe implementar al menos tres estrategias distintas:
  - `DailyReminder`
  - `HourlyReminder`
  - `WeeklyReminder`
- Cada estrategia debe redefinir el método `recordar()`.  
- El usuario puede cambiar la estrategia sin alterar la lógica general del programa.

### Clases involucradas
- `ReminderStrategy` (Interfaz base)
- `DailyReminder`, `HourlyReminder`, `WeeklyReminder` (Implementaciones concretas)
- `ReminderManager` (Singleton que utiliza la estrategia activa)

### Ejemplo de código

```python
from patrones.strategy.reminder_strategy import DailyReminder, HourlyReminder

estrategia = HourlyReminder(intervalo=8)
estrategia.recordar("Paracetamol 500mg")
```

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-003 | Strategy | `reminder_strategy.py` | `ReminderStrategy` |

---

## HISTORIA DE USUARIO 4 – PATRÓN OBSERVER

**Título:** Notificación automática al usuario  
**Patrón aplicado:** Observer  
**Clase principal:** `NotificationService`

### Descripción
Como usuario, quiero recibir notificaciones automáticas cuando llega la hora de tomar un medicamento,  
para no tener que revisar manualmente mis horarios de medicación.

### Criterios de aceptación
- El sistema debe permitir suscribirse a eventos de recordatorio.  
- Cuando el `ReminderManager` detecte la hora de toma, debe notificar a todos los observadores activos.  
- El usuario debe recibir el mensaje con el nombre del medicamento, dosis y horario.

### Clases involucradas
- `NotificationService` (Observer)
- `ReminderManager` (Subject)
- `Medication` (Entidad observada)

### Ejemplo de código

```python
from patrones.observer.notification_service import NotificationService
from patrones.singleton.reminder_manager import ReminderManager

manager = ReminderManager()
notifier = NotificationService("Juan Pérez")

manager.suscribir(notifier)
manager.notificar("Ibuprofeno 400mg", "14:00")
```

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-004 | Observer | `notification_service.py` | `NotificationService` |

---

## HISTORIA DE USUARIO 5 – PERSISTENCIA Y TRAZABILIDAD DE REGISTROS

**Título:** Guardado y lectura del historial de medicación  
**Patrón complementario:** Persistencia (sin patrón estructural específico)  
**Clase principal:** `RegistroMedicacionService`

### Descripción
Como usuario, quiero que el sistema registre las dosis tomadas,  
para consultar posteriormente mi historial médico y validar que cumplí el tratamiento.

### Criterios de aceptación
- Cada dosis tomada debe guardarse en un archivo de datos.  
- El sistema debe permitir consultar el historial por fecha o medicamento.  
- La lectura debe utilizar un formato legible y persistente (Pickle, JSON o CSV).

### Clases involucradas
- `RegistroMedicacionService`
- `Medication`
- `ReminderManager`

### Ejemplo de código

```python
from servicios.registro_medicacion import RegistroMedicacionService

service = RegistroMedicacionService()
service.guardar_dosis("Ibuprofeno", "400mg", "14:00")

historial = service.leer_historial()
print("[OK] Dosis registradas:", len(historial))
```

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-005 | Persistencia | `registro_medicacion.py` | `RegistroMedicacionService` |

---

### HISTORIA TÉCNICA 6 – GESTIÓN CENTRALIZADA DE RECORDATORIOS

**Título:** Control unificado de recordatorios activos  
**Patrón aplicado:** Singleton (gestor central)  
**Clase principal:** ReminderManager  

### Descripción

Como desarrollador del sistema, quiero que todos los recordatorios activos sean gestionados desde una única instancia global, para garantizar la consistencia de los datos y evitar duplicación de recordatorios.

### Criterios de aceptación

- Debe existir una única instancia de `ReminderManager` en ejecución.  
- Todas las operaciones (registro, eliminación, consulta) deben acceder a la misma instancia.  
- No se deben permitir múltiples listas o gestores paralelos de recordatorios.  
- La ejecución de `main.py` debe confirmar la unicidad del gestor y su control centralizado.

### Clases involucradas

- `ReminderManager` (Singleton)  
- `NotificationService` (Observer)  
- `Recordatorio` (Entidad)  
- `Usuario` (Entidad)  

### Pseudocódigo

```python
from patrones.singleton.reminder_manager import ReminderManager

manager1 = ReminderManager()
manager2 = ReminderManager()

assert id(manager1) == id(manager2)
print("[OK] Instancia única de ReminderManager confirmada.")

### Trazabilidad
| Requisito | Patrón | Archivo | Clase |
|------------|--------|----------|--------|
| REQ-006 | Singleton | `reminder_manager.py` | `ReminderManager` |

---
## CONCLUSIÓN

Cada historia de usuario corresponde directamente a un patrón de diseño y cumple con los principios SOLID,  
favoreciendo la separación de responsabilidades, la extensibilidad y la reutilización del código.  
MediReminder constituye un ejemplo claro y completo de aplicación práctica de los patrones más relevantes en la materia de **Diseño de Sistemas**.
