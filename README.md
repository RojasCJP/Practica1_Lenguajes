# PRACTICA UNICA LENGUAJES FORMALES Y DE PROGRAMACION 

# MANUAL DE USUAIO

<p>Lo primero que tenemos que entender es que es este programa</p>
<p>Este programa es una version simplificada de SQL el cual hace consultas en archivos .json</p>
<p>El programa posee unos pocos comandos los cuales nos permiten hacer algunas consultas</p>
<p>Este es el listado de comandos:</p>

<p>Cargar: el comando cargar introduce n archivos .json a la memoria para luego utilizarlos en el programa para hacer las consultas que el usuario desee </p>
-La sintaxis para este comandos es: CARGAR archivo1.json, archivo2.json, ..., archivon.json

<p>Seleccionar: este comando nos permite seleccionar algun campo de nuestros archivos json o imprimirlos todos</p>
-La sintaxis para este comando es: SELECCIONAR *  o  SELECCIONAR campo_en_archivo_json

<p>Seleccionar-Donde: este comando nos permite seleccionar algun campo de nustros archivos json donde estos cumplan con una condicion dada</p>
-La sintaxis para este comando es: SELECCIONAR campo_en_archivo_json DONDE campo_en_archivo_json = condicion

<p>Maximo: este comando nos permite mostrar el mayor entre los atributos de nuestro archivo json siempre y cuando este atributo sea numerico</p>
-La sintaxis para este comando es: MAXIMO campo_numerico_en_archivo_json

<p>Minimo: este comando nos permite mostrar el menor entre los atributos de nuestro archivo json siempre y cuando este atributo sea numerico</p>
-La sintaxis para este comando es: MINIMO campo_numerico_en_archivo_json

<p>Suma: este comando nos permite mostrar la suma entre los atributos de una archivo json siempre y cuando este atributo sea numerico</p>
-La sintaxis para este comando es: SUMA campo_numeroco_en_archivo_json

<p>Cuenta: este comando nos permite mostrar la cantidad de registros json que hay en nustros archivos cargados, esta cuenta puede cambiar segun la cantidad de archivos json que esten cargados en nuestro programa</p>
-La sintaxis para este comando es: CUENTA

<p>Reportar: este comando nos permite crear una archivo html con la cantidad de registros que nosotros indiquemos, este los muestra en forma de una tabla</p>
-La sintaxis para este comando es: REPORTAR n
