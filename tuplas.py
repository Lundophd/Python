#tuplas
print("Hola!! este programa muestra las 10 primera posicione y solo muestra las pares")

def filtrar_pares(numeros):
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        
    return pares
    
tuple_numeros = tuple(range(1,10))
print(type(tuple_numeros))
resultado = filtrar_pares(tuple_numeros)
print(resultado)

