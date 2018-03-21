# En esta oportunidad veremos dos tipos nuevos de datos:
# * Los arrays
# * Los booleanos
#
# Los arrays son cadenas -o listas- de datos. Se definen con la notación [] y se separan los datos con coma.
# cadenaDePalabras = ['Hola', 'Alejo', '¿Cómo estás?']
# Para uhu acceder a los valores guardados en la lista, se utiliza el índice del valor (comenzando por cero)
# Por ejemplo, para leer el valor "Alejo", utilizamos el comando
# cadenaDePalabras[1]
# Es el segundo valor de la lista, pero los índices comienzan en 0
#
# De la misma manera que se acceden a los valores, se los puede modificar
cadenaDePalabras = ['Hola', 'Alejo', '¿Cómo estás?'];
print(cadenaDePalabras)
cadenaDePalabras[2] = '¿Te sacaste la mancha?'
print(cadenaDePalabras)
#
# Ahora bien, si quiero agregar un valor a la lista, tengo varias opciones:
# Si quiero agregarlo al final de la lista, utilizo el comando "append(item)"
cadenaDePalabras.append('No, esa mancha no se quita');
print(cadenaDePalabras);
#
# Si quiero agregarlo en otra posicion, utilizo el comando insert(index, item)	
# OJO: el índice que le pases tiene que estar dentro de la longitud de la lista
cadenaDePalabras.insert(2, 'backyardigans rulz');
print(cadenaDePalabras);
#
# Si querés saber la longitud de la cadena, usás la función "len(lista)"
# Tené en cuenta que esta función toma cantidad de elementos 
# (los de la lista, que se separan con coma), no de palabras
print(len(cadenaDePalabras));
#
# El otro tipo de dato que vemos hoy es el booleano (nombrado así por George Bool... Googlealo).
# El tipo de dato se utiliza para realizar operaciones lógicas, donde el resultado es verdadero o falso
verdadero = 1 == 1;
print(verdadero);
falso = 1 == 2;
print(falso);
#
# True quiere decir verdadero
# False, falso
# En el ejemplo anterior se utilizó la función de igualdad (==). 
# No confundir con la asignación de variables (un único =).
# Otros operadores: 
# a < b es True si a es menor a b
# a > b es True si a es mayor a b
# a <= b es True si a es menor o igual a b
# a >= b es True si a es mayor o igual a b
#
# Una vez que tenemos un valor booleano, podemos realizar operaciones lógicas
# a and b es True si a es True y b es True
# a or b es True si a es True o b es True
# not(a) es True si a es False	
print('Verdadero and Verdadero:');																
print(verdadero and verdadero)
print('Verdadero and Falso:');
print(verdadero and falso);
print('Falso and Falso:');
print(falso and falso);
print('Verdadero or Verdadero:');																
print(verdadero or verdadero)
print('Verdadero or Falso:');
print(verdadero or falso);
print('Falso or Falso:');
print(falso or falso);
print('not(Verdadero):');
print(not(verdadero));
print('not(Falso):');
print(not(falso));
#
# Ahora sí, ejercicios:
# 1. Crear una lista de palabras que hagan referencia al 26 de junio de 2011 y mostrarlo por pantalla
# 2. Crear una lista vacía e imprimirla en pantalla
# 3. Agregar al final de la lista vacía del punto anterior 
#    una serie de números pares ordenados y mostrarlos en pantalla
# 4. En la lista del punto 3, entre cada número par insertar un número impar que vaya (numéricamente) entre ellos
# 5. Definir una variable booleana para saber si dos es menor a uno e imprimirla por pantalla
# 6. Definir una variable booleana para saber si uno es menos a dos Y si dos es menor a tres e imprimirla por pantalla
# 7. Definir una variable booleana para saber si tres es menos a dos o uno es menor a cero e imprimirla por pantalla