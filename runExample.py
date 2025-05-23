import pyglet
import importlib

module_name = "examples.simpleVisual"  # Replace with your module name
object_name = "showSimulation"  # Replace with the object name you want to import

simpleVisual = importlib.import_module(module_name)
showSim = getattr(simpleVisual, "showSimulation")

aShow = showSim()

pyglet.app.run()
