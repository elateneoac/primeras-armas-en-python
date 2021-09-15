# archivo
# desde Python más de una vez vamos a tener que abrir un archivo guardado en nuestras compus.
# en la jerga, usamos 'levantar' para referirnos a: leer un archivo del disco duro y guardarlo en memoria ram.
# de ahora en más, 'levantar' = 'cargar archivo en el programa, desde nuestra compu'

# abrir un archivo
para_leer = open('data/para_leer.txt', 'rt')    
para_escribir = open('data/para_escribir.txt', 'wt')

# usamos los archivos: leemos uno y escribimos el otro.
# escribimos
contenido_para_leer = para_leer.read()

import datetime
contenido_a_escribir = datetime.datetime.now().strftime('escribimos año %Y, mes %m, día %d') # rescatamos la fecha de hoy
contenido_a_escribir += '\n' # le agrego el 'salto de linea'
contenido_a_escribir # 'escribimos año 2021, mes 08, día 19\n'

para_escribir.write(contenido_a_escribir)
#  💡 IMPORTANTE  💡 : para ver impactado lo que escribimos, tenemos que FLUSHEAR el contenido.
# 'hacer flush' = 'guardar en el disco duro lo que tenemos guardado en memoria ram'
# para flushear: llamados al método, o cerramos el archivo.
para_escribir.flush()

# leemos
contenido_leido = para_leer.read()
contenido_leido # 'hola como va todo bien?\notra linea con info\nultima linea con data\ncuarta linea'

#  💡 IMPORTANTE 💡 : si volvemos a hacer '.read()', nos devuelve vacio: esto es porque 'para_leer' guarda la posición de la última letra que leyo.
# como leyó todas las letras, entonces la posición es el final del archivo. No queda más nada para leer.
contenido_leido = para_leer.read()
contenido_leido # ''


# cerramos los archivos
#  💡 IMPORTANTE 💡 : los archivos SE TIENEN QUE CERRAR. sino pueden haber errores.
para_leer.close()
para_escribir.close()
