# MediReminder

## Descripción general

**MediReminder** es un sistema de recordatorio de medicación orientado a usuarios que necesitan asistencia para seguir tratamientos médicos.  
El sistema permite registrar medicamentos, generar recordatorios automáticos y notificar al usuario en el momento adecuado según distintas estrategias configurables.  

El proyecto aplica los **cuatro patrones de diseño principales** vistos en la materia:  
- **Singleton**  
- **Factory Method**  
- **Strategy**  
- **Observer**  

Además, incorpora una capa adicional de **persistencia de datos** para guardar el historial de medicación.

---

## Objetivo del sistema

Garantizar que los usuarios tomen sus medicamentos correctamente mediante recordatorios inteligentes y flexibles.  
El sistema centraliza la información, evita duplicidades y automatiza las notificaciones, promoviendo la adherencia a tratamientos prolongados.

---

## Funcionalidades principales

1. **Gestión de medicamentos**: registro de dosis, nombres y frecuencia.  
2. **Recordatorios inteligentes**: alertas según distintas estrategias de repetición.  
3. **Notificación automática**: envío de avisos al usuario al cumplirse una alarma.  
4. **Historial de tratamientos**: almacenamiento y consulta del registro de medicación tomada.  
5. **Configuración centralizada**: instancia única que gestiona todo el flujo del sistema.

---

## Patrones de diseño utilizados

| Patrón | Descripción | Archivo principal | Clase principal |
|--------|--------------|-------------------|-----------------|
| **Singleton** | Garantiza una única instancia de gestión de recordatorios. | `reminder_manager.py` | `ReminderManager` |
| **Factory Method** | Crea distintos tipos de medicamentos dinámicamente. | `medication_factory.py` | `MedicationFactory` |
| **Strategy** | Define diferentes estrategias de recordatorio (diaria, por hora, semanal). | `reminder_strategy.py` | `ReminderStrategy` |
| **Observer** | Notifica automáticamente a los usuarios suscritos. | `notification_service.py` | `NotificationService` |
| **Persistencia** | Guarda y recupera el historial de tratamientos. | `registro_medicacion.py` | `RegistroMedicacionService` |

---

## Estructura del proyecto

```
MediReminder/
│
├── entidades/
│   ├── medicamentos/
│   │   ├── medicamento.py            ← clase base
│   │   ├── pastilla.py               ← subclase concreta
│   │   ├── jarabe.py                 ← subclase concreta
│   │   └── inyeccion.py              ← subclase concreta
│   │
│   ├── recordatorios/
│   │   ├── recordatorio.py           ← clase que contiene la información del recordatorio
│   │   ├── estrategia_diaria.py      ← Strategy 1
│   │   ├── estrategia_horas.py       ← Strategy 2
│   │   └── estrategia_semanal.py     ← Strategy 3
│   │
│   └── usuarios/
│       ├── usuario.py                ← clase base del usuario
│       └── notificacion.py           ← Observer
│
├── patrones/
│   ├── singleton/
│   │   └── reminder_manager.py       ← Singleton principal
│   ├── factory/
│   │   └── medication_factory.py     ← Factory Method
│   ├── strategy/
│   │   └── reminder_strategy.py      ← interfaz abstracta de Strategy
│   └── observer/
│       └── notification_service.py   ← manejador del Observer
│
├── servicios/
│   └── registro_medicacion.py        ← Persistencia de datos
│
├── main.py
├── README.md
├── USER_STORIES.md
└── JUSTIFICACION.md
```

---

## Ejecución del sistema

Para ejecutar el sistema desde consola:

```bash
python3 main.py
```

---

## Simulación por consola

```
======================================================================
  SISTEMA DE RECORDATORIO DE MEDICACIÓN - PATRONES DE DISEÑO
======================================================================

----------------------------------------------------------------------
  PATRÓN SINGLETON: Inicialización del gestor de recordatorios
----------------------------------------------------------------------
[OK] Instancia única de ReminderManager activa.
ID de instancia: 157649308712345

----------------------------------------------------------------------
  PATRÓN FACTORY METHOD: Creación de medicamentos
----------------------------------------------------------------------
[OK] Medicamento creado: Ibuprofeno (400mg)
[OK] Medicamento creado: Paracetamol (500mg)

----------------------------------------------------------------------
  PATRÓN STRATEGY: Configuración de estrategias de recordatorio
----------------------------------------------------------------------
[OK] Estrategia diaria establecida para Paracetamol 500mg
[OK] Estrategia cada 8 horas establecida para Ibuprofeno 400mg

----------------------------------------------------------------------
  PATRÓN OBSERVER: Notificación automática
----------------------------------------------------------------------
[INFO] Usuario suscrito: Juan Pérez
[OK] Notificación enviada: “Hora de tomar Paracetamol 500mg (08:00)”
[OK] Notificación enviada: “Hora de tomar Ibuprofeno 400mg (16:00)”

----------------------------------------------------------------------
  PERSISTENCIA DE DATOS
----------------------------------------------------------------------
[OK] Registro forestal guardado en: data/recordatorios_02-11-2025.dat
[OK] Historial leído correctamente (2 dosis registradas)

----------------------------------------------------------------------
  RESULTADO FINAL
----------------------------------------------------------------------
[OK] SINGLETON   - Instancia única verificada
[OK] FACTORY     - Medicamentos creados dinámicamente
[OK] STRATEGY    - Estrategias configuradas con éxito
[OK] OBSERVER    - Notificaciones enviadas
[OK] PERSISTENCIA- Registro almacenado correctamente
======================================================================
```

---

## Requisitos del sistema

- **Python 3.10 o superior**
- Librerías estándar (`datetime`, `pickle`, `abc`)
- Estructura de carpetas según el esquema de patrones

---

## Ejemplo de uso

```python
from patrones.singleton.reminder_manager import ReminderManager
from patrones.factory.medication_factory import MedicationFactory
from patrones.strategy.reminder_strategy import DailyReminder
from patrones.observer.notification_service import NotificationService

# Crear instancia única del gestor
manager = ReminderManager()

# Crear medicamentos
paracetamol = MedicationFactory.crear_medicamento("Pill", "Paracetamol", "500mg", "cada 12h")

# Asignar estrategia
manager.set_estrategia(DailyReminder())

# Suscribir usuario
usuario = NotificationService("Juan Pérez")
manager.suscribir(usuario)

# Generar recordatorio
manager.notificar(paracetamol.get_nombre(), "08:00")
```

---

## Validación de patrones

1. **Singleton**: La instancia del gestor es única en toda la ejecución.  
2. **Factory Method**: Cada medicamento se crea según su tipo dinámico.  
3. **Strategy**: El comportamiento de recordatorio varía sin modificar la lógica principal.  
4. **Observer**: Los observadores reciben actualizaciones automáticas.  
5. **Persistencia**: Los datos del usuario se guardan y leen correctamente.

---

## FLUJO DE EJECUCIÓN GENERAL

El archivo `main.py` coordina la ejecución completa del sistema aplicando los cuatro patrones de diseño:

| Etapa | Patrón | Descripción |
|-------|---------|-------------|
| 1 | **Singleton** | Inicializa el `ReminderManager`, garantizando una única instancia global del gestor de recordatorios. |
| 2 | **Factory Method** | Crea dinámicamente distintos tipos de medicamentos (`Pastilla`, `Jarabe`, `Inyeccion`) mediante la clase `MedicationFactory`. |
| 3 | **Strategy** | Define las estrategias de repetición (`DailyReminder`, `HourlyReminder`, `WeeklyReminder`) aplicadas a los recordatorios activos. |
| 4 | **Observer** | Gestiona las notificaciones automáticas a los usuarios suscritos mediante `NotificationService`. |
| 5 | **Persistencia** | Almacena todos los datos en archivos binarios (`.dat`) dentro de `/data` para conservar el historial. |

---

## PERSISTENCIA DE DATOS

El sistema utiliza un mecanismo de persistencia para almacenar los registros de medicación de cada usuario.  
Al finalizar la ejecución, todos los recordatorios activos, medicamentos asociados y horarios programados se guardan en un archivo `.dat` dentro de la carpeta `/data`.

### Archivo principal
- **`servicios/registro_medicacion.py`**

### Descripción técnica
- La función principal recibe un objeto `Usuario` con sus recordatorios activos.  
- Serializa la información utilizando el módulo `pickle` de Python.  
- Genera un archivo identificado por el nombre del usuario, por ejemplo:  
  `data/Carlos Perez.dat`

### Ejemplo de salida
```text
[OK] Registro de medicación guardado en: data/Carlos Perez.dat

---

### TRAZABILIDAD DE PATRONES

| Patrón | Archivo | Clase Principal | Descripción |
|--------|----------|----------------|--------------|
| **Singleton** | `patrones/singleton/reminder_manager.py` | `ReminderManager` | Gestiona una única instancia global de recordatorios. |
| **Factory Method** | `patrones/factory/medication_factory.py` | `MedicationFactory` | Crea instancias dinámicas de medicamentos. |
| **Strategy** | `patrones/strategy/reminder_strategy.py` | `ReminderStrategy` | Implementa estrategias de repetición personalizadas. |
| **Observer** | `patrones/observer/notification_service.py` | `NotificationService` | Notifica automáticamente al usuario al cumplirse un recordatorio. |
| **Persistencia** | `servicios/registro_medicacion.py` | `RegistroMedicacion` | Serializa y guarda los datos del usuario y sus recordatorios. |


---
## Autores

Proyecto desarrollado para la materia **Diseño de Sistemas**  
Facultad de Ingeniería – Universidad de Mendoza  

**Autor:** *Maria Eva Modarelli*
**Año:** 2025  

---
