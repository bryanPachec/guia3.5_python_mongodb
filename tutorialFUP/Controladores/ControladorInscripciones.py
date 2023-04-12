from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Repositorio.RepositorioInscripcion import RepositorioInscripcion

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInscripcion():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       self.repositorioInscripcion = RepositorioInscripcion()
       print("Creando ControladorInscripcion")


   def index(self):
       print("Listar todos los inscripción")
       return self.repositorioInscripcion.findAll()


   def create(self, unaInscripcion):
       print("Nueva Inscripción")
       nuevaIncripcion = Inscripcion(unaInscripcion)
       return self.repositorioInscripcion.save(nuevaIncripcion)


   def show(self, id):
       print("Mostrando una inscripcion con id ", id)
       mostrarInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
       return mostrarInscripcion.__dict__


   def update(self, id, unaInscripcion):
       print("Actualizando inscripción con id ", id)
       inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
       inscripcionActual.año = unaInscripcion["Año"]
       inscripcionActual.semestre = unaInscripcion["Semestre"]
       inscripcionActual.nota_final = unaInscripcion["Nota_Final"]
       return self.repositorioInscripcion.save(inscripcionActual)


   def delete(self, id):
       print("Elimiando inscripción con id ", id)
       return self.repositorioInscripcion.delete(id)

