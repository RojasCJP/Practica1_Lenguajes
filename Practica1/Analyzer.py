from Practica1.loader import Loader


class Analyzer:
    todos_comandos = []
    comando_original = ''

    def __init__(self, todos_comandos, comando_original):
        self.todos_comandos = todos_comandos
        self.comando_original = comando_original

    # metodo para analizar y recuperar todas las palabras separadas
    # este metodo separa las palabras para que luego puedan utilizarse de manera aislada
    # guarda el comando original
    # cada palabra la mete en una matriz
    # y para obtener el lugar de cada palabra utilizamos un contador
    # las condiciones utilizadas son para poder guardar el ultimo digito si en caso no existieran espacios en la palabra

    def separator(self):
        print('ingrese el comando respectivo')
        comando = input()
        comando_original = comando
        if comando.find(' ') == -1:
            self.todos_comandos.append(comando[0:len(comando)])
        else:
            self.todos_comandos.append(comando[0:(comando.find(' '))])
        while comando.find(' ') != -1:
            print(comando.find(' '))
            contador = comando.find(' ')
            comando = comando[0:(comando.find(' '))] + '-' + comando[(comando.find(' ') + 1):len(comando) + 1]
            print(comando)
            if comando.find(' ') == -1:
                self.todos_comandos.append(comando[contador + 1:len(comando)])
            else:
                self.todos_comandos.append(comando[contador + 1:(comando.find(' '))])
        return comando_original

    def selector_first_word(self, operation):
        if operation == 'cargar':
            print('usted cargara el/los siguiente(s) archivo(s) json ' + str(self.todos_comandos[1:]))
            loader = Loader(self.todos_comandos[1:])
            loader.plus_dot_json()
            loader.load_file()
            loader.print_file()
        elif operation == 'seleccionar':
            print('usted seleccionara un atributo de su archivo')
        elif operation == 'maximo':
            print('usted obtendra el maximo de un atributo')
        elif operation == 'minimo':
            print('usted obtendra el minimo de un atributo')
        elif operation == 'suma':
            print('usted sumara todos los valores de dicho atributo')
        elif operation == 'cuemta':
            print('mostrara cuantos registros hay')
        elif operation == 'reportar':
            print('aqui creara un reporte html')
        else:
            print('no escogio ningun comando')

    def control(self):
        print('los numeros anteriormente mostrados son los espacios en los que hay un espacio en el codigo original')
        print(self.comando_original)
        for element in self.todos_comandos:
            print('elemento del array ' + element)
