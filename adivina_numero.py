import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_ingresado = int(input('Ingresa un número :'))

    while numero_aleatorio != numero_ingresado:
        if numero_aleatorio > numero_ingresado:
            print('\nEl número es mayor')
            numero_ingresado = int(input('Ingresa otro número más grande :'))
            
        elif numero_aleatorio < numero_ingresado:
            print('\nEl número es menor')
            numero_ingresado = int(input('Ingresa otro número más pequeño :'))
            
    
    print('\n>>> GANASTE EL JUEGO <<<')

if __name__ == '__main__':
    run()