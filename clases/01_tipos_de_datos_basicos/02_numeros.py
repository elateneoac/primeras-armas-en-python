# 2.2. números
# el tipo 'numero' puede ser 'entero' ('entero' = 'int' = 'Integer')  y 'con coma' ('con coma' = 'punto flotante' = 'Float'):
docena = 12
pi = 3.1416
gravedad = -9.8

docena # 12
pi # 3.1416
gravedad # -9.8


# 2.2.1. operaciones típicas
# con las variables de tipo número se pueden hacer las operaciones típicas:

# suma
docena + 10 # 22
pi + 1.1 # 4.2416

# resta
docena - 10 # 2
pi - 1.1 # 2.0416

# multiplicación
docena * 2 # 24
pi * 2 # 6.2832

# división: devuelve un tipo 'con coma', o 'float'
docena / 2 # 6.0
docena / 8 # 1.5
pi / 2 # 1.5708

# división entera: sólo devuelve la parte entero, por eso devuelve un tipo 'int')
docena // 2 # 6 
docena // 8 # 1
pi // 2 # 1.0 (en este caso devuelve un tipo 'con coma', porque 'pi' es 'con coma')

# módulo: devuelve el resto (breve repaso de matemáticas: el resto de '5 / 2' es '3')
docena % 10 # 2
docena % 8 # 4
pi % 2 # 1.1416

# potencia
2 ** 2 # 4
docena ** 2 # 144
pi ** 2 # 9.86965056

# valor absoluto: si le paso un negativo, me devuelve el valor en positivo
abs(gravedad)
abs(docena)


# 2.2.2. comparaciones
# entre números podemos hacer comparaciones, además de las que hicimos con los booleanos, también se suman los de mayor o menor:

# mayor 'estricto'
docena < 20 # True
docena < 12 # False

# mayor 'o igual'
docena <= 12 # True
docena <= 10 # False

# menor 'estricto'
docena > 20 # False
docena > 12 # False

# menor 'o igual'
docena >= 12 # True
docena >= 10 # True

# igual a (ATENCIÓN ACÁ: es con un DOBLE IGUAL '==')
docena == 12 # True
docena == 10 # False

# distinto a
docena != 12 # False
docena != 10 # True

# negado (no es estrictamente una comparación, pero va por ahí)
not docena == 12 # False
not docena == 10 # True


# 2.2.2.1 varias comparaciones juntas
# es posible concatenar varias comparaciones (esto después lo vamos a usar con 'if' 'for' y 'while')
# para concatenar comparaciones hacemos podemos usar:
# - operadores tradicionales, o
# - palabras reservadas, bien python style:
# TIP 💡 siempre intentar usar 'and', 'or' o 'not': Es mucho más cómodo de leer y más facil de escribir.

# tradi style
# &: se cumplen TODAS
docena == 12 & docena < 20 # True
docena == 12 & docena < 10 # False
docena == 10 & docena < 10 # False

# |: se cumple ALGUNA (o POR LO MENOS UNA)
docena == 12 | docena < 20 # True
docena == 12 | docena < 10 # True
docena == 10 | docena < 10 # False

# python style (podemos usar 'not' en el medio, para negar la segunda comparación)
# and: se cumplen TODAS
docena == 12 and docena < 20 # True
docena == 12 and docena < 10 # False
docena == 12 and not docena < 10 # True
docena == 10 and docena < 10 # False

# or: se cumple ALGUNA (o POR LO MENOS UNA)
docena == 12 or docena < 20 # True
docena == 12 or docena < 10 # True
docena == 10 or docena < 10 # False
docena == 10 or not docena < 10 # True

# a todas las comparaciones de arriba, si le agregamos un 'not' al principio, es como negar TODA LA COMPARACIÓN


# (OPCIONAL) 2.2.3. PARA LOS AMANTES DE LAS MATEMÁTICAS
# yendo un poco más allá, también podemos hacer otras operaciones usando la librería 'math'
import math
# raiz cuadrada
math.sqrt(docena) # 3.4641016151377544

# seno
math.sin(docena) # -0.5365729180004349

# coseno
math.cos(docena) # 0.8438539587324921

# tangente
math.tan(docena) # -0.6358599286615808

# log natural
math.log(docena) # 2.4849066497880004

# número 'con coma' pi
math.pi # 3.141592653589793