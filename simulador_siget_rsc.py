import time
import random

class ProcesoSIGET:
    def __init__(self, nombre, prioridad, tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_restante = tiempo_ejecucion
        self.estado = "Nuevo"  # [1]
        print(f"[*] Proceso {self.nombre} creado en estado: {self.estado}")

    def actualizar_estado(self, nuevo_estado):
        # Muestra la transición clara de estados para el informe técnico [2]
        print(f"    [{self.nombre}] TRANSICIÓN: {self.estado} -> {nuevo_estado}")
        self.estado = nuevo_estado

# Simulación mejorada del Planificador
def planificador_siget_avanzado(procesos):
    print("\n--- Iniciando Planificación de CPU (SIGET) ---")
    
    # Todos los procesos pasan a 'Listo' al ser admitidos en la cola [1]
    for p in procesos:
        p.actualizar_estado("Listo")

    # Ordenar por prioridad (Prioridad 1 es emergencia) [4]
    procesos.sort(key=lambda p: p.prioridad)

    while procesos:
        p = procesos.pop(0)
        
        # Paso a 'En ejecución' [1]
        p.actualizar_estado("En ejecución")
        
        # Simulación de latencia por Arquitectura Von Neumann [3]
        # (Las instrucciones y datos compiten por el bus, generando retrasos)
        print(f"      (Ejecutando ráfaga de CPU para {p.nombre}...)")
        time.sleep(1) 
        p.tiempo_restante -= 1

        # Simulación de estado 'Bloqueado' [1]
        # Por ejemplo, esperando datos de un sensor de tráfico o entrada/salida
        if random.random() < 0.3 and p.tiempo_restante > 0:
            p.actualizar_estado("Bloqueado")
            print(f"      [!] {p.nombre} esperando recurso (E/S)...")
            time.sleep(1)
            p.actualizar_estado("Listo")
            procesos.append(p) # Regresa a la cola
            continue

        if p.tiempo_restante > 0:
            p.actualizar_estado("Listo")
            procesos.append(p)
        else:
            # Paso final a 'Terminado' [1]
            p.actualizar_estado("Terminado")

# Definición de tareas del SIGET
tareas = [
    ProcesoSIGET("Rutina_Vial_01", 3, 2),
    ProcesoSIGET("Emergencia_Ambulancia", 1, 1), # Alta prioridad [4]
    ProcesoSIGET("Semaforo_Inteligente", 2, 2)
]

planificador_siget_avanzado(tareas)