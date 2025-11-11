#-------------------------------------------------------------------------
# MODULO: operaciones                                                    
# Descripcion: Contiene las funciones basicas de operaciones  de mates
# Cada funcion recibe dos parametros y devuelve el resultado.
#------------------------------------------------------------------------

def sumar(a, b): 
    '''
    Retorna la suma de dos numeros

    Parametros:
        a(float): Primer numero
        b(float): Segundo numero

    Retorna:
        float: Resultado de a + b    
    '''
    return a + b  

def restar(a, b):
    '''
    Retorna la resta de dos numeros

    Parametros:
        a(float): Primer numero
        b(float): Segundo numero

    Retorna:
        float: Resultado de a - b    
    '''
    return a - b

def multiplicar(a, b):
    '''
    Retorna el prod de dos numeros

    Parametros:
        a(float): Primer numero
        b(float): Segundo numero

    Retorna:
        float: Resultado de a * b    
    '''
    return a * b

def dividir(a, b):
    '''
    Retorna la cociente de dos numeros
    Controla el error si el divisor es cero

    Parametros:
        a(float): Primer numero
        b(float): Segundo numero

    Retorna:
        float: Resultado de a - b    
    '''
    try: 
       return a / b
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")      

def potencia(a, b):
    '''
    Retorna la potencia del primer numero

    Parametros:
        a (float) : Primer numero
        b (float) : Segundo numero
    
    Retorna :
        float : Resultado de a ** b
    '''
    return a ** b

def modulo(a, b):
    '''
    Retorna el residuo de una operacion de cociente

    Parametros:
        a (float) : Primer numero
        b (float) : Segundo numero
    
    Retorna :
        float : Resultado de a % b
    '''
    return a % b
