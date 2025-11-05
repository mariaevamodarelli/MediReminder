"""
Archivo integrador generado automaticamente
Directorio: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones
Fecha: 2025-11-05 10:03:08
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: error_de_persistencia.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/error_de_persistencia.py
# ================================================================================

class ErrorDePersistencia(Exception):
    def __init__(self, mensaje: str):
        super().__init__(f"Error de persistencia: {mensaje}")

# ================================================================================
# ARCHIVO 2/3: intervalo_invalido_error.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/intervalo_invalido_error.py
# ================================================================================

class IntervaloInvalidoError(Exception):
    def __init__(self, intervalo: str):
        super().__init__(f"El intervalo {intervalo} no es válido, debe ser mayor que cero")

# ================================================================================
# ARCHIVO 3/3: tipo_medicamento_invalido.py
# Ruta: /home/maria-eva-modarelli/diseñosistemas/MediReminder/MediReminder/medi_reminder/excepciones/tipo_medicamento_invalido.py
# ================================================================================

class TipoMedicamentoInvalido(Exception):
    def __init__(self, tipo: str):
        super().__init__(f"El tipo de medicamento {tipo} no reconocido.")

