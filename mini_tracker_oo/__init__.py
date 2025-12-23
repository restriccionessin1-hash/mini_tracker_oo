class Tracker:
    def __init__(self):
        # El estado es un atributo de instancia (Encapsulamiento)
        self.tiempo_total_acumulado = 0.0

    def iniciar_tarea(self, tarea):
        print(f"Iniciando tarea (POO): {tarea}")

    def detener_tarea(self, tiempo_trabajado):
        # Se modifica el atributo propio del objeto
        self.tiempo_total_acumulado += tiempo_trabajado
        print(f"Tarea detenida. Tiempo guardado en la instancia.")

    def consultar_total(self):
        return self.tiempo_total_acumulado
