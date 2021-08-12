# tipo de dato 'fecha'
# para manejar fechas, tenemos que usar un tipo de dato NO primitivo: es decir, tenemos que importarlo.
# la libreria 'datetime' está dentro de las que vienen incluidas con python, asique es casi como un tipo primitivo.
# dentro de 'datetime' tenemos:
# - datetime (si, mismo nombre): para trabajar fecha + hora
# - date: para trabajar solo fecha
# - time: para trabajar solo hora

import datetime

# 'datetime'
# creamos una 'fecha y hora'
una_fecha_y_hora = datetime.datetime(2021, 1, 1, 12, 59)

# accedemos a sus valores
una_fecha_y_hora.year # 2021
una_fecha_y_hora.month # 1
una_fecha_y_hora.day # 1
una_fecha_y_hora.hour # 12
una_fecha_y_hora.minute # 59
una_fecha_y_hora.second # 0

# obtener instante
ahora = datetime.datetime.now()
ahora # datetime.datetime(año, mes, dia, hora, minutos, segundos, microsegundos)

# 'date'
# creamos una 'fecha'
una_fecha = datetime.date(2021, 1, 1)
una_fecha.year # 2021
una_fecha.month # 1
una_fecha.day # 1

# obtener fecha actual
hoy = datetime.date.today()
hoy # datetime.date(año, mes, dia)

# 'time'
# creamos un 'horario'
un_horario = datetime.time(9, 20, 59, 123456)
un_horario.hour # 9
un_horario.minute # 20 
un_horario.second # 59
un_horario.microsecond # 123456

# 🕒 diferencia de tiempo 🕒
# dentro de 'datetime' existe también el módulo 'timedelta': en la jerga, delta se usa para referirse a 'variación'.
# en este caso 'timedelta' = 'variación de tiempo'.
# para operar, python permite usar los operadores: + y -, tal como si se tratase de números.
primero_de_enero_del_2021 = datetime.datetime(2021, 1, 1)
primero_de_enero_del_2020 = datetime.datetime(2020, 1, 1)

un_anio_de_diferencia = primero_de_enero_del_2021 - primero_de_enero_del_2020
un_anio_de_diferencia # datetime.timedelta(366)
un_anio_de_diferencia.total_seconds() # 31622400.0

un_anio_de_diferencia_negativo = primero_de_enero_del_2020 - primero_de_enero_del_2021 # datetime.timedelta(-366)
un_anio_de_diferencia_negativo # datetime.timedelta(-366)

# la diferencia se expresa en: dias y segundos.
# es decir, si tengo dos fechas con 1 día y 1 hora de diferencia, 'timdelta' dirá que hay 1 día y 3600 segundos de diferencia.
una_hora_del_primero_de_enero_del_2021 = datetime.datetime(2021, 1, 1, 1)
una_hora_del_primero_de_enero_del_2021 - primero_de_enero_del_2020 # datetime.timedelta(366, 3600)


# 🖊️ pasar fecha a strings, y viceversa 🖊️
# para pasar de string a fecha y al revés, necesitamos indicar un formato particular
# este formato nos va a decir cómo queremos escribir la fecha (de datetime a string),
# o cómo está escrita la fecha (de string a datetime).

# de fecha a string: strftime (la 'f' es de 'format')
string_una_fecha = una_fecha_y_hora.strftime('%Y/%m/%d')
string_una_fecha # '2021/01/01'

string_una_fecha = una_fecha_y_hora.strftime('año %Y, mes %m, día %d')
string_una_fecha # 'año 2021, mes 01, día 01'

string_ahora = datetime.datetime.now().strftime('año %Y, mes %m, día %d')
string_ahora # 'año (anio actual), mes (mes actual), día (dia actual)'

# de string a fecha: strptime (la 'p' es de 'parse')
string_otra_fecha = '2021-05-08'
otra_fecha = datetime.datetime.strptime(string_otra_fecha, '%Y-%m-%d')
otra_fecha # datetime.datetime(2021, 5, 8, 0, 0)

# PARA MÁS INFO: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior