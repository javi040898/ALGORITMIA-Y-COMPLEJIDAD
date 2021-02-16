
import random


#Apartado a
def generar_aleatorios():
    numeros = []
    for i in range(0,11): #Se generan 11 numeros aleatorios del 1 al 10 y se introducen en una lista
        valor = (random.randint(1,11))
        numeros.append(valor)
    return numeros

#Apartado b
#Se pone 99 cuando para cuando no se conectan y 0 para el mismo
#Se inicializa el grafo pedido con las letras
#La matriz se interpreta de la siguiente manera
# 1 2 3 4 5 6 7
#1
#2
#3
#4
#5
#6
#7
matriz_grafo_distancias = [
                ["0","d","99","99","99","c","99"],
                ["99","0","h","i","g","99","99"],
                ["99","99","0","99","99","99","99"],
                ["99","99","k","0","99","99","99"],
                ["99","g","99","j","0","99","99"],
                ["c","e","99","99","f","0","99"],
                ["a","99","99","99","99","b","0"]]

#Funcion que sustituye las letras por los numeros aleatorios generados anteriormente
def susituir_letras(matriz,numeros):
    contador = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if(matriz[i][j] != "99" and matriz[j][i] != "0"): #Si es una letra se sustituye por el primer numero de la lista
                matriz[i][j] = numeros[contador]

                if(matriz[j][i] != "99" ): #Si su opuesto tambien tiene el mismo valor, se susituye por el mismo (casos 1,6 y 2,5)
                    matriz[j][i] = numeros[contador]
                    contador -= 1
                contador += 1

    convertir_entero(matriz) #Se convierten en enterios los numeros, ya que se inicializan como un string
    print("Matriz de distancias inicial, con los numeros aleatorios: ")
    mostrar_matriz(matriz)
    print("")
    return matriz

#Funcion auxiliar que convierte en enteros los numeros de la matriz
def convertir_entero(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz


#Apartado c
#Algoritmo de Floyd, se calculan las distancias minimas comparando las filas y las columnas simetricas
#Devuelve la matriz de distancias minimas
def distancias_minimas(matriz):
    for i in range(0,len(matriz)): #Recorre las filas y columnas simetricas que se tienen que sumar
        for j in range(0,len(matriz[i])): #Recorre la fila cuando se empieza a comparar
            for k in range(0, len(matriz[i])): #Recorre el valor con el que se compara la suma simetrica
                print("Compara ", matriz[j][i], "(de la posicion",j,",",i,")", "+",matriz[i][k], "(de la posicion",i,",",k,")", "con ",matriz[j][k], "(de la posicion",j,",",k,")",)
                if((matriz[j][i]+matriz[i][k]) < matriz[j][k]): #Si es menor, se sustituye
                    print("Al ser menor",matriz[j][i], "+",matriz[i][k], ", lo intercambia"," y el valor nuevo es",matriz[j][i]+matriz[i][k])
                    matriz[j][k] = matriz[j][i]+matriz[i][k]
                mostrar_matriz(matriz)
                print("")

    print("Matriz distancias minimas: ")
    mostrar_matriz(matriz)
    return matriz

#Funcion para mostrar la matriz en forma de matriz
def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

matriz_inicial = (susituir_letras(matriz_grafo_distancias,generar_aleatorios()))
distancias_minimas(matriz_inicial)




