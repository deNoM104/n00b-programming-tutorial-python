# Las funciones son la sal de la vida de la programación. Permiten escribir código complejo una vez y reutilizarlo varias veces
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

    print('La suma de los primeros', hastaDonde, 'naturales da un total de', sumaInterna);

    return sumaInterna;

n = int(input('Hasta donde sumar? '));
sumaNatural(n);
n = int(input('Hasta donde sumar ahora? '));
sumaNatural(n);