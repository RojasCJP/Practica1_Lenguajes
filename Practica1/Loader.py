import json


class Loader:
    # constructor de loader

    def __init__(self, file_array):
        self.file_array = file_array
        self.todos_comandos = file_array
        self.data_json = []

    # este metodo pone el .json a todos las posiciones de la matriz de comandos si se utiliza el comando cargar
    # esto sirve para poder cargar los archivos sin necesidad de poner la extencion

    def plus_dot_json(self):
        contador_dot = 0
        for element in self.file_array:
            self.file_array[contador_dot] = self.file_array[contador_dot] + '.json'
            contador_dot += 1

    # este metodo carga el/los archivos .json para el programa y los guarda en un arreglo llamado data_json
    # este arreglo es un atributo de la clase asi que utiliza el prefijo self

    def load_file(self):
        contador = 0
        for file in self.file_array:
            with open(file) as f:
                self.data_json.append(json.load(f))
            contador += 1

    # este metodo ayuda a mostrar todos los registros cargados con el metodo anterior

    def print_file(self):
        print(type(self.data_json[0]['people']))
        registro_dentro_archivo = 1
        registro_json_numero = 0
        for registro_json in self.data_json:
            for person in registro_json['people']:
                print("registro " + str(registro_dentro_archivo) + " " + person['nombre'], person['apellido'],
                      person['edad'], person['estado'], sep=", ")
                registro_dentro_archivo += 1
            registro_json_numero += 1

    # este es el metodo para la condicion de

    def condition(self):
        contador = 0
        for element in self.todos_comandos:
            if element == 'DONDE':
                print('la condicion es: ' + element)
            else:
                contador += 1

    # imprimir la condicion
    def print_select(self, selection):
        print(type(self.data_json[0]['people']))
        registro_dentro_archivo = 1
        registro_json_numero = 0
        for registro_json in self.data_json:
            for person in registro_json['people']:
                print("registro " + str(registro_dentro_archivo))
                for element in selection:
                    print(element + ": " + person[element] + ", ", end=" ")
                registro_dentro_archivo += 1
                print()
            registro_json_numero += 1

# todo preparar los metodos por si estan vacios y tambien por si el nombre del archivo es invalido
