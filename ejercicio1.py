# Se asume A y B sin cero, no vacias, que consisten en N enteros.
# Se asume N y M son numeros enteros dentro del intervalo [1, 30.000].
# Cada elemento en A, B y C son numeros enteros en [1, 2 * M]
# A[K] <= B [K].

def solucion(A, B, C): # Se reciben los 3 arrays iniciales: tablones A, tablones B y Clavos
    final = len(C)
    inicio = 0
    resultado = -1 
    while final >= inicio: # Busqueda binaria para no recorrer secuencialmente y reducir el tiempo 50%
        mitad = (inicio + final) / 2
        if checkear(A, B, C, mitad):
            final = mitad - 1
            resultado = mitad
        else:
            inicio = mitad + 1
    return resultado


def checkear(A, B, C, M): # Funcion que pide la consigna con los 4 parametros de entrada A, B, C y M
    clavos = [0] * 2 * ( len(C) + 1 )
    for I in range(0, M):
        clavos[C[I]] += 1
    for I in range(1, len(clavos)):
        clavos[I] += clavos[I - 1]
    for I in range(len(A)):
        if (clavos[B[I]] - clavos[A[I]-1]) == 0:
            return False
    return True

# Caso de prueba brindado
print(solucion([1,4,5,8], [4,5,9,10], [4,6,7,10,2]))
