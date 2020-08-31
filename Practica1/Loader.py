import json
import os


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
            self.file_array[contador_dot] = self.file_array[contador_dot]
            contador_dot += 1

    # este metodo carga el/los archivos .json para el programa y los guarda en un arreglo llamado data_json
    # este arreglo es un atributo de la clase asi que utiliza el prefijo self

    def load_file(self):
        contador = 0
        for file in self.file_array:
            if os.path.isfile(file):
                with open(file) as f:
                    self.data_json.append(json.load(f))
                contador += 1
            else:
                print('el archivo que intenta agregar no existe')

    # este metodo ayuda a mostrar todos los registros cargados con el metodo anterior

    def print_file(self):
        print(type(self.data_json[0]))
        registro_dentro_archivo = 1
        registro_json_numero = 0
        for registro_json in self.data_json:
            for element in registro_json:
                print(element['nombre'], element['edad'], element['activo'], element['promedio'], sep=", ")
                registro_dentro_archivo += 1
                registro_json_numero += 1

    # este es el metodo para la condicion de

    def condition(self, selection, campo_validador, condicion):
        try:
            print(type(self.data_json[0]))
            registro_dentro_archivo = 1
            registro_json_numero = 0
            for registro_json in self.data_json:
                for person in registro_json:
                    for element in selection:
                        if (str(person[campo_validador])) == condicion:
                            print(element + ": " + str(person[element]) + ", ", end=" ")
                    registro_dentro_archivo += 1
                registro_json_numero += 1
                print()
        except:
            print('El registro que usted solicito no se encuentra')

    # imprimir la condicion

    def print_select(self, selection):
        print(type(self.data_json[0]))
        registro_dentro_archivo = 1
        registro_json_numero = 0
        for registro_json in self.data_json:
            try:
                for person in registro_json:
                    for element in selection:
                       print(element + ": " + str(person[element]) + ", ", end=" ")
                    registro_dentro_archivo += 1
                    print()
            except:
                print('El registro que pidio no se ecuentra')
            registro_json_numero += 1

    def print_minimo(self, selection):
        minimo = float('inf')

        for registro_json in self.data_json:
            for person in registro_json:
                if type(person[selection]) == int or float:
                    if minimo >= person[selection]:
                        minimo = person[selection]
                else:
                    print('el dato que usted pide no es un numero')
                    return
        print(minimo)

    def print_maximo(self, selection):
        maximo = float('-inf')
        for registro_json in self.data_json:
            for person in registro_json:
                if type(person[selection]) == int or float:
                    if maximo <= person[selection]:
                        maximo = person[selection]
                else:
                    print('el dato que usted pide no es un numero')
                    return
        print(maximo)

    def print_total_suma(self, selection):
        suma = 0
        for registro_json in self.data_json:
            for person in registro_json:
                if type(person[selection]) == int or float:
                    suma += person[selection]
                else:
                    print('el dato que usted pide no es un numero')
                    return
        print(suma)

    def print_cuenta(self):
        cuenta = 0
        for element in self.data_json:
            cuenta += len(element)
        print(cuenta)

# todo hacer el reporte
