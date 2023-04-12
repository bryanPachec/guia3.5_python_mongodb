from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Repositorio.RepositorioMateria import RepositorioMateria

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMaterias():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       self.repositorioMateria = RepositorioMateria()
       print("Creando ControladorMaterias")


   def index(self):
       print("Listar todas las materias")
       return self.repositorioMateria.findAll()



   def create(self, laMateria):
       print("Crear una materia")
       nuevaMateria = Materia(laMateria)
       return self.repositorioMateria.save(nuevaMateria)



   def show(self, id):
       print("Mostrando la materia con id ", id)
       laMateria =  Materia(self.repositorioMateria.findById(id))
       return laMateria.__dict__


   def update(self, id, laMateria):
       print("Actualizando materia con id ", id)
       materiaActual = Materia(self.repositorioMateria.findById(id))
       materiaActual.nombre = laMateria["Nombre"]
       materiaActual.creditos = laMateria["Creditos"]
       return self.repositorioMateria.save(materiaActual)

   def delete(self, id):
       print("Elimiando materia con id ", id)
       return self.repositorioMateria.delete(id)

