from os import system
from funciones_calculadora import *

def limpiar_pantalla(a=None, b=None, operacion=None):
    operaciones = {
        1: "Suma",
        2: "Resta",
        3: "Multiplicación",
        4: "División",
        5: "Factorial"}

    system("cls")
    print("Bienvenido a la calculadora de Ignacio, espero que te guste!")
    print(f"Primer número: {a if a is not None else "Ingresa el primer número"}")
    print(f"Segundo número: {b if b is not None else "Ingresa el segundo número"}")
    operacion_nombre = operaciones.get(operacion, "Selecciona la operación!")
    print(f"La operación que elegiste fue: {operacion_nombre}")

def pausar():
    input("Presione Enter para continuar...")

def mostrar_menu_operaciones():
    print("Seleccione la operación a realizar:")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Factorial")

def ejecutar_operacion(operacion, a, b):
    if operacion == 5:
        print(f"El resultado del factorial de {a} es: {factorial(a)} ")
        print(f"El resultado del factorial de {b} es: {factorial(b)} ")
        return(f"El factorial de {a} es {factorial(a)} y el de {b} es {factorial(b)} ")
    else:
        operaciones = {
            1: suma,
            2: resta,
            3: multiplicacion,
            4: division}

        return operaciones[operacion](a, b)

def funcion_principal():
    a = None
    b = None
    operacion = None
    resultado_operacion = None  #varable para guardar el resultado de la operación

    while True:
        limpiar_pantalla(a, b, operacion)
        print("Menu de opciones:")
        print("1) Ingresar Primer Número")
        print("2) Ingresar Segundo Número")
        print("3) Mostrar Operaciones")
        print("4) Mostrar Resultados")
        print("5) Salir del Programa")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                a = ingresar_numero_a()
            case "2":
                b = ingresar_numero_b()
            case "3":
                mostrar_menu_operaciones()
                operacion = int(input("Ingrese la operación a realizar: "))
            case "4" if a is None or b is None or operacion is None or operacion > 5:
                print("Debe ingresar ambos números y seleccionar una operación válida primero.")
            case "4":
                if resultado_operacion is not None:
                    print(f"El resultado de la operación anterior es: {resultado_operacion}")
                else:
                    print("Aún no se ha realizado ninguna operación.")
                pausar()
            case "5":
                print("Gracias por usar la calculadora de Ignacio. ¡Que tengas un buen día!")
                break
            case _:
                print("Opción inválida. Por favor, ingrese una opción válida.")

        if operacion is not None and a is not None and b is not None:
            resultado_operacion = ejecutar_operacion(operacion, a, b)

    pausar()

funcion_principal()
