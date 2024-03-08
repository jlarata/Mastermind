'''
A game of logical guessing. This was a challenge in an Algorythm Class Manual i'm reading.
The game will produce a random number with 4 different figures. The player must guess by trying
each time with a 4-digit number. The program return how many "aciertos" (successes) and "coincidencias"
meaning a correct number in the correct position, or a correct number in a wrong position.
When total success is achieved, the program return the amount of attempts.
'''

import utils
from random import choice  

cant_cifras = 4
        
def saluda():
    utils.slowPrint("\n Hola, vamos a jugar al Mastermind, quéres que te lea las reglas? s/n: ", 0.005)
    a = input(">>: ")
    b = utils.validaInputSoN(a, "sSnN")
    return b

def leeReglas(b, cant_cifras):
    reglas = f"""\n Cada vez que se empieza un partido, el Mastermind eige un CODIGO que consiste en un número de {cant_cifras} cifras
(sin cifras repetidas). El jugador debe adivinar el CODIGO en la menor cantidad de intentos posibles.
    Cada intento consiste en una propuesta de un código posible que tipea el jugador, por el que recibe
una respuesta del MASTERMIND indicando ACIERTOS y COINCIDENCIAS.
    La cantidad de aciertos es la cantidad de dígitos que propuso el jugador que también están en el código en la misma posición.
    La cantidad de coincidencias es la cantidad de digitos que propuso el jugador
que también están en el código pero en una posición distinta.

Listx? Allá vamos!

"""
    if b.upper() == "S":
        utils.slowPrint(f"{reglas}", 0.005)
    elif b.upper() == "N":
        utils.slowPrint("\n Bien, comencemos.\n")

def eligeNumeroAlAzar():
    cifrasSinUsar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cifras = []
    
    a = choice(cifrasSinUsar)
    cifras.append(a)
    cifrasSinUsar.remove(a)
    b = choice(cifrasSinUsar)
    cifras.append(b)
    cifrasSinUsar.remove(b)
    c = choice(cifrasSinUsar)
    cifras.append(c)
    cifrasSinUsar.remove(c)
    d = choice(cifrasSinUsar)
    cifras.append(d)
    
    #print (cifras, cifrasSinUsar)
    return str(a)+str(b)+str(c)+str(d)

def tomaInputDelJugador():
    utils.slowPrint("\n Ingrese su intento (o ingrese \"X\" para salir): \n")
    inputDelJugador = input(" >> ")
    return inputDelJugador

def validaInput(inputDelJugador):
    if inputDelJugador.upper() == "X":
        cerraYNosFuimo()
        
    while not str(inputDelJugador).isnumeric() or len(inputDelJugador) < 4 or int(inputDelJugador) >= 10000:
        if inputDelJugador.upper() == "X":
            cerraYNosFuimo()
        else:
            utils.slowPrint("\n Debe ingresar un número de cuatro cifras. \n Pruebe nuevamente:")
            inputDelJugador = input('>> ')
    return inputDelJugador
    
def analizaAciertos(codigo, input):
    cifra = 0
    aciertos = 0
    for x in range(4):
        if codigo[cifra] == input[cifra]:
            aciertos += 1
        cifra += 1
    return (aciertos)

def analizaCoincidencias(codigo, inputValidado, aciertos):
    cantidadDeCoincidencias = 0
    #la lista y los append sirven para que el jugador pueda ingresar "1111" y no le de 3 coincidencias
    #alternativamente se puede impedir que el jugador ingrese ese tipo de inputs en la validación
    #haciendo el juego más difícil.
    coincidencias = []
    for x in inputValidado:
        if x in codigo and x not in coincidencias:
            coincidencias.append(x)
            cantidadDeCoincidencias += 1    
    return cantidadDeCoincidencias-aciertos

def recibeValidaAnaliza(codigo):
    inputValidado = ""
    intentos = 0
    while not inputValidado == codigo:
        inputDelJugador = tomaInputDelJugador()
        inputValidado = validaInput(inputDelJugador)
        aciertos = analizaAciertos(codigo, inputValidado)
        coincidencias = analizaCoincidencias(codigo, inputValidado, aciertos)
        intentos += 1
        #print (" El codigo es", codigo, "\n El jugador ingresó ", inputValidado)
        print(" Se encontraron ", aciertos, " aciertos y ", coincidencias, "coincidencias.")
    return(intentos)
    
def cerraYNosFuimo():
    input("Hasta la próxima!")
    quit()
    

def main():
    cant_cifras = 4
    
    b = saluda()
    leeReglas(b, cant_cifras)
    codigo = eligeNumeroAlAzar()
    intentos = recibeValidaAnaliza(codigo)
    print("\nEnhorabuena! lo resolviste en ", intentos, "intentos")    
    input("\nHasta la próxima!\n")
    quit()

main()

