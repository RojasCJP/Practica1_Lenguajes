from Practica1.analyzer import Analyzer

todos_comandos = []
comando_original = ''
analyzer = Analyzer(todos_comandos, comando_original)
switch = True
while switch:
    analyzer.todos_comandos = []
    analyzer.comando_original = ''
    comando_original = analyzer.separator()
    analyzer.selector_first_word(analyzer.todos_comandos[0])
    analyzer.control()
    if comando_original == 'exit':
        switch = False
