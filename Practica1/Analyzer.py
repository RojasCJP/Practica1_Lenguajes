from Practica1.loader import Loader
import re


class Analyzer:
    todos_comandos = []
    comando_original = ''
    loader = Loader(todos_comandos[1:])

    # constructor para analizador de comandos

    def __init__(self, todos_comandos, comando_original):
        self.todos_comandos = todos_comandos
        self.comando_original = comando_original

    # metodo para analizar y recuperar todas las palabras separadas
    # este metodo separa las palabras para que luego puedan utilizarse de manera aislada
    # guarda el comando original
    # cada palabra la mete en una matriz
    # y para obtener el lugar de cada palabra utilizamos un contador este se utiliza unicamente para imprimir
    # las condiciones utilizadas son para poder guardar el ultimo digito

    def separator(self):
        print('----------------------------------------------------------------------------------------------------------')
        print('ingrese el comando respectivo')
        comando = input()
        comando = re.sub(",", "", comando)
        comando = re.sub("'", "", comando)
        comando = re.sub('"', "", comando)
        comando_original = comando
        if comando.find(' ') == -1:
            self.todos_comandos.append(comando[0:len(comando)])
        else:
            self.todos_comandos.append(comando[0:(comando.find(' '))])
        while comando.find(' ') != -1:
            # print(comando.find(' '))
            contador = comando.find(' ')
            comando = comando[0:(comando.find(' '))] + '-' + comando[(comando.find(' ') + 1):len(comando) + 1]
            # print(comando)
            if comando.find(' ') == -1:
                self.todos_comandos.append(comando[contador + 1:len(comando)])
            else:
                self.todos_comandos.append(comando[contador + 1:(comando.find(' '))])
        return comando_original

    # este metodo selecciona la primera palabra y con forme a eso esto hara cierta accion

    def selector_first_word(self, operation):
        if operation == 'cargar':
            print('usted cargara el/los siguiente(s) archivo(s) json ' + str(self.todos_comandos[1:]))
            self.loader = Loader(self.todos_comandos[1:])
            self.loader.plus_dot_json()
            self.loader.load_file()
        elif operation == 'seleccionar':
            if self.todos_comandos[1] == '*':
                self.loader.print_file()
            else:
                contador = 0
                for element in self.todos_comandos:
                    if element == 'donde':
                        if type(self.todos_comandos[contador + 3]) == int:
                            condicion = int(self.todos_comandos[contador + 3])
                        else:
                            condicion = self.todos_comandos[contador + 3:]
                            condicion_str = ''
                            if len(condicion) >= 2:
                                for elemento in condicion:
                                    condicion_str += elemento + ' '
                                condicion_str = condicion_str[0:-1]
                            else:
                                for elemento in condicion:
                                    condicion_str += '' + elemento
                        self.loader.condition(self.todos_comandos[1:contador], self.todos_comandos[contador + 1], condicion_str)
                        return
                    else:
                        contador += 1
                self.loader.print_select(self.todos_comandos[1:])
        elif operation == 'maximo':
            self.loader.print_maximo(self.todos_comandos[1])
        elif operation == 'minimo':
            self.loader.print_minimo(self.todos_comandos[1])
        elif operation == 'suma':
            self.loader.print_total_suma(self.todos_comandos[1])
        elif operation == 'cuenta':
            self.loader.print_cuenta()
        elif operation == 'reportar':
            print('aqui creara un reporte html')
        elif operation == 'exit':
            print('adios wapo')
        else:
            print('no escogio ningun comando')

    # este metodo muestra todos los datos oportunos, como la matris de comandos y los comandos separados, ademas del mensaje original pero como queda al final

    def control(self):
        print('los numeros anteriormente mostrados son los espacios en los que hay un espacio en el codigo original')
        print(self.comando_original)
        for element in self.todos_comandos:
            print('elemento del array ' + element)
