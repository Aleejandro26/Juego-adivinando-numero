import random

def juego_adivinaza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de numero:")
    print("Debes adivinar un numero del 1 al 100")
    print("Intenta adivinarlo")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menos a {adivinanza}")
            else:
                print(f"Felicidades has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos")
        else:
            print("Por favor introduzca un numero valido de entre el 1 al 100")

juego_adivinaza()