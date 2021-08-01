# 3. listas
una_docena = [0,1,2,3,4,5,6,7,8,9,10,11]
una_docena

# 3.1. acceder a los elementos
# primer elemento
una_docena[0] # 0

# ultima elemento
una_docena[11] # IndexError: list index out of range

# se le puede mandar cualquier cosa
lista_mixta = [1,2,3,4, 'hola', 'chau']
lista_mixta[5]

# accediendo a los elementos
una_docena[2:4]

# último elemento
una_docena[-1]

# del primero al anteultimo
una_docena[0:-1]

# del segundo en adelante
una_docena[1:]

# 3.2. recorrer las listas
for numero in una_docena:
    # hace algo
    numero

# lo mismo de arriba pero usando 'while'
i = 0
while i < 7:
    una_docena[i]
    i += 1

# iterar al estilo python

# estilo tradi
una_docena_por_dos = []
otra_docena_por_dos = []
for numero in una_docena:
    una_docena_por_dos.append(numero * 2)

una_docena_por_dos

# estilo python
otra_docena_por_dos = [numero * 2 for numero in una_docena if numero < 6]
otra_docena_por_dos