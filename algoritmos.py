import os
import time

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


# =======================
# Enumeración exhaustiva
# =======================
# Se busca la raiz cuadrada de un número de ingresado

def verificar_raiz_cuadrada():

    ingreso = int(input("Ingrese un número: "))
    respuesta = 0

    # Tiempo de inicio proceso
    tiempo_inicial = time.time()
    # print(time.localtime())

    while respuesta**2 < ingreso:
        respuesta +=1

    if respuesta**2 == ingreso:
        print(f"La raiz cuadrada de {ingreso} es {respuesta}")
    else:
        print(f"El número no tiene raiz cuadrada exacta")

    # Tiempo de ejecución del proceso
    print(f"El tiempo de ejecución del proceso fue {time.time() - tiempo_inicial}")

if __name__ == '__main__':
    limpiar_consola()
    verificar_raiz_cuadrada()