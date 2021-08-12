# listas
# las listas son un tipo de dato que sirven para guardar colecciones ordenadas,
# es decir, que cada elemento tiene una posición según un criterio.

# creando una lista
# para crear una variable tipo 'lista' usamos los corchetes []
docena = [1,2,3,4,5,6,7,8,9,10,11,12]
paises = ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']
popurri = [2021, 'Argentina', 'Agosto', 3.14] # los elementos de la lista pueden ser de cualquier tipo

docena # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
paises # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']
popurri # [2021, 'Argentina', 'Agosto', 3.14]

# acceder a los elementos:
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


# operaciones
# en las listas operar con variables de cualquier tipo.

# [i]=: reemplazar elemento en la posición 'i'.
popurri[-1] = 'Sábado' # reemplazo el último elemento por 'Sábado'
popurri # [2021, 'Argentina', 'Agosto', 'Sábado']

# +: concatenar dos listas
paises_y_docena = paises + docena
paises_y_docena # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# append(): agregar un nuevo elemento.
popurri.append('Soleado')
popurri # [2021, 'Argentina', 'Agosto', 'Sábado', 'Soleado']

# insert(): agregar un nuevo elemento en una determinada posición.
popurri.insert(0, 'Nublado') # agrego 'Colombia' primero (posición cero)
popurri.insert(-1, 1900) # agrego 'Ecuador' anteúltimo
popurri # ['Nublado', 2021, 'Argentina', 'Agosto', 'Sábado', 1900, 'Soleado']

# index(): posición de un elemento
paises.index('Chile') # 2
paises.index('Córdoba') # ValueError: 'Córdoba' is not in list

# remove(), del: borrar elemento
# Al borrar un elemento no se genera un hueco.
# Los siguientes elementos se moverán para llenar el vacío.
# Si hubiera más de una aparición de un valor, 'remove()' sólo saca la primera aparición.
popurri.remove('Sábado')
popurri.remove('Martes') # ValueError: list.remove(x): x not in list
del popurri[1] # elimino el segundo
del popurri[99] # IndexError: list assignment index out of range
popurri # ['Nublado', 'Argentina', 'Agosto', 1900, 'Soleado']

# len(): cantidad de elementos
len(paises) # 5

# in, not in: chequear si un elemento 'está' o 'no está'
'Argentina' in paises # True
'Canada' in paises # False
'México' not in paises # True

# *: repetir una lista
paises * 2 # ['Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay', 'Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']