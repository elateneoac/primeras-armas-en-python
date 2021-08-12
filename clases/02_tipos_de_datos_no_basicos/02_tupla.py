# tipo de dato 'tupla'
# Las tuplas representan estructuras simples.
# Típicamente, una tupla representa un solo objeto con varias partes.
# Una analogía posible es la siguiente: Una tupla es como una fila de una tabla.

# para crear una 'tupla' usamos los parentesis: ()
popurri = ('Rojo', 'mesa-redonda', False, 2021, 'Argentina')
popurri # ('Rojo', 'mesa-redonda', False, 2021, 'Argentina')

paises = [
    ('argentina', 'buenos aires', 2021),
    ('chile', 'santiago', 1991),
    ('uruguay', 'montevideo', 2020),
    ('brasil', 'sao paulo', 2000)
]
paises # [('argentina', 'buenos aires', 2021), ('chile', 'santiago', 1991), ('uruguay', 'montevideo', 2020), ('brasil', 'sao paulo', 2000)]

# operaciones
# - [indice]: acceder alas tuplas están ordenadas, asique se acceden tal cual como las 'listas'
popurri[0] # 'Rojo'
popurri[1] # 'mesa-redonda'
popurri[-1] # 'Argentina'

# - [indice] = : NO SE PUEDE. el contenido de una tupla no se modifica.
popurri[0] = 'Verde' # TypeError: 'tuple' object does not support item assignment

# 📦 empaquetar y desempaquetar 📦
# las tuplas se podría decir que 'empaquetan' y 'desempaquetan' variables.
# Cuando hacemos (a, b, c), estamos 'empaquetando' 'a', 'b' y 'c' en un mismo paquete/tupla.
a = 'uno'
b = 'dos'
c = 'tres'
paquete = (a, b, c)
paquete # ('uno', 'dos', 'tres')

# Cuando queres trabajar con a, b y c por separado, podemos 'desempaquetarlos' y guardalos en otras variables, EN UNA LÍNEA.
d, e, f = paquete
d # 'uno'
e # 'dos'
f # 'tres'