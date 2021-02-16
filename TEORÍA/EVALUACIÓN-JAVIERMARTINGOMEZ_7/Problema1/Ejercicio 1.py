import math



#Funcion que introduce en una lista los mini grafos que se puede hacer con cada nodo
def mini_grafos(matriz):
    grafos = []
    for i in range(len(matriz)):
        grafo = [i]
        for j in range(len(matriz[i])):
            if(matriz[i][j] == 1):
                grafo.append(j)
        grafos.append(grafo)
    return grafos


def formar_grafos(matriz):
    lista_grafos = mini_grafos(matriz)
    j = 0
    while(j <= len(lista_grafos)-1): #Recorremos la lista con los mini grafos
        i = 0
        while(i != len(lista_grafos[j]) and j != len(lista_grafos)-1): #Recorremos cada grafo

            if(lista_grafos[j][i] in lista_grafos[j+1]): #Si el valor de un grafo esta en otro, significa que es un grafo
                lista_grafos[j] = lista_grafos[j] + lista_grafos[j+1] #Se unen los dos grafos
                lista_grafos[j] = list(set(lista_grafos[j])) #Eliminamos los repetidos
                lista_grafos.pop(j+1) #Se elimina el otro grafo, ya que forma parte del otro
                i = 0 #Es cero ya que empieza a comprobar desde el principio
            else:
                i += 1
        j += 1
    return lista_grafos


def grado_conexion(matriz):
    grafos = formar_grafos(matriz)

    return len(grafos)/len(matriz)

#Funcion para leer archivo y que lo transforme en una lista, ya que solo se pueden leer strings
def leer_archivo(archivo):
    text_file = open(archivo)
    matriz_sin_dividir = text_file.read().split(',')
    matriz = []
    for i in range(len(matriz_sin_dividir)):
        matriz_sin_dividir[i] = int(matriz_sin_dividir[i])
    j = 0
    fila = []
    dimensiones = int(math.sqrt(len(matriz_sin_dividir))) #Calculamos las dimensiones para hacer las filas
    for i in range(0,len(matriz_sin_dividir)-1,dimensiones): #Si por ejemplo la matriz tiene longitud de 36, sera una matriz 6x6
        while(len(fila) != dimensiones):
            fila = fila + [matriz_sin_dividir[j]]
            j += 1
        matriz = matriz + [fila]
        fila = []

    return matriz


f = open('salida_voraz3.txt', 'w')
matriz_salida = (leer_archivo('ejemplo_voraz3.txt'))
f.write("Numero de grupos: "+ str(len(formar_grafos(matriz_salida)))+ "\n")
f.write("Grupos: " + str(formar_grafos(matriz_salida))+ "\n")
f.write("Grado de conexion: "+str(grado_conexion(matriz_salida)))
f.close()




