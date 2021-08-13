# txt
# modo:
# 'r' = 'abro para lectura'
# 't' = 'es un archivo de texto'
# 'b' = 'abro en modo binario'
archivo = open('data/archivo.txt', 'rt')
contenido = archivo.read()
archivo.close()

contenido = ''
with open('data/archivo.txt', 'rt') as a:
    contenido = a.read()

# leo linea
contenido = ''
archivo = open('data/archivo.txt', 'rt')
contenido = archivo.readline()
archivo.close()

# leer todas las lineas y guardar en una lista
lineas = ''
archivo = open('data/archivo.txt', 'rt')
lineas = archivo.readlines()
archivo.close()

# algunas operaciones
lineas[0]
lineas[-1]
len(lineas)