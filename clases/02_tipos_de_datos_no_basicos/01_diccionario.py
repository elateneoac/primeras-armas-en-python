# tipo de dato 'diccionario'
# estos tipos de datos se pueden definir en dos palabras: 'clave' y 'valor'.
# La idea del diccionario tradicional es que cada 'palabra' tiene un 'significado'.
# La idea del tipo de dato 'diccionario' es la misma: cada 'clave' tiene un 'valor'.

# para crear un 'diccionario' usamos las llaves: {}
compra_del_super = {
    'a-domicilio' : False,
    'supermercado' : 'coto',
    'manzana' : 3,
    'lacteos' : ['leche','yogurt','queso'],
    'cerveza' : {
        'marca':'imperial',
        'cantidad' : 20
    }
}

# operaciones
## [clave]: acceder a los elementos
compra_del_super['a-domicilio'] # False
compra_del_super['supermercado'] # 'coto'
compra_del_super['manzana'] # 3
compra_del_super['uva'] # KeyError: 'uva'

compra_del_super['lacteos'] # ['leche', 'yogurt', 'queso']
compra_del_super['cerveza'] # {'marca': 'imperial', 'cantidad': 20}

## [clave] = nuevo_valor: nuevo valor. aca podemos crear una nueva clave o reemplazar un valor existente
compra_del_super['peras'] = 5 # nuevo valor y nueva clave
compra_del_super['peras'] # 5

compra_del_super['peras'] = 0 # reemplazo valor en una clave que ya existe
compra_del_super['peras'] # 0

## del: borrar clave y valor
del compra_del_super['peras']
compra_del_super['peras'] # KeyError: 'peras'

# 💡 ¿VENTAJAS de los diccionarios? 💡
# Los diccionarios son útiles cuando hay muchos valores diferentes y esos valores pueden ser modificados o manipulados.
# Dado que el acceso a los elementos se hace por clave, no es necesario recordar una posición para cierto dato,
# lo que muchas veces cumple un objetivo fundamental:
#     ! hacer que el código sea más legible (y con esto menos propenso a errores). !

# ❓ ¿es lo mismo que 'json'? ❓
# en resumidas cuentas: cuando guardamos un diccionario en un archivo de texto, lo guardamos en un archivo '.json'.
# en la práctica: json = diccionario + algunos detalles.

# algunos ejemplos de como acceder al diccionario
## guardo valor en una variable y lo modifico desde ahí
lacteos = compra_del_super['lacteos']
lacteos[0] # 'leche'
lacteos.append('casancrem')
lacteos # ['leche', 'yogurt', 'queso', 'casancrem']

compra_del_super['lacteos'].append('queso-cheddar')
compra_del_super['lacteos'] # ['leche', 'yogurt', 'queso', 'casancrem', 'queso-cheddar']
lacteos # ['leche', 'yogurt', 'queso', 'casancrem', 'queso-cheddar']

## accedo a un diccionario dentro de un diccionario
compra_del_super['cerveza']['marca'] # 'imperial'

cerveza = compra_del_super['cerveza']
cerveza['marca'] # 'imperial'
