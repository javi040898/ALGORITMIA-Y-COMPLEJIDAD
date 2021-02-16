


#Funcion donde aplicamos el movimiento en L del caballo para ver, si partiendo de la posicion inicial dada es capaz de llegar a la posicion final dada
def movimiento_valido(fila_inicial, columna_inicial, fila_final, columna_final):

    if (abs(fila_final - fila_inicial) == 1 and abs(columna_final - columna_inicial) == 2):
        return True

    elif (abs(fila_final - fila_inicial) == 2 and abs(columna_final - columna_inicial) == 1):
        return True

    else:
        return False

#Funcion que decide si el caballo puede llegar a todas las posiciones o no
def posiciones_caballo(tablero, fila_inicial, columna_inicial, num_movimientos):
    mostrar_tablero(tablero)
    if (num_movimientos == len(tablero) * len(tablero[0])): #Si el numero de movimientos (de 1s) es igual a las dimensiones del tablero, el tablero tiene solución
        return True

    for fila in range(filas): #Se cada posicion del tablero
        for columna in range(columnas):
            if (movimiento_valido(fila_inicial, columna_inicial, fila, columna) and tablero[fila][columna] == 0): #Si podemos realizar ese movimiento y no se ha visitado aun

                tablero[fila][columna] = 1  #La posicion pasa a ser visitada
                tablero_recorrido = posiciones_caballo(tablero, fila, columna, num_movimientos+1) #Llamamos a la funcion recursivamente con la posicion donde esta actualmente el caballo

                if (tablero_recorrido): #Si a partir de esa posicion se llega a una solucion, devuelve true
                    return True
                else:
                    tablero[fila][columna] = 0 #Si no, la marca como no visitada
    return False

def mostrar_tablero(matriz):
    for i in matriz:
        print(i)
    print("")




filas = 3
columnas = 3
fila_inicial = 0
columna_inicial = 0

tablero = [[0 for columna in range(columnas)] for fila in range(filas)]


tablero[fila_inicial][columna_inicial] = 1 #La posicion inicial se marca como visitada
salida = posiciones_caballo(tablero, fila_inicial, columna_inicial, 1)

if(salida):
    print("Solucion encontrada")
else:
    print("Solucion no encontrada")




