import os
import requests
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear')

print("""
========================================
======== Casa de cambio digital ========
========================================
""")

print(f'Tipo de cambio SUNAT para hoy {date.today()}\n')

tipo_de_cambio = requests.get(f'https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={date.today()}').json()
operación = input('La operación es de ... Compra (c) o Venta (v) =>')

monto = None

while monto is None:

    try:
        if operación.upper() == 'C':
            valor = tipo_de_cambio['compra']
            monto = float(input("Monto en dólares para la compra($) :"))
            print(f'Monto de cambio a soles :\n{round(monto * valor, 2)} soles peruanos\n')
        else:
            valor = tipo_de_cambio['venta']
            monto = float(input("Monto en soles para la venta(S/) :"))
            print(f'Monto de cambio a dólares :\n{round(monto * valor, 2)} dólares\n')

            print(f'¡Gracias por hacer su cambio digital!\n')

    except:

        if monto is None:
            print(f'\n>>> Debe ingresar monto <<<<\n')


input("\n\n>>> Presione la tecla 'ENTER' para salir")

# API: fuente de datos de referencia
# https://apis.net.pe/api-tipo-cambio.html