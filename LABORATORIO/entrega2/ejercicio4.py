import random

#Matrices costes de ejemplo
#99 es el infinito, es decir, no hay conexion entre los nodos

matriz_costes2=[[1,2,3,4,5,6,7],
            [1,99,3,99,4,99,99,99],
            [2,2,99,2,6,4,99,99],
            [3,99,2,99,99,5,6,99],
            [4,4,6,99,99,3,99,4],
            [5,99,4,5,3,99,8,7],
            [6,99,99,6,99,8,99,3],
            [7,99,99,99,4,7,3,99]]

matriz_costes=[[1,2,3,4,5,6,7],
            [1,99,1,99,4,99,99,99],
            [2,1,99,2,6,4,99,99],
            [3,99,2,99,99,5,6,99],
            [4,4,6,99,99,3,99,4],
            [5,99,4,5,3,99,8,7],
            [6,99,99,6,99,8,99,3],
            [7,99,99,99,4,7,3,99]]

matriz_costes3=[[1,2,3,4,5,6,7],
            [1,99,3,99,99,5,1,99],
            [2,3,99,1,2,4,99,99],
            [3,99,1,99,3,99,99,99],
            [4,99,2,3,99,99,99,99],
            [5,5,4,5,99,99,2,3],
            [6,1,99,99,99,2,99,99],
            [7,99,99,99,99,3,99,99]]


"""funcion auxiliar para saber que nodo
tiene el minimo coste con sus nodos conexos
"""
def posicionMinimo(matriz,listaVisitados):
    minimo=matriz[1][1] #primer coste
    for i in listaVisitados: #recorremos los nodos en el camino
        for j in range(1,int(len(matriz[i]))):
            if(minimo>matriz[i][j]):
                minimo=matriz[i][j]
                posicion=i
    return posicion            


def prim(n,matriz):#n es el numero de nodos
    actual=random.randint(1, n)#coge de inicio un numero random
    print("Nodo inicial: ",actual)
    camino=[actual]#el camino que seguiremos donde introduciremos el nodo inicial
    posicion=0
    coste=0
    while(len(camino) < n):
        minimo=matriz[actual][1] #la posicion del primer coste
        posicion=1 #al empezar a comprobar el minimo desde el primer coste, puede que no entre al if porque el minimo este en la posicion 1
        for i in range(1,int(len(matriz[actual]))):
            if(minimo>matriz[actual][i]): #comprobamos el minimo de la fila
                minimo=matriz[actual][i]
                posicion=i #guardamos la posicion del minimo para ver con que nodo conecta
        if(posicion in camino):#si ya se ha visitado el nodo
            matriz[actual][posicion]=99#si ya ha sido visitado se pone 99 en la posicion
        else:
            print("Se unen los nodos: ",matriz.index(matriz[actual])," y ",posicion)
            coste+=matriz[actual][posicion] #sumamos el coste de la conexion
            print("Coste actual: ", coste)
            camino.append(posicion) #insertamos el nodo visitado en el camino
            print("Nodos visitados: ",camino)
        #se comprueba cual es el nodo visitado que tiene el valor minimo
        actual=posicionMinimo(matriz,camino)#saber minimo de todos los visitados
    retorno= "Orden de visita de los nodos: "+str(camino)+" con coste: "+str(coste)
    
    return retorno


print(prim(7,matriz_costes))





