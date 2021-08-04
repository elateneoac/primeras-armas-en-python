# tipo de dato 'diccionario'
# estos tipos de datos se pueden definir en dos palabras: 'clave' y 'valor'.
# La idea del diccionario tradicional es que cada 'palabra' tiene un 'significado'.
# La idea del tipo de dato 'diccionario' es la misma: cada 'clave' tiene un 'valor'.

compra_del_super = {
    'a-domicilio' : False, # booleano
    'supermercado' : 'coto', # string
    'manzana' : 3, # numero
    'lacteos' : ['leche','yogurt','queso'], # lista
    'cerveza' : {'marca':'imperial', 'cantidad' : 20} # diccionario
}

compra_del_super['a-domicilio'] # False
compra_del_super['supermercado'] # 'coto'
compra_del_super['manzana'] # 3
compra_del_super['lacteos'] # ['leche', 'yogurt', 'queso']
compra_del_super['cerveza'] # {'marca': 'imperial', 'cantidad': 20}
compra_del_super['cerveza']['marca'] # 'imperial'