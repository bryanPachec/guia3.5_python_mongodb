from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMaterias import ControladorMaterias
from Controladores.ControladorDepartamentos import ControladorDepartamentos
from Controladores.ControladorInscripciones import ControladorInscripcion

app = Flask(__name__)
"""
Los cors permiten que se puedan hacer pruebas al
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

miControladorEstudiante = ControladorEstudiante()
miControladorMaterias = ControladorMaterias()
miControladorDepartamentos = ControladorDepartamentos()
miControladorInscripciones = ControladorInscripcion()

"""
Servicio que el servidor ofrecerá, y este consiste en
retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""

@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
   json = miControladorEstudiante.index()
   return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
   data = request.get_json()
   json = miControladorEstudiante.create(data)
   return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
   json = miControladorEstudiante.show(id)
   return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
   data = request.get_json()
   json = miControladorEstudiante.update(id, data)
   return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
   json = miControladorEstudiante.delete(id)
   return jsonify(json)


@app.route("/", methods=['GET'])
def test():
   json = {}
   json["message"] = "Server running ..."
   return jsonify(json)


""" Contolador materia"""


@app.route("/materias", methods=['GET'])
def getMaterias():
   json = miControladorMaterias.index()
   return jsonify(json)


@app.route("/materias", methods=['POST'])
def crearMaterias():
   data = request.get_json()
   json = miControladorMaterias.create(data)
   return jsonify(json)


@app.route("/materias/<string:id>", methods=['GET'])
def getMateria(id):
   json = miControladorMaterias.show(id)
   return jsonify(json)


@app.route("/materias/<string:id>", methods=['PUT'])
def modificarMaterias(id):
   data = request.get_json()
   json = miControladorMaterias.update(id, data)
   return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarMaterias(id):
   json = miControladorMaterias.delete(id)
   return jsonify(json)



"""
Funcion leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""

""""DEPARTAMENTOS"""

@app.route("/departamentos", methods=['GET'])
def getDepartamentos():
   json = miControladorDepartamentos.index()
   return jsonify(json)


@app.route("/departamentos", methods=['POST'])
def crearDepartamentos():
   data = request.get_json()
   json = miControladorDepartamentos.create(data)
   return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
   json = miControladorDepartamentos.show(id)
   return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['PUT'])
def modificarDepartamentos(id):
   data = request.get_json()
   json = miControladorDepartamentos.update(id, data)
   return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
   json = miControladorDepartamentos.delete(id)
   return jsonify(json)


""""INSCRIPCIÓN"""

@app.route("/inscripcion", methods=['GET'])
def getInscripcion():
   json = miControladorInscripciones.index()
   return jsonify(json)


@app.route("/inscripcion", methods=['POST'])
def crearInscripcion():
   data = request.get_json()
   json = miControladorInscripciones.create(data)
   return jsonify(json)


@app.route("/inscripcion/<string:id>", methods=['GET'])
def getInscripcion1(id):
   json = miControladorInscripciones.show(id)
   return jsonify(json)


@app.route("/inscripcion/<string:id>", methods=['PUT'])
def modificarInscripcion(id):
   data = request.get_json()
   json = miControladorInscripciones.update(id, data)
   return jsonify(json)


@app.route("/inscripcion/<string:id>", methods=['DELETE'])
def eliminarInscripcion(id):
   json = miControladorInscripciones.delete(id)
   return jsonify(json)



def loadFileConfig():
   with open('config.json') as f:
       data = json.load(f)
   return data

if __name__ == '__main__':
   dataConfig = loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
   print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
   """
   Se crea la instancia del servidor con la url del backend y puerto especificado
   en el archivo de configuración.
   """
   serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])