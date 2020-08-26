import json


class Loader:
    file_array = []

    def __init__(self, file_array):
        self.file_array = file_array
        self.data_json = []

    def plus_dot_json(self):
        contador_dot = 0
        for element in self.file_array:
            self.file_array[contador_dot] = self.file_array[contador_dot] + '.json'
            contador_dot += 1

    def load_file(self):
        contador = 0
        for file in self.file_array:
            with open(file) as f:
                self.data_json.append(json.load(f))
            contador = contador + 1

    def print_file(self):
        print(type(self.data_json[0]['people']))
        registro_dentro_archivo = 1
        registro_json_numero = 0
        for registro_json in self.data_json:
            for person in self.data_json[registro_json_numero]['people']:
                print("registro " + str(registro_dentro_archivo) + " " + person['nombre'], person['apellido'], person['edad'], person['estado'], sep=", ")
                registro_dentro_archivo += 1
            registro_json_numero += 1
