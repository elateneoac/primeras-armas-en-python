# 3. listas
# las listas son un tipo de dato que sirven para guardar colecciones ordenadas,
# es decir, que cada elemento tiene una posición según un criterio.

# 3.1. creando una lista
# para crear una variable tipo 'lista' usamos los corchetes []
docena = [1,2,3,4,5,6,7,8,9,10,11,12]
paises = ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']
popurri = [2021, 'Argentina', 'Agosto', 3.14] # los elementos de la lista pueden ser de cualquier tipo

docena # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
paises # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']
popurri # [2021, 'Argentina', 'Agosto', 3.14]

# 3.2.1. acceder a los elementos:
# ANTES QUE NADA: en casi todos los lenguajes:
# EL PRIMER ELEMENTO ESTÁ EN LA POSICIÓN CERO. Esto es diferente a R,
# donde el primer elemento está en la posición 1.
#
# Python tiene una MUY práctica sintaxis para acceder a elementos:

# primer elemento
paises[0] # 'Argentina'

# último elemento
paises[-1] # 'Paraguay'

# del 1ero hasta el 3ero inclusive
paises[:3] # ['Argentina', 'Uruguay', 'Chile']

# del 3ero hasta el último
paises[2:] # ['Chile', 'Bolivia', 'Paraguay']

# del 3do al 4to
paises[2:4] # ['Chile', 'Bolivia']

# del 2do al último
paises[1:-1] # ['Uruguay', 'Chile', 'Bolivia']


# 3.2. operaciones
# en las listas operar con variables de cualquier tipo.

# 3.2.1. [i]=: reemplazar elemento en la posición 'i'.
popurri[-1] = 'Sábado' # reemplazo el último elemento por 'Sábado'
popurri # [2021, 'Argentina', 'Agosto', 'Sábado']

# 3.2.1 +: concatenar dos listas
paises_y_docena = paises + docena
paises_y_docena # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 3.2.2. append(): agregar un nuevo elemento.
popurri.append('Soleado')
popurri # [2021, 'Argentina', 'Agosto', 'Sábado', 'Soleado']

# 3.2.2. insert(): agregar un nuevo elemento en una determinada posición.
popurri.insert(0, 'Nublado') # agrego 'Colombia' primero (posición cero)
popurri.insert(-1, 1900) # agrego 'Ecuador' anteúltimo
popurri # ['Nublado', 2021, 'Argentina', 'Agosto', 'Sábado', 1900, 'Soleado']

# 3.2.2. index(): posición de un elemento
paises.index('Chile') # 2
paises.index('Córdoba') # ValueError: 'Córdoba' is not in list

# 3.2.2. remove(), del: borrar elemento
# Al borrar un elemento no se genera un hueco.
# Los siguientes elementos se moverán para llenar el vacío.
# Si hubiera más de una aparición de un valor, 'remove()' sólo saca la primera aparición.
popurri.remove('Sábado')
popurri.remove('Martes') # ValueError: list.remove(x): x not in list
del popurri[1] # elimino el segundo
del popurri[99] # IndexError: list assignment index out of range
popurri # ['Nublado', 'Argentina', 'Agosto', 1900, 'Soleado']

# 3.2.2. len(): cantidad de elementos
len(paises) # 5

# 3.2.2. in, not in: chequear si un elemento 'está' o 'no está'
'Argentina' in paises # True
'Canada' in paises # False
'México' not in paises # True

# 3.2.2. *: repetir una lista
paises * 2 # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay', 'Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']


# 3.3. recorrer -o iterar- las listas
# Siguiendo la sintaxis simplistas para acceder a las listas,
# Python tiene una sintaxis práctica y minimalista para iterar lista:

# 3.3.1. recorrer estilo tradicional
paises_iterados_con_for = []
for pais in paises:
    paises_iterados_con_for.append(pais)
paises_iterados_con_for # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']

# # 3.3.1. recorrer estilo tradicional con while:
# lo mismo de arriba pero usando 'while'
paises_iterados_con_while = []
i = 0
while i < len(paises):
    pais = paises[i]
    paises_iterados_con_while.append(pais)
    i += 1
paises_iterados_con_while # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']

# 3.3.1. recorrer estilo python
# esta forma es la más pythonista de todas: en una sola línea podes:
# - iterar
# - filtrar
# - operar
# - iterar anidadamente (for dentro de un for)
# - guardar resultado en una nueva lista
paises_iterados_con_for_pythonista = [pais for pais in paises]
paises_iterados_con_for_pythonista # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']

# 3.3.1. iterar, filtrar y modificar: hacer lo mismo en las 3 versiones.

# estilo tradi con for
paises_iterados_con_for = []
for pais in paises:
    if 'a' not in pais:
        continue # si el pais no contiene la letra 'a', entonces no lo guardo.
    paises_iterados_con_for.append(pais.upper()) # lo guardo en mayúscula
paises_iterados_con_for # ['ARGENTINA', 'URUGUAY', 'BOLIVIA', 'PARAGUAY']

# estilo tradi con while
paises_iterados_con_while = []
i = 0
while i < len(paises):
    pais = paises[i]
    if 'a' not in pais:
        i += 1 # tengo que avanzar de paso aca porque después de 'continue' se vuelve al principio
        continue # si el pais no contiene la letra 'a', entonces no lo guardo.
    paises_iterados_con_while.append(pais.upper()) # lo guardo en mayúscula
    i += 1

paises_iterados_con_while # ['ARGENTINA', 'URUGUAY', 'BOLIVIA', 'PARAGUAY']

# estilo pythonista
paises_iterados_con_while = [pais.upper() for pais in paises if 'a' in pais]
paises_iterados_con_while # ['ARGENTINA', 'URUGUAY', 'BOLIVIA', 'PARAGUAY']

# cada uno de los 3 estilos tienen sus pro y sus contras.
# la recomendación es que intenten siempre primero con el 'estilo pythonista',
# y si con ese no sale, vayan con el 'estilo tradi con for'. En la práctica,
# este último es el que más se usa porque soluciona casi cualquier tipo de iteración,
# sin perder calidad en el código.