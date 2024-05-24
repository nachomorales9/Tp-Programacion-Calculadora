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
    print(f"Primer número: {a if a else "No ingresado"}")
    print(f"Segundo número: {b if b else "No ingresado"}")
    operacion_nombre = operaciones.get(operacion, "No seleccionada")
    print(f"Operación seleccionada: {operacion_nombre}")

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
    match operacion:
        case 1:
            return suma(a, b)
        case 2:
            return resta(a, b)
        case 3:
            return multiplicacion(a, b)
        case 4:
            return division(a, b)
        case 5:
            return factorial(a) and factorial(b)

def funcion_principal():
    a = None
    b = None
    operacion = None

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
            case "4":
                if a is None or b is None:
                    print("Debe ingresar ambos números primero.")
                elif operacion is None:
                    print("Debe seleccionar una operación primero.")
                else:
                    operaciones = {
                        1: "Suma",
                        2: "Resta",
                        3: "Multiplicación",
                        4: "División",
                        5: "Factorial"
                    }
                    resultado = ejecutar_operacion(operacion, a, b)
                    operacion_nombre = operaciones.get(operacion, "Operación desconocida")
                    if operacion == 5:
                        print(f"El {operacion_nombre} de {a} es = {resultado}")
                    else:
                        print(f"La {operacion_nombre} entre {a} y {b} es = {resultado}")
                    pausar()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Por favor, ingrese una opción válida.")

