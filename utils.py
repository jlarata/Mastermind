from time import sleep

#produce el efecto de escritura
#a menor intervalo mayor veocidad. ejemplo 0.02
#si no se indica un intervalo como parámetro, por defecto queda .02
def slowPrint(str, intervalo=0.015):
    for letter in str:
        print(letter, end='', flush=True)
        sleep(intervalo)
        
#no sale del ciclo hasta no tener un ingreso numérico
#el centinela sirve para cuando se necesita pasar una excepción a la validación
#i.e. que sea numérico o bien que sea un determinado str.
def validaInputNumerico(str, centinela=['centinela']): 
    if str in centinela:
        return str
    else: 
        while not str.isnumeric():
            slowPrint("\n Eso no es un número. \n Pruebe nuevamente:")
            str = input('>> ')
        return int(str)
    
def validaInputSoN(str, centinela=['centinela']): 
    if str in centinela:
        return str
    else: 
        while not str in "sSnN":
            slowPrint("\n Eso no es ni \"s\" ni \"n\" \n Pruebe nuevamente: \n")
            str = input('>> ')
        return str