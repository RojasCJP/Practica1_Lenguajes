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

    def selector_first_word(operation):
        if operation == 'CARGAR':
            print('usted cargara archivos json')
        if operation == 'SELECCIONAR':
            print('usted seleccionara un atributo de su archivo')
        if operation == 'MAXIMO':
            print('usted obtendra el maximo de un atributo')
        if operation == 'MINIMO':
            print('usted obtendra el minimo de un atributo')
        if operation == 'SUMA':
            print('usted sumara todos los valores de dicho atributo')
        if operation == 'CUENTA':
            print('mostrara cuantos registros hay')
        if operation == 'REPORTAR':
            print('aqui creara un reporte html')

    def control(self):
        print('los numeros anteriormente mostrados son los espacios en los que hay un espacio en el codigo original')
        print(self.comando_original)
        for element in self.todos_comandos:
            print('elemento del array ' + element)
