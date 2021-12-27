from typing import List


print('Hola, mundo')

nombre = 'Jorge Winder Avila'

print('Para el tipo de dato:', type(nombre))
print('Para la longitud:', len(nombre))
print('Este es el caracter por indice:', nombre[2], nombre[10])
print('Rebanar cadena de los primeros 5', nombre[0:4])
print('Revertir palabras', nombre[::-1])

print(f'Cadena capitalizada: {nombre.capitalize()} para el primer caracter de toda la cadena')

print(f'Cadena transformada a mayúsculas: {nombre.upper()}')
print(f'Cadena transformada a minúsculas: {nombre.lower()}')

print(f'Remplazar letra', nombre.replace('e', 'E'))

print(f'Separar una cadena: {nombre.split(" ")}')
print(f'Unir cadenas separadas: { "-".join(nombre.split(" ")) }')

print('\n====================\n')

# Recibir datos del usuario

dato = input('Ingrese un número: ')
print(f'El dato ingresado por el usuario es: {dato}')

print('\n====================\n')

# Estructuras de control

temperatura = 36

if temperatura <= 36:
    print('No tiene fiebre')
else:
    print('Tiene fiebre')

print('\n====================\n')

# Estructura de datos: Listas

Lista = [1, 2, 10, 34, 25, 10]

Lista.append(22)
Lista.extend([100, 129, 245])


print(f'Arreglo: {Lista}')
print(f'Cabtidad de elementos de arreglo: {len(Lista)}')
print(f'Recuento de un valor en arreglo {Lista.count(10)}')
print(f'Eliminar un elemento:  {Lista.pop()}')
print(f'Eliminar un elemento:  {Lista}')

print('\n====================\n')

# Estructura: Diccionario de datos
  
persona = {'Nombre': 'Jorge', 'Apellido': 'Winder', 'Edad': 33}
print(persona)

# for clave in persona.keys():
for clave in persona:
    print(clave)

for valor in persona.values():
    print(valor)

for clave, valor in persona.items():
    print(f'Clave -> {clave} y Valor -> {valor}')


print('\n==== Estructura de control "For" ===\n')

for i in range(0,4):
    print(i)

print('\n====================\n')

for i in Lista:
    print(i)

print('\n======= Recorrer una frase ==========\n')

palabra = 'Esta es una frase'

for letra in palabra:
    print(letra)

print('\n==== Estructura de control "While" ===\n')

i = 0

while i < 6:
    i+=2
    print(i)


print('\n==== Lectura de archivo ===\n')

with open('nuevo_archivo.txt', 'r') as file:
    for line in file:
        print(line)


print('\n==== Escritura de archivo ===\n')

objeto = {"Jorge": 33, "María": 87, "Gonzalo": 85}

# Escribir en un archivo
 
with open("archivo_objeto.txt", 'w') as archivo:
    for clave, valor in objeto.items():
        archivo.write(f'{clave} {valor}\n')

# Agregar contenido a un archivo

objeto_nuevo = {"Mario": 33, "Claudia": 87, "Ricardo": 85}

with open("archivo_objeto.txt", "a") as archivo:
    for clave, valor in objeto_nuevo.items():
        archivo.write(f'{clave} {valor}\n')

