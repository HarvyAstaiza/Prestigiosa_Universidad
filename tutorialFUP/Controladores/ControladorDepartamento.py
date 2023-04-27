from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorDepartamento():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioDepartamento.findAll()

    def create(self, infoDepartamento):
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__

    def update(self, id, infoDepartamento):
        DepartamentoActual = Departamento(self.repositorioDepartamento.findById(id))
        DepartamentoActual.nombre = infoDepartamento["nombre"]
        DepartamentoActual.descripcion = infoDepartamento["descripcion"]
        return self.repositorioDepartamento.save(DepartamentoActual)

    def delete(self, id):
        return self.repositorioDepartamento.delete(id)
