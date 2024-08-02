def operation_selector(num1, num2, op):
    """
    Realiza una operación aritmética o bit a bit entre dos números enteros.

    Parámetros:
    num1 (int): El primer número entero.
    num2 (int): El segundo número entero.
    op (str): El operador que define la operación a realizar.
              Puede ser '+', '-', '*', '&'.

    Retorna:
    tuple: Un código de estado (0 para éxito, otro valor para error)
           y el resultado de la operación o None en caso de error.

    Objetivo de la función: Verifica que los parámetros sean del tipo correcto.
    Realiza la operación correspondiente según el operador proporcionado.
    """
    # Verificar que num1 y num2 sean enteros y no sean True, False o None
    if not isinstance(num1, int) or not isinstance(num2, int) or \
       num1 in [True, False] or num2 in [True, False]:
        return -50, None  # Código de error único para parámetros no enteros

    # Verificar que op sea un string y no sea None
    if not isinstance(op, str) or op is None:
        return -60, None  # Código de error único para op no string

    # Verificar que op sea una de las opciones permitidas
    if op not in ['+', '-', '*', '&']:
        return -70, None  # Código de error único para op no válido

    # Realizar la operación según el carácter op
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2

    return 0, result  # Código de éxito y resultado de la operación

'''Calcula el promedio de todos los valores que están en la lista.

Parámetros:
    lista_numeros:espera que sea una lista (o una secuencia) que
    contenga números, ya sean enteros o flotantes.
    Retorna:retorna una tupla con dos valores que depende de las
    condiciones verificadas en el código,(-80 o -90 según el error
    de verificacion, o el promedio de todos los valores)

    Objetivo de la función:Calcula el promedio de todos los
    valores que están en la lista, verificando que el parámetro
    de entrada sea un número, puede ser positivo, negativo,
    decimal, etc y que el tamaño de la lista no sea mayor a 10
    elementos.

'''
def calculo_promedio(lista_numeros):
    # Verifica que los elementos de la lista sean números(enteros o flotantes)
    for valor in lista_numeros:
        if type(valor) not in (int, float):
            return -80, None
    # Verifica que el tamaño de la lista no sea mayor a 10 elementos
    if len(lista_numeros) > 10:
        return -90, None
    # Calcula el promedio de los valores en la lista
    if lista_numeros:
        promedio = sum(lista_numeros) / len(lista_numeros)
    else:
        promedio = 0
    return 0, promedio
