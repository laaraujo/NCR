# Se asume que el segundo parametro es de longitud inferior al primero
# No debe haber distincion entre mayusculas

def solucion(cadena, subcadena): # Rebice 2 cadenas de caracteres
	cadena = cadena.lower() # pasa a minusculas.
	subcadena = subcadena.lower() # pasa a minusculas.
	longitud = len(subcadena)
	indice_maximo = len(cadena) - longitud + 1
	resultado = 0
	for indice in range(0, indice_maximo): # Se recorre cadena hasta que no alcance la cantidad de caracteres.
		if checkear_anagrama(subcadena, cadena[ indice : indice + longitud]):
			resultado += 1
	return resultado

def checkear_anagrama(original, nuevo): # Toma dos strings a comparar (y ver si son anagramas al mismo tiempo).
	original = sorted(list(original))
	nuevo = sorted(list(nuevo))
	return True if sorted(original) == sorted(nuevo) else False # No se buscan anagramas, simplemente se ordenan los caracteres y se compara el resultado.

# Caso de prueba brindado
print(solucion('hola, que buena ola Laomir', 'OAL'))








	

		
			

