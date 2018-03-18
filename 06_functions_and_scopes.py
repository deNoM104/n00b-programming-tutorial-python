# Las funciones son la sal de la vida de la programación. Permiten escribir código complejo una vez y reutilizarlo varias veces.
# Así como en matemática, las funciones toman parámetros y devuelven valores.
# Por ejemplo, si tomamos el algoritmo para sumar los primeros n números naturales y lo queremos aplicar sobre dos números distintos
n = int(input('Hasta donde sumar? '));
suma = 0;
for i in range(1, n+1):
    suma = suma + i
print('La suma de los primeros', n, 'naturales da un total de', suma);

n = int(input('Hasta donde sumar ahora? '));
suma = 0;
for i in range(1, n+1):
    suma = suma + i
print('La suma de los primeros', n, 'naturales da ahora un total de', suma);
#
# Con funciones, en su lugar escribiremos el algoritmo una vez y lo usaremos dos veces
# Para definir una función se utiliza la palabra reservada DEF, un nombre y una lista de parámetros (valores que se le pasan a la función)
def sumaNatural(hastaDonde):
    sumaInterna = 0;
    for iterador in range(1, hastaDonde + 1):
        sumaInterna = sumaInterna + iterador

    return sumaInterna;

n = int(input('Hasta donde sumar? '));
suma = sumaNatural(n);
print('La suma de los primeros', n, 'naturales da un total de', suma);
n = int(input('Hasta donde sumar ahora? '));
sumaNatural(n);
print('La suma de los primeros', n, 'naturales da ahora un total de', suma);
# 
# Las funciones pueden tomar cualquier cantidad de parámetros, y hasta algunos opcionales
# Así como los parámetros son opcionales, también lo es la devolución de valores
def categoria(club, categoria):
    if club != 'BOCA':
        print(club, 'sos de la B');
    else:
        print(club, 'sos de la', categoria);
    return;

categoria('riber', 'a');
categoria('BOCA', 'A');

def categoria2(club, categoria = 'A'):
    if club != 'BOCA':
        print(club, 'sos de la B');
    else:
        print(club, 'sos de la', categoria);
    return;

categoria2('riber', 'A');
categoria2('BOCA');
#
# Podemos también llamar a funciones dentro de funciones, para hacer más sencilla la lectura
# Si por ejemplo tenemos una funcion que recorre un arreglo de naturales y devuelve la suma de los n primeros números naturales
def sumaFea(arreglo):
    for elemento in arreglo:
        sumaInterna = 0;
        for indice in range(1, elemento+1):
            sumaInterna = sumaInterna + indice;
        print('La suma de los primeros', elemento, 'naturales da un total de', sumaInterna);
    return;

muchos = range(1, 6);
sumaFea(muchos);
#
# Pero ya teníamos una función que realiza la suma natural de un número, así que podemos llamarla dentro de la propia función
def sumaFactorizada(arreglo):
    for elemento in arreglo:
        resultado = sumaNatural(elemento);
        print('La suma de los primeros', elemento, 'naturales da un total de', resultado);
    return;

sumaFactorizada(muchos);
#
# Veremos ahora el _scope_ de las variables
# Las variables definidas "en el aire" (fuera de funciones, ifs, ciclos, etc) se llaman variables GLOBALES