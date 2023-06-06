import os
import time

def limparTela():
    os.system("cls")

def aguarde(segundos=3):
    time.sleep(segundos)

def palavraChave (palavra , ultimaLetra):
    for letra in palavra:
        if letra in ultimaLetra:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()