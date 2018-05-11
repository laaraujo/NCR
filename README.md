# NCR
Evaluación técnica para Ingresantes - Diciembre 2017

Acerca del método de evaluación

Los problemas y requisitos que se detallan a continuación son solamente de carácter opcional. El
postulante tendrá la opción de elegir cuales resolver y aún sin ser excluyentes para la contratación,
es un plus a la hora de la decisión final.
Se podrán resolver en cualquier lenguaje y plataforma y el entregable deberá ser solo el código y
una descripción de las herramientas utilizadas. Ej (se resolvió con C# bajo .NET 4.5)
Happy coding!

Clavando tablones
Se le dan dos arreglos A y B sin cero, no vacías, que consisten en N enteros.

Estos arreglos representan N tablones. Más precisamente, A [K] es el comienzo y B [K] el final del K-
ésimo tablón.

A continuación, se le da un arreglo no vacía cero-indexado C que consta de M enteros. Este arreglo
representa M clavos.
Más precisamente, C [I] es la posición donde se puede martillar en el clavo I-ésimo.
Decimos que un tablón (A [K], B [K]) es clavado si existe un clavo C [I] tal que A [K] ≤ C [I] ≤ B [K].
El objetivo es encontrar el número mínimo de clavos que deben utilizarse hasta que todos los tablones
estén clavados.
En otras palabras, debe encontrar un valor J tal que todos los tablones serán clavados después de usar sólo
los primeros clavos.
Más exactamente, para cada tablón (A [K], B [K]) tal que 0 ≤ K <N, debería existir un clavo C [I] tal que
I <J y A [K] ≤ C [I] ≤ B [K].
Por ejemplo, dados los arreglos:
A[0] = 1 B[0] = 4
A[1] = 4 B[1] = 5
A[2] = 5 B[2] = 9
A[3] = 8 B[3] = 10
Se pueden representar 4 tablones: [1, 4], [4, 5], [5, 9] y [8, 10].
Dado el arreglo C:
C[0] = 4
C[1] = 6
C[2] = 7
C[3] = 10
C[4] = 2
Si usamos los siguientes clavos:
0, entonces los tablones [1, 4] y [4, 5] serán clavados.
0, 1, entonces los tablones [1, 4], [4, 5] y [5, 9] serán clavados.
0, 1, 2, entonces los tablones [1, 4], [4, 5] y [5, 9] serán clavados.
0, 1, 2, 3, entonces todos los tablones serán clavados.
Así, cuatro es el número mínimo de clavos que, usados secuencialmente, permiten que todos los tablones
sean clavados.
Escribir una función:
int solution (int A [], int B [], int N, int C [], int M);
que, dada dos arreglos A y B no vacías de índice cero que consisten en N enteros y un arreglo C cero no
vacía compuesta por M enteros,
devuelve el número mínimo de clavos que, usados secuencialmente, permiten que todos los tablones sean
clavados.
Si no es posible clavar todos los tablones, la función debe devolver -1.
Por ejemplo, dados los conjuntos A, B, C tales que:
A[0] = 1 B[0] = 4
A[1] = 4 B[1] = 5
A[2] = 5 B[2] = 9
A[3] = 8 B[3] = 10
C[0] = 4
C[1] = 6
C[2] = 7
C[3] = 10
C[4] = 2
La función debe devolver 4, como se explicó anteriormente.
Asumir que:
N y M son números enteros dentro del intervalo [1, 30.000];
Cada elemento de los arreglos A, B, C es un número entero dentro del rango [1, 2 *
M]; A [K] ≤ B [K].

Buscando anagramas
Se provee una cadena de caracteres de largo N y una subcadena de largo M. Se desea saber cuántas veces
aparece la subcadena o un anagrama de la misma dentro de la cadena principal.

Por ejemplo, si se tiene la cadena A y la subcadena B
A = “hola, que buena ola Laomir”
B = “OAL”
El resultado deberá ser 3, dado lo siguiente
A = “hola, que buena ola Laomir”
Escribir una función
Int solution(string A, string B)
que devuelva la cantidad de veces que aparece B en A, o un anagrama de B en A.

Asumir:
No hay distinción entre mayúsculas y
minúsculas N > M.

Diagrama de secuencia
Considere una transacción de extracción de efectivo mediante un cajero automático.
Presentar un diagrama de secuencia que sirva para sistematizar dicha transacción. Tener en
cuenta los posibles errores que puedan surgir.

Diagrama de clases
Se necesita modelar una capa de usuarios en donde cada usuario puede tener permisos
exclusivos para utilizar determinados servicios del sistema. El usuario con perfil “superusuario”
podrá cargar usuarios y perfiles y asignar responsabilidades; entre ellas puede asignar la
responsabilidad de crear usarios y de asignar responsabilidades. Se pide un diagrama de clases
que solucione este requisito.
