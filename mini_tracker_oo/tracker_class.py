class Tracker:
    def __init__(self):
        # El estado está encapsulado como atributo de instancia
        self.tiempo_total_acumulado = 0.0

    def iniciar_tarea(self, tarea):
        print(f"Iniciando tarea (POO): {tarea}")

    def detener_tarea(self, tiempo_trabajado):
        self.tiempo_total_acumulado += tiempo_trabajado
        print(f"Tarea detenida. Tiempo sumado al objeto.")

    def consultar_total(self):
        return self.tiempo_total_acumulado