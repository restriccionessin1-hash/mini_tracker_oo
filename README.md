# Mini Tracker - Versión POO

Esta es una refactorización del rastreador de tiempo utilizando el paradigma de Programación Orientada a Objetos (POO).

## Beneficios del Encapsulamiento
A diferencia de la versión funcional, aquí el estado se encuentra **encapsulado** dentro de una clase llamada `Tracker`. Esto evita el uso de variables globales y permite que cada objeto mantenga su propio conteo independiente.

## Uso de la Clase
Para utilizar el rastreador, es necesario realizar la **instanciación** del objeto:

```python
from mini_tracker_oo import Tracker

mi_tracker = Tracker()
mi_tracker.iniciar_tarea("Mi Tarea")