# En esta sección veremos distintas formas de dirigir nuestro código según enunciados lógicos (booleanos, vistos en la sección anterior)
# Lo primero que veremos son los saltos de control IF-THEN(-ELIF)-ELSE
# Cuando quiero realizar acciones dependiendo de ciertas condiciones, utilizamos la sentencia if
sosDeLaB = True;
cuadro = 'Rasin';
if sosDeLaB:
    cuadro = 'Riber';
print(cuadro, 'sos de la B');
# 
# La sentencia if agrega uno o más pasos dependiendo de si la condición se satisface.
# ACLARACIÓN de Python: el bloque de código que querramos agregar dentro del if debe estar indentado (separado del margen por una cierta cantidad de espacios).
padre = 'Atlanta';
if cuadro == 'Riber':
    padre = 'Boca';
    sosDeLaB = False;
#
# Si quiero mostrar un valor si se da la condicion lógica y otro distinto si NO se cumple, utilizo la palabra ELSE
if sosDeLaB:
    print(cuadro, 'siempre serás hijo de', padre);
else:
    print(padre, 'deja de mantener vagos como tu hijo', cuadro);
#
# Si hay muchas condiciones sobre un mismo y quiero evaluarlas, utilizo la palabra ELIF. 
# Es importante notar que se evalúan en el orden en que están escritas: si el primer IF no cumple, prueba el primer ELIF; si ese no cumple, prueba el segundo; y así hasta finalizar el bloque
# NOTA: vamos a utilizar la instrucción INPUT para tomar valores del teclado por consola
puntos = int(input('A cuántos puntos está tu equipo del puntero? '));
if puntos == 0:
    print('Felicitaciones! Sos del único grande!');
elif puntos < 10:
    print('Todavía podés entrar en la Libertadores');
elif puntos < 24:
    print('Podría ser peor');
else:
    print('jajajajajajaja');
#
# Veremos ahora los ciclos. Un ciclo es un conjunto de sentencias que se repiten mientras se dé una condición propuesta. Se utiliza el comando WHILE
while puntos > 0:
    print(puntos, 'acercándonos al puntero');
    puntos = puntos - 1;
print('A', puntos, 'del puntero');
#
# El ciclo WHILE se utiliza para ciclar en condiciones complejas
# Para ciclos en rangos (1..n), se utiliza el ciclo FOR
for x in range(1, 10):
    print('x =', x);
# Nótese que usamos la función RANGE para definir entre qué valores itera el ciclo. el rango x,y definido por la función se toma como [x,y)
# La sentencia FOR puede utilizarse para recorrer los elementos de una lista o arreglo
deLaB = [ 'San Lorenzo', 'Huracán', 'Racing', 'Independiente', 'Vélez', 'River'];
print('Los siguientes equipos han descendido');
for equipo in deLaB:
    print(equipo);
# Al igual que con los WHILEs, dentro de un mismo FOR se pueden realizar varias operaciones
suma = 0;
for i in range(1, 3):
    print('i =', i);
    suma = suma + i;
    print('suma:', suma);
print('suma:', suma);
#
# EJERCICIOS
# Para estos ejercicios utilizaremos la función INPUT para ingresar números desde el teclado
# SINTAXIS: int(input(texto));
# 1. Realizar un condicional que vaya a una u otra condición según el NÚMERO que ingrese el usuario
# 2. Realizar un condicional que muestre un texto si el NÚMERO ingresado es mayor a 10
# 3. Realizar un condicional que analice cinco opciones distintas a partir del NÚMERO ingresado
# 4. Realizar un ciclo que sume los primeros N números enteros, donde N es el NÚMERO ingresado
# 5. Realizar un ciclo que indique si el NÚMERO ingresado es PRIMO