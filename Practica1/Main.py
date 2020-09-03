from Analyzer import Analyzer
from reporte import Reporte

comando_para_guardar = ''
todos_comandos = []
comando_original = ''
analyzer = Analyzer(todos_comandos, comando_original)
switch = True
while switch:
    analyzer.todos_comandos = []
    analyzer.comando_original = ''
    comando_original = analyzer.separator()
    analyzer.selector_first_word(analyzer.todos_comandos[0])
    for element in analyzer.todos_comandos:
        comando_para_guardar += element + ' '
        #     todo hay que guardar todos los comandos, concatenarlos y guardarlos despues
    comando_para_guardar = ''
    if comando_original == 'exit':
        switch = False
    elif analyzer.todos_comandos[0] == 'reportar':
        # todo hacer el registro, creo que se puede hacer con plantilla
        cuenta = 0
        for element in analyzer.loader.data_json:
            cuenta += len(element)
        try:
            numero_registros = int(comando_original[8:])
            reporte = Reporte(numero_registros, cuenta, analyzer.loader.file_array)
        except:
            if (comando_original[9:10]) == '*':
                reporte = Reporte(cuenta, cuenta, analyzer.loader.file_array)
            else:
                print('el dato que ingreso no es un numero')
