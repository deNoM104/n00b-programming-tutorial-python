# Las variables son elementos que almacenan y editan valores
# Una variable se utiliza para definir el comportamiento o resultado de una función u operación.
# Para declarar una variable, simplemente debés definir un nombre y asignarle un valor con el operador =
pipo = 3
print('El valor de pipo es: ')
print(pipo)
# El valor de una variable puede variar, como bien lo indica su nombre.
# Simplemente se le asigna un nuevo valor con el mismo operador de antes (=)
pipo = 4
print('El valor de pipo es: ') 
print(pipo)
# El tipo de una variable depende del valor asignado. Si se le asigna un número, será una variable numérica;
# Si se le asigna texto, será una variable de texto.
pipo = 'tu madre'
print('Una respuesta ingeniosa?')
print(pipo) # Futurama...
#
# Sobre las variables numéricas se pueden realizar operaciones aritméticas.
# SUMA con el operador + ej: 1 + 2
# RESTA con el operador - ej: 2 - 1
# MULTIPLICACIÓN con el operador * ej: 3 * 4
# DIVISIÓN con el operador / ej: 12 / 3
denom = 10
print(denom)
print(denom - 8) # Al no usar la asignacion, el valor de denom no se modifica
denom = denom - 9
print(denom) # Acá sí se modificó el valor de la variable
bakka = denom + 19
print(bakka)
#
# A las variables de texto sólo se les puede "sumar" más texto (concatenar)
kokoro = 'Mi vecino es '
print(kokoro)
totoro = "Totoro!"
kokoro = kokoro + totoro
print(kokoro)
#
# Es importante notar que no se deben mezclar tipos de variable.
# La operación
# denom = denom + kokoro
# devolvería un error
#
# Ahora sí, los ejercicios
# 1. Definí una variable e imprimí en pantalla su valor
# 2. Cambiá el valor de la variable e imprimí el nuevo valor en pantalla
# 3. Definí una variable NUMÉRICA e imprimí el valor en pantalla
# 4. Realizá operaciones aritméticas sobre la variable e imprimí los nuevos valores
# 5. Definí una variable de texto e imprimila por pantalla
# 6. Concatenale texto SIN ASIGNAR el nuevo valor y mostralo por pantalla
# 7. Concatenale texto ASIGNANDO a la variable y mostrala por pantalla