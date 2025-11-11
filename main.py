from operaciones import * 

# Bucle principal : mantiene el programa corriendo hasta que el usuario  elija salir
while True:
    # ------------ MENU PRINCIPAL ------------ 
    # Se muestra en consola la lista de operaciones disponibles
    print("***=== Calculadora Sencilla ===***")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Modulo")
    print("7. Salir")

    # Solicita al usuario que elija una opcion del menu
    try:
        opcion = int(input("Elige una opción (1-7): ")) 
    except ValueError:
        # Captura el error si el usuario introdice texto o un valor no numerico
        print("¡Debe de ser un tipo numero!")
        continue # vuelve a mostrar el menu sin detener el programa

    # Si el usuario elije la opcion 5, se terminar el programa
    if opcion == 7:
        print("Haz detenido el programa")
        break    
    # Si elije una opcion validad (1 a 5) se solicitan los numeros a operar
    elif opcion >= 1 and opcion <= 6:
        # Se piden los dos numeros para realizar la operacion
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("¡Debes introducir un numero valido!")
            continue # vuelve al inicio del bucle
        
        if opcion == 1:
            print(f"Resultado: {sumar(num1, num2)}") 
        elif opcion == 2:
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {dividir(num1, num2)}")
        elif opcion == 5:
            print(f"Resultado: {potencia(num1, num2)}")
        elif opcion == 6:
            print(f"Resultado: {modulo(num1, num2)}")
    # Si el usuario elije un numero fuera del rango
    else: 
         print("Debe elegir un numero del 1 al 6")
       
