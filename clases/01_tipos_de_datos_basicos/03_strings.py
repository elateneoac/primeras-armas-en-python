# string
# el tipo 'string' es una 'cadena de carácteres' (string = cadena): en castellano, lo podriamos llamar tipo 'texto'.

# armando un 'string'

# comillas simples: sirve para string standars. Generalmente se usan para caracteres (es decir, una sóla letra) 
v_corta = 'v'
ciudad = 'Buenos Aires'

v_corta # 'v'
ciudad # 'Buenos Aires'

# comillas dobles: las más tradicionales.
pais = "Argentina"
pais # "Argentina"

# No hay diferencia entre las comillas simples (') y las dobles (").
# Pero el mismo tipo de comillas que se usó para abrir debe usarse para cerrar.

# comillas triples: nos permiten capturar todo el texto encerrado a lo largo de múltiples lineas.
renglones = '''
Primer renglón.
Segundo renglón.
Último renglón.
'''
renglones # '\n\nPrimer renglón.\n\nSegundo renglón.\n\nÚltimo renglón.\n\n'

# ¿comillas dobles o simples? ¿" o '?
# para crear un 'string', podemos usar "hola" u 'hola'. Es lo mismo.
# En general, "" suele usarse para definir 'string' (es decir, más de una letra),
# mientras que ' suele usarse para definir un 'char' (caracter, una sóla letra).
#
# Recomendación personal: es más practico usar ''. Solamente tenemos que apretar una tecla (la del caracter).
# En cambio, para escribir " tenemos que usar 'shit + 2', es decir, tenemos que apretar dos teclas.
# Es decir, usando ' nos ahorramos apretar teclas. Pareco poco pero esos detalles hacen diferencia.


# ¿por qué una 'cadena'?
# los 'string' puede verse como una lista (cadena) de letras: es decir, puedo accedar a la letra 1, a la 2, a la última, etc etc.
# es decir, se puede usar como una lista standar (ver clase '03_listas.py')

# primer letra
ciudad[0] # 'B'

# segunda letra
ciudad[1] # 'u'

# última letra
ciudad[-1] # 's'

# primeros seis
ciudad[:6] # 'Buenos'

# últimos 5
ciudad[-5:] # 'Aires'

# del 5to al 7mo
ciudad[5:8] # 's A'


# operaciones
# abajo listamos algunos tips útiles para trabajar con strings

# +: concatenar
# dos strings diferentes
ciudad = "Buenos Aires"
pais = "Argentina"
ubicacion = ciudad + ", " + pais + "." # "Buenos Aires, Argentina."
ubicacion

# +=: agregar a lo último
ubicacion += " América del Sur."
ubicacion # "Buenos Aires, Argentina. América del Sur."

# len(): longitud
len(ciudad) # 12

# chequear si contiene una palabra o caracter (in, not in)
ciudad_contiene_B = 'B' in ciudad
ciudad_contiene_B # True

ciudad_contiene_a = 'a' in ciudad
ciudad_contiene_a # False

ciudad_no_contiene_A = 'A' not in ciudad
ciudad_no_contiene_A # False

# *: repetir
ciudad_tres_veces = ciudad * 3
ciudad_tres_veces # 'Buenos AiresBuenos AiresBuenos Aires'

# str(): pasar de número a string
anio = 2021
string_anio = str(anio)
string_anio # '2021'


# métodos de strings
# los strings tienen métodos incorporados que sirven para hacer tareas muy comunes

# strip(): sacar espacios sobrantes de adelante y de atrás
ciudad_con_espacios = "  Buenos Aires  "
ciudad_con_espacios # '  Buenos Aires  '
ciudad_con_espacios.strip() # 'Buenos Aires'

# lower(): todo minúscula
ciudad.lower() # 'buenos aires'

# upper(): todo mayúscula
ciudad.upper() # 'BUENOS AIRES'

# replace(): reemplazar pedazo por otro
telenovela = ciudad.replace('Aires', 'Vecinos')
telenovela # 'Buenos Vecinos'

# str(): convertir un número tipo 'numero' a 'string'
anio = 2021
string_anio = str(anio)
string_anio # '2021'

# más métodos útiles
ciudad.endswith('Aires')       # True. Verifica si termina con el sufijo
ciudad.find('u')               # 1. Primera aparición de 'u' en 'ciudad' (o -1 si no está)
ciudad.index('u')              # 1. Primera aparición de 'u' en s (error si no está)
ciudad.isalpha()               # False. Verifica si los caracteres son alfabéticos
ciudad.isdigit()               # False. Verifica si los caracteres son numéricos
ciudad.islower()               # False. Verifica si los caracteres son minúsculas
ciudad.isupper()               # False. Verifica si los caracteres son mayúsculas
ciudad.join(['hola', 'chau'])  # 'holaBuenos Aireschau'. Une una lista de cadenas usando 'ciudad' como delimitador
','.join(['primero', 'segundo', 'tercero']) # uso más común de 'join
ciudad.split(' ')          # ['Buenos', 'Aires']. Parte la cadena en subcadenas
ciudad.startswith('Bue')      # True. Verifica si comienza con un sufijo

# las cadenas NO se pueden modificar
# los 'string' son de 'sólo lectura'.
# Esto implica que las operaciones y métodos que manipulan cadenas deben crear nuevas cadenas para almacenar su resultado.
ciudad[0] = 'x' # TypeError: 'str' object does not support item assignment