# tipo de dato 'diccionario'
# estos tipos de datos se pueden definir en dos palabras: 'clave' y 'valor'.
# La idea del diccionario tradicional es que cada 'palabra' tiene un 'significado'.
# La idea del tipo de dato 'diccionario' es la misma: cada 'clave' tiene un 'valor'.

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


compra_del_super['a-domicilio'] # False
compra_del_super['supermercado'] # 'coto'
compra_del_super['manzana'] # 3

compra_del_super['lacteos'] # ['leche', 'yogurt', 'queso']
compra_del_super['cerveza'] # {'marca': 'imperial', 'cantidad': 20}

# lista
lacteos = compra_del_super['lacteos']
lacteos[0]
lacteos.append('casancrem')

compra_del_super['lacteos'].append('queso-cheddar')

# diccionario
cerveza = compra_del_super['cerveza']
cerveza['marca']

compra_del_super['cerveza']['marca'] # 'imperial'

import json

un_string = "hola"
un_string_con_saltos_de_linea = """
hola
como
va"""

string_compra_del_super = """{
    "a-domicilio" : 0,
    "supermercado" : "coto",
    "manzana" : 3,
    "lacteos" : ["leche',"yogurt","queso"],
    "cerveza" : {
        "marca" : "imperial",
        "cantidad" : 20
    }
}"""

string_compra_del_super = "{\"saludo\":\"hola\"}"

# guardo string de diccionario en una variable tipo 'json'
json_compra_del_super = json.loads(string_compra_del_super)

# poder hacer consas con la variable tipo json (con 'json_compra_del_super')

# guardo la variable tipo 'json' en un string
salida = json.dump(json_compra_del_super)

noticias = json.load('archivo.json')
noticias

# csv