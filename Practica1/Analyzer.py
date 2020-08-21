# metodo para analizar y recuperar todas las palabras separadas
def separator():
    # ingresa el comando para la consulta
    comando = input('ingrese el comando respectivo')
    # guarda el comando general por si es necesario despues
    global comando_original
    comando_original = comando
    # inicia un array para meter todas las palabras por separado
    global todos_comandos
    todos_comandos = []
    todos_comandos.append(comando[0:(comando.find(' '))])
    while comando.find(' ') != -1:
        # muestra el espacio que ocupan los caracteres de espacio(' ')
        print(comando.find(' '))
        # cambia todos los espacios por guiones para que no pierda algunas propiedades utiles y para poder trabajar con el mensaje original
        comando = comando[0:(comando.find(' '))] + '-' + comando[(comando.find(' ') + 1):len(comando)]
        # anade el comando correspondiente al array
        todos_comandos.append(comando[comando.find(' '):(comando.find(' '))])


separator()
switch = True
while switch:
    separator()
    if comando_original == 'exit':
        switch=False

print('los numeros anteriormente mostrados son los espacios en los que hay un espacio en el codigo original')
print(comando_original)
for element in todos_comandos:
    print(element)
