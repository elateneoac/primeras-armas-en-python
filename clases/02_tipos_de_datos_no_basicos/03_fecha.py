import datetime

una_fecha = datetime.datetime(2021, 8, 5, 20, 42)

una_fecha.year
una_fecha.month
una_fecha.day
una_fecha.hour
una_fecha.minute
una_fecha.second

# obtener instante
ahora = datetime.datetime.now()

string_una_fecha = una_fecha.strftime('año %Y, mes %m, día %d')
string_una_fecha

string_ahora = datetime.datetime.now().strftime('año %Y, mes %m, día %d')
string_ahora

otra_fecha = datetime.datetime.strptime('2021-05-08', '%Y-%m-%d')
