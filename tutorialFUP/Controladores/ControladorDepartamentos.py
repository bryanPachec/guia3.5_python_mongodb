from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorio.RepositorioDepartamento import RepositorioDepartamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorDepartamentos():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       self.repositorioDepartamento = RepositorioDepartamento()
       print("Creando ControladorDepartameto")


   def index(self):
       print("Listar todos los departamentos")
       return self.repositorioDepartamentos.findAll()

   def create(self, Eldepartamento):
       print("Crear un departamento")
       nuevoDepartamento = Departamento(Eldepartamento)
       return self.repositorioDepartamento.save(nuevoDepartamento)


   def show(self, id):
       print("Mostrando el departamento con id ", id)
       elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
       return  elDepartamento.__dict__


   def update(self, id, Eldepartamento):
       print("Actualizando depertamento con id ", id)
       departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
       departamentoActual.nombre = Eldepartamento["nombre"]
       return self.repositorioDepartamento.save(departamentoActual)



   def delete(self, id):
       print("Elimiando departamento con id ", id)
       return self.repositorioDepartamento.delete(id)

