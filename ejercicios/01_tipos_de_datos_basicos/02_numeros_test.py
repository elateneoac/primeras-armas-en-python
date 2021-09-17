import pytest
import inspect

respuesta = None
resultado = None
solucion = None

def test_sumar_numeros():
    # - sumar dos numeros, y
    # - que la suma sea igual a 10

    respuesta = '''
    5 + 5
    '''
    
    assert '+' in respuesta
    assert eval(respuesta.strip()) == 10

def test_sumar_variables():
    # - crear las variables 'una_variable' y 'otra_variable'
    # - sumarlas, y
    # - que la suma sea igual a 100

    respuesta = '''
una_variable = 5
otra_variable = 95
resultado = una_variable + otra_variable
'''

    exec(respuesta)
    assert '+' in respuesta
    assert 'una_variable' in respuesta
    assert 'otra_variable' in respuesta
    assert resultado == 100

def test_restar_numeros():
    # - restar dos numeros,
    # - que la resta sea igual a 10, y
    # - guardar la resta en la variable 'resultado'
    
    respuesta = '''
    20 - 10
    '''

    # eval(respuesta)
    assert '-' in respuesta
    assert eval(respuesta.strip()) == 10

def test_restar_variables():
    # - crear las variables 'una_variable' y 'otra_variables'
    # - restarlas, 
    # - que la resta sea igual a 100, y 
    # - guardar la resta en la variable 'resultado'

    respuesta = '''
    (acá escribir código)
    '''

    exec(respuesta)
    assert '-' in respuesta
    assert 'una_variable' in respuesta
    assert 'otra_variable' in respuesta
    assert resultado == 100