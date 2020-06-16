# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:04:33 2020

@author: JohnnyGS
"""

#Librerías necesarias.
import random
import time

#Función que muestra las opciones posibles con un menú.
def menu():
    print()
    print("Bienvenido al Tres en Raya")
    print("--------------------------")
    print()
    print("Seleccione su ficha: ")
    print()
    print("O Empieza el juego")
    print()
    print("Elija: O / X")
    print()
    
    ficha=""
    while ficha != "O" and ficha != "X":
        print("Seleccione una ficha válida, por favor...")
        ficha=input("--> ").upper()
        
    if ficha=="O":
        jugador="O"
        ordenador="X"
    else:
        jugador="X"
        ordenador="O"
#Tras escoger ficha indica cual será para la máquina y cual para el jugador.
    return jugador, ordenador

#Función para mostrar el tablero actual tras cada jugada.
def m_tablero(tablero):
    print()
    print("Tres en raya")
    print()
    print("1 | 2 | 3")
#Transforma el print en la posición indicada del array.
    print("{} | {} | {}".format(tablero[0], tablero[1], tablero[2]))
    print("  |   |")
    print("---+---+---")
    print("4 | 5 | 6")
    print("{} | {} | {}".format(tablero[3], tablero[4], tablero[5]))
    print("  |   |")
    print("---+---+---")
    print("7 | 8 | 9")
    print("{} | {} | {}".format(tablero[6], tablero[7], tablero[8]))
    print("  |   |")
    print()
    
#Función para volver a jugar partida.
def s_jugar():
    print()
    respuesta = input("¿Quiere jugar otra partida? Si(s) - No(n): ").lower()
    if respuesta == "s":
        return True
    else:
        return False
    
#Función para obtener ganador de la partida.
def ganador(tablero, jugador):
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
        tablero[3] == tablero[4] == tablero[5] == jugador or \
        tablero[6] == tablero[7] == tablero[8] == jugador or \
        tablero[0] == tablero[3] == tablero[6] == jugador or \
        tablero[1] == tablero[4] == tablero[7] == jugador or \
        tablero[2] == tablero[5] == tablero[8] == jugador or \
        tablero[0] == tablero[4] == tablero[8] == jugador or \
        tablero[2] == tablero[4] == tablero[6] == jugador:
            
        return True
    
    else:
        
        return False

#Función para obtener tablero, si está lleno se da por empate.
def tablero_lleno(tablero):
    for i in tablero:
        if i == " ":
            return False
    else:
        return True

#Función para saber si una casilla está en blanco.
def casilla_libre(tablero, casilla):
    return tablero[casilla] == " "

#Función que define los posibles movimientos del tablero (1-9).
def movimiento(tablero):
    posiciones=["1","2","3","4","5","6","7","8","9"]
    posicion=None
    while True:
        if posicion not in posiciones:
            posicion=input("Introduzca una posición válida (1-9): ")
        else:
            posicion=int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("La posición elegida se encuentra ocupada.")
            else:
                return posicion-1

#Función indicando todos los posibles movimientos para la máquina.
def movimiento_ordenador(tablero, jugador):
    if tablero[0] == tablero[1] == jugador and tablero[2] == " ":
        casilla=2
    elif tablero[0] == tablero[2] == jugador and tablero[1] == " ":
        casilla=1
    elif tablero[1] == tablero[2] == jugador and tablero[0] == " ":
        casilla=0
    elif tablero[3] == tablero[4] == jugador and tablero[5] == " ":
        casilla=5
    elif tablero[3] == tablero[5] == jugador and tablero[4] == " ":
        casilla=4
    elif tablero[4] == tablero[5] == jugador and tablero[3] == " ":
        casilla=3
    elif tablero[6] == tablero[7] == jugador and tablero[8] == " ":
        casilla=8
    elif tablero[6] == tablero[8] == jugador and tablero[7] == " ":
        casilla=7
    elif tablero[7] == tablero[8] == jugador and tablero[6] == " ":
        casilla=6
    elif tablero[0] == tablero[3] == jugador and tablero[6] == " ":
        casilla=6
    elif tablero[0] == tablero[6] == jugador and tablero[3] == " ":
        casilla=3
    elif tablero[3] == tablero[6] == jugador and tablero[0] == " ":
        casilla=0
    elif tablero[1] == tablero[4] == jugador and tablero[7] == " ":
        casilla=7
    elif tablero[1] == tablero[7] == jugador and tablero[4] == " ":
        casilla=4
    elif tablero[4] == tablero[7] == jugador and tablero[1] == " ":
        casilla=1
    elif tablero[2] == tablero[5] == jugador and tablero[8] == " ":
        casilla=8
    elif tablero[2] == tablero[8] == jugador and tablero[5] == " ":
        casilla=5
    elif tablero[5] == tablero[8] == jugador and tablero[2] == " ":
        casilla=2
    elif tablero[0] == tablero[4] == jugador and tablero[8] == " ":
        casilla=8
    elif tablero[0] == tablero[8] == jugador and tablero[4] == " ":
        casilla=4
    elif tablero[4] == tablero[8] == jugador and tablero[0] == " ":
        casilla=0
    elif tablero[2] == tablero[4] == jugador and tablero[6] == " ":
        casilla=6
    elif tablero[2] == tablero[6] == jugador and tablero[4] == " ":
        casilla=4
    elif tablero[4] == tablero[6] == jugador and tablero[2] == " ":
        casilla=2
    else:
#Si la casilla se encuentra vacía y no hay movimiento ganador hará uno random
#en vacía.
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break
    return casilla


#Programa principal

jugando=True

while jugando:
    tablero = [" "]*9
    
    jugador, ordenador=menu()
    
    m_tablero(tablero)
    
    if jugador=="O":
        turno="Jugador"
    else:
        turno="Ordenador"
    
    partida=True
    
    while partida:
        if tablero_lleno(tablero):
            print("Empate")
            partida=False
        elif turno=="Jugador":
            casilla=movimiento(tablero)
            tablero[casilla]=jugador
            turno="Ordenador"
            m_tablero(tablero)
            if ganador(tablero,jugador):
                print("Enhorabuena, has ganado!")
                partida=False
        elif turno=="Ordenador":
            print("La máquina efectuará su movimiento.")
            time.sleep(2)
            casilla=movimiento_ordenador(tablero,ordenador)
            tablero[casilla]=ordenador
            turno="Jugador"
            m_tablero(tablero)
            if ganador(tablero,ordenador):
                print("Has perdido!")
                partida=False
    jugando=s_jugar()