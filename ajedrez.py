import random
import numpy as np
import math

tablero = np.array(([0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]))

ficha = int(input("¿Qué ficha desea simular? \n 1. Peon \n 2. Torre \n 3. Caballo \n 4. Alfil \n 5. Reina \n 6. Rey \n"))

#estas son las coordenadas aleatorias donde estará la ficha
a = random.randint(0,7) #coordenada a
b = random.randint(0,7) #coordenada b

fila = 0
columna = 0

print("Elemento en la fila: " + str(a) + " Columna: "+ str(b))

for elemento in np.nditer(tablero): #iteracion sobre los elementos del arreglo tablero
    if ficha ==1:
        if b==columna and (fila==a+1 or fila== a-1):
            tablero[fila][columna] = 1                                      # Condicional para la evaluacion del peon
    elif ficha == 2:
            if a==fila or b==columna:                                       # Condicional para la evaluacion de la torre
            tablero[fila][columna] = 1
    elif ficha == 3:
        if (a-fila)*(a-fila) +(b-columna)*(b-columna) == 5:                 # Condicional para la evaluacion del caballo
            tablero[fila][columna] = 1
    elif ficha == 4:
        if abs(a - fila) == abs(b - columna):                               # Condicional para la evaluacion del alfil
            tablero[fila][columna] = 1
    elif ficha == 5:
        if (a==fila) or (b==columna) or (abs(a-fila) == abs(b-columna)):    # Condicional para la evaluacion de la reina
            tablero[fila][columna] = 1
    elif ficha == 6:
        if (abs(a-fila)<=1) and (abs(b-columna) <=1):                       # Condicional para la evaluacion del rey
            tablero[fila][columna] = 1
    else:
        pass
    columna += 1
    if columna == 8:
        columna = 0;
        fila += 1

tablero[a][b] = 8 # ubicacion de la ficha

print(tablero)
class Ficha:
    nombre = str
    movimientos = tuple
