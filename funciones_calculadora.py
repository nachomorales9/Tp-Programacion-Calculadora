from os import system

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0 or a == 0:
        return "inexistente, no es posible dividir por 0."
    return a / b

def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def limpiar_pantalla(): #Limpia pantalla
    system("cls")

def pausar(): #Pausa el codigo, utilizar si o si con limpiar pantalla
    system("pause")
    


def ingresar_numero_a():
    a = None
    while a is None:
        try:
            a = int(input("Ingrese el primer número: "))
        except ValueError:
            print("Error, ingrese un número nuevamente")
    return a


def ingresar_numero_b():
    b = None
    while b is None:
        try:
            b = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    return b