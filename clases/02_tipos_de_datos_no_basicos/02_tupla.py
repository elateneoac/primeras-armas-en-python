

una_tupla = ('Rojo', 'mesa-redonda', False, 2021, 'Argentina')
una_tupla.index('Argentina')

paises = [
    ('argentina', 'buenos aires', 2021),
    ('chile', 'santiago', 1991),
    ('uruguay', 'montevideo', 2020),
    ('brasil', 'sao paulo', 2000)
]


# iterar tradicional
for pais_y_capital in paises:
    pais = pais_y_capital[0]
    capital = pais_y_capital[1]
    anio = pais_y_capital[2]
    print('Pais: ' + pais + ', Capital: ' + capital)

# iterar con tuplas pythonista
for pais, capital, anio in paises:
    print('Pais: ' + pais + ', Capital: ' + capital + ' Año: ' + str(anio))