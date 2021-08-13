# lo abrimos sin with como si fuese un txt
archivo_notis = open('data/notis_20210803.csv')
archivo_notis.readline()
archivo_notis.close()

# usando lo que ya sabemos
archivo_notis = open('data/notis_20210803.csv')
filas = archivo_notis.readlines()
archivo_notis.close()

# veo cuantas filas tiene
len(filas)

# estilo tradi
for fila in filas:
    valores = fila.split(',',4)

    diario = valores[0]
    seccion = valores[1]
    fecha = valores[2]
    titulo = valores[3]
    texto = valores[4]

    if 'Macri' in titulo:
        print(diario, seccion, titulo)

# estilo con pythonista
for linea in filas:
    diario, seccion, fecha, titulo, texto = linea.split(',',4)

    if 'Macri' in titulo:
        diario
