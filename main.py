from mini_tracker_oo.tracker_class import Tracker

mi_tracker = Tracker() # Instanciación del objeto
mi_tracker.iniciar_tarea("Estudio de POO")
mi_tracker.detener_tarea(3.0)
print(f"Total en el objeto Tracker: {mi_tracker.consultar_total()} h")