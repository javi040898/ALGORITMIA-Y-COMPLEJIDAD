


f = open('salida_backtracking4.txt', 'w')

def posiciones_camion(camino, fila_inicial, columna_inicial,mirada):
    camino_posible = False
    if (mirada == 4):
        mirada = 0  # Si llega a 4 ha dado una vuelta completa y vuelve a la mirada inicial
    if(camino[fila_inicial][columna_inicial] == '2'):
        return True
    else:
        if(mirada == 0): #Izquierda
            if(columna_inicial != 0): #Puede ir recto
                if (camino[fila_inicial][columna_inicial - 1] != 'X'):  # Si puede llegar a esa posicion yendo recto
                    camino_posible = posiciones_camion(camino, fila_inicial, columna_inicial - 1, mirada)
                if (camino_posible):
                    f.write("Va recto desde la posicion "+ str(fila_inicial)+str(columna_inicial)+ " hasta la "+ str(fila_inicial)+str(columna_inicial-1) +"\n")
                    return True
            if(fila_inicial != 0):
                if(camino[fila_inicial - 1][columna_inicial] != 'X'):  # Si puede llegar a esa posicion girando a la derecha
                    camino_posible = posiciones_camion(camino, fila_inicial - 1, columna_inicial, mirada + 1)
                if (camino_posible):
                    f.write("Gira a la derecha desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+ " hasta la "+str(fila_inicial-1)+ str(columna_inicial) +"\n")
                    return True
        elif(mirada == 1):  # Arriba
            if (fila_inicial != 0):
                if (camino[fila_inicial - 1][columna_inicial] != 'X'):  # Si puede llegar a esa posicion yendo recto
                    camino_posible = posiciones_camion(camino, fila_inicial - 1, columna_inicial, mirada)
                if (camino_posible):
                    f.write("Va recto desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+ " hasta la "+str(fila_inicial-1)+ str(columna_inicial) +"\n")
                    return True
            if(columna_inicial != len(camino[fila_inicial])-1):
                if (camino[fila_inicial][columna_inicial + 1] != 'X'):
                    camino_posible = posiciones_camion(camino, fila_inicial, columna_inicial + 1, mirada + 1)
                if (camino_posible):
                    f.write("Gira a la derecha desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+" hasta la "+str(fila_inicial)+ str(columna_inicial+1) +"\n")
                    return True
        elif (mirada == 2):  # Derecha
            if (columna_inicial != len(camino[fila_inicial])-1):
                if (camino[fila_inicial][columna_inicial + 1] != 'X'):  # Si puede llegar a esa posicion yendo recto
                    camino_posible = posiciones_camion(camino, fila_inicial, columna_inicial + 1, mirada)
                if (camino_posible):
                    f.write("Va recto desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+ " hasta la "+str(fila_inicial)+ str(columna_inicial + 1) +"\n")
                    return True
            if(fila_inicial != len(camino)-1):
                if (camino[fila_inicial + 1][columna_inicial] != 'X'):
                    camino_posible = posiciones_camion(camino, fila_inicial + 1, columna_inicial, mirada + 1)
                if (camino_posible):
                    f.write("Gira a la derecha desde la posicion "+ str(fila_inicial)+str(columna_inicial)+ " hasta la "+str(fila_inicial+1)+ str(columna_inicial) +"\n")
                    return True
        elif (mirada == 3):  # Abajo
            if (fila_inicial != len(camino)-1):
                if (camino[fila_inicial + 1][columna_inicial] != 'X'):  # Si puede llegar a esa posicion yendo recto
                    camino_posible = posiciones_camion(camino, fila_inicial + 1, columna_inicial, mirada)
                if (camino_posible):
                    f.write("Va recto desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+ " hasta la "+ str(fila_inicial+1)+ str(columna_inicial) +"\n")
                    return True
            if(columna_inicial != 0): #No puede ir recto
                if (camino[fila_inicial][columna_inicial - 1] != 'X'):
                    camino_posible = posiciones_camion(camino, fila_inicial, columna_inicial - 1, mirada + 1)
                if (camino_posible):
                    f.write("Gira a la derecha desde la posicion "+ str(fila_inicial)+ str(columna_inicial)+ " hasta la "+str(fila_inicial)+ str(columna_inicial-1) +"\n")
                    return True
    return False


def filaInicial(camino):
    for fila in range(0, len(camino)):
        for columna in range(0, len(camino[fila])):
            if(camino[fila][columna] == '1'):
                return fila
def columnaInicial(camino):
    for fila in range(0, len(camino)):
        for columna in range(0, len(camino[fila])):
            if (camino[fila][columna] == '1'):
                return columna

def leer_archivo(archivo):
    f = open(archivo)
    i = 0
    filas = 0
    columnas = 0
    matriz = []
    for linea in f:
        if(i == 0):
            filas = int(linea)
        elif(i == 1):
            columnas = int(linea)
        else:
            matriz += linea.split('\t')
        i += 1

    while('\n' in matriz):
        matriz.remove('\n')

    j = 0
    fila = []
    matriz_final = []
    for i in range(0, len(matriz) - 1,columnas):  # Si por ejemplo la matriz tiene longitud de 36, sera una matriz 6x6
        while (len(fila) != columnas):
            fila = fila + [matriz[j]]
            j += 1
        matriz_final = matriz_final + [fila]
        fila = []

    return matriz_final


camino = leer_archivo('ejemplo_backtracking4.txt')

fila_ini = filaInicial(camino)
columna_ini = columnaInicial(camino)


if(posiciones_camion(camino,fila_ini,columna_ini,0)):
    f.write("Empieza en la posicion: " + str(fila_ini) + str(columna_ini) + "\n")
    f.write("Solucion encontrada" + "\n")
else:
    f.write("Empieza en la posicion: " + str(fila_ini) + str(columna_ini) + "\n")
    f.write("Solucion no encontrada" + "\n")
