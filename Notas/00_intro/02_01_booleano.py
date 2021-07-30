# 2.1. booleanos
# el tipo 'booleano' solo puede tomar dos valores: 'True' o 'False' (siempre con mayúscula):
verdadero = True
falso = False

verdadero # True
falso # False

# el uso principal de los booleanos es para hacer comparaciones.
# para hacer comparaciones entre variables, usamos:
# == para chequear si 'son iguales'
verdadero == True # True
verdadero == False # False

# != para chequear si 'son distintos'
falso != True # True
falso != False # False

# yendo un poco más a fondo, los booleanos puede verse como 'unos' y 'ceros': 1 = True, 0 = False.
# en la práctica, también funcionan como 1 y 0:

# la multiplicación por booleanos siempre es la operación más útil.
10 * verdadero # 10
10 * falso # 0

# el resto de las operaciones funcionan pero en la práctica no se usan.
10 + verdadero # 11
10 + falso # 10

10 - verdadero # 9
10 - falso # 10

10 / verdadero # 10.0
10 / falso # ZeroDivisionError: division by zero