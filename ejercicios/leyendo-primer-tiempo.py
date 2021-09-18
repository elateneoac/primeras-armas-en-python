import json

c1 = open('/home/manu/repos/elateneoac/primeras-armas-en-python/data/primertiempo-c01.txt', 'rt')

# leo linea 1
parrafo1 = c1.readline() # le dejo el salto de linea final

# leo linea 2
parrafo2 = c1.readline().strip() # uso strip para sacarle el salto de linea al final

# leo linea 3
parrafo3 = c1.readline().strip()

# cierro archivo
c1.close()

# cantidad de letras en el parrafo 1
len(parrafo1)

# cantidad de letras en el parrafo 1 sin el salto de linea
cantidad_de_letras_en_parrafo_1 = len(parrafo1.strip())

# separo el parrafo 2 en palabras
oraciones_2 = parrafo2.split('.') # 'split' me genera una lista

# cantidad de oraciones en el parrafo 2
cantidad_de_oraciones_en_parrafo_2 = len(oraciones_2)

# cantidad de letras en la oracion 4 del parrafo 2
oracion_4_del_parrafo2 = oraciones_2[3]
cantidad_de_letras_de_la_oracion3_del_parrafo_2 = len(oracion_4_del_parrafo2)

# cantidad de letras en la anteultima oracion
len(oraciones_2[-2])

# json a guardar
datos = {
    'cantidad_de_letras_en_parrafo1' : cantidad_de_letras_en_parrafo_1,
    'cantidad_de_oraciones_en_parrafo2' : cantidad_de_oraciones_en_parrafo_2,
    'cantidad_de_letras_de_la_oracion3_del_parrafo_2' : cantidad_de_letras_de_la_oracion3_del_parrafo_2
}

# guardo los datos
archivo_datos = open('/home/manu/repos/elateneoac/primeras-armas-en-python/data/datos-primertiempo-c01.json', 'wt')

json.dump(datos, archivo_datos)

archivo_datos.close()

# 'info-capitulo1.csv' un csv q tenga: id_parrafo, cantidad_letras, cantidad_palabras, cantidad_oraciones

c1 = open('/home/manu/repos/elateneoac/primeras-armas-en-python/data/primertiempo-c01.txt', 'rt')

parrafos = c1.readlines()

filas = []
id_parrafo = 0
for parrafo in parrafos:

    parrafo = parrafo.strip() # volar basura de atras y adelante

    cantidad_de_letras = len(parrafo) # cuento las letras

    palabras = parrafo.split(' ') # separo en palabras
    cantidad_de_palabras = len(palabras) # y cuento las palabras

    oraciones = parrafo.split('.') # separo en oraciones
    cantidad_de_oraciones = len(oraciones) # y cuento las oraciones

    # armo la fila
    fila = (id_parrafo, cantidad_de_letras, cantidad_de_palabras, cantidad_de_oraciones)
    filas.append(fila) # sumo la fila a las filas

    id_parrafo += 1 # aumento el contador

csv_datos_c1 = open('/home/manu/repos/elateneoac/primeras-armas-en-python/data/datos-primertiempo-c01.csv', 'wt')

csv_datos_c1.write('id_parrafo,cantidad_de_letras,cantidad_de_palabras,cantidad_de_oraciones\n')
csv_datos_c1.flush()

for fila in filas:
    id = str(fila[0])
    letras = str(fila[1])
    palabras = str(fila[2])
    oraciones = str(fila[3])

    csv_datos_c1.write(id + ',' + letras + ','+ palabras + ',' + oraciones + '\n')

csv_datos_c1.close()