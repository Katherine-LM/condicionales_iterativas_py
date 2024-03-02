import random

lista  = ["piedra", "papel", "tijera"]

computador = random.choice(lista)
jugador = None

while jugador not in lista:
    jugador = input("Escoge entre piedra, papel o tijera: ").lower()


if jugador == computador:
    print("Jugador ", jugador)
    print("Computadora ", computador)
    print("Empate!")

elif jugador == "roca":
    if computador == "papel":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Perdiste!")
    if computador == "tijera":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Ganaste!")

elif jugador == "papel":
    if computador == "tijera":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Perdiste!")
    if computador == "piedra":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Ganaste!")

elif jugador == "tijera":
    if computador == "piedra":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Perdiste!")
    if computador == "piedra":
        print("Jugador ", jugador)
        print("Computadora ", computador)
        print("Ganaste!")
