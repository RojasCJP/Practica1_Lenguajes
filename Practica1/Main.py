from Practica1.analyzer import Analyzer

todos_comandos = []
comando_original = ''
analyzer = Analyzer(todos_comandos, comando_original)
switch = True
while switch:
    comando_original = analyzer.separator()
    analyzer.selector_first_word()
    analyzer.control()
    if comando_original == 'exit':
        switch = False
