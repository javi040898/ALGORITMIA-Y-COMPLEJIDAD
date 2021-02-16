

def obtener_valor_optimo(maximo_peso, lista_pesos, lista_valores): #Funcion que obtiene el valor optimo de la mochila y los objetos usados para ese valor

    matriz = [[0 for i in range(maximo_peso + 1)] #Se inicializa la matriz llena de 0s
              for j in range(len(lista_pesos) + 1)]

    for i in range(0,len(lista_pesos) + 1): #Se va rellenando la matriz con los valores y pesos

        for j in range(0,maximo_peso + 1):
            if i == 0 or j == 0:
                matriz[i][j] = 0

            elif lista_pesos[i - 1] <= j: #Si el nuevo objeto tiene menos peso que el maximo
                matriz[i][j] = max(matriz[i - 1][j],lista_valores[i - 1] + matriz[i - 1][j - lista_pesos[i - 1]]) #Miro el maximo entre entre el valor actual
                                                                                                                 #y el nuevo, para ver cual es mejor para quedarme

            else: #Si el peso es superior al maximo, me quedo como estaba
                matriz[i][j] = matriz[i - 1][j]

    mochila = [] #Lista de valores que se han utilizado, usando el peso de los elementos utilizados.


    resultado = matriz[len(lista_pesos)][maximo_peso] #Variable que almacena el mejor valor
    peso_actual = maximo_peso #Variable que va almacenando el peso

    for i in range(len(lista_pesos), 0, -1): #De fin a principio, para ir viendo si tienen el mismo valor (se usa ese objeto)

        if (resultado <= 0): #Como vamos restando, si llega a 0, salimos del bucle
            break
        if (resultado == matriz[i - 1][peso_actual]): #Si el resultado es igual al valor de la fila anterior, tiene que seguir buscando en las anteriores filas
            continue
        else: #Si no es igual, es obvio que ese elemento se ha tenido que usar, por lo que restamos el valor al resultado, y lo annadimos a la mochila
            resultado = resultado - lista_valores[i - 1]
            mochila.append(lista_pesos[i - 1])
            peso_actual = peso_actual - lista_pesos[i - 1]

    mostrar_matriz(matriz)
    return matriz[len(lista_pesos)][maximo_peso], mochila

def mostrar_matriz(matriz):
    for i in matriz:
        print(matriz)



#Funcion auxiliar que nos dice cuales son los elementos que no se han usado en la primera mochila
def elementos_restantes(mochila, lista_pesos, lista_valores):
    for i in range(len(mochila)):
        indice = lista_pesos.index(mochila[i])
        lista_pesos.pop(indice)
        lista_valores.pop(indice)



def valores_dos_mochilas(limite_mochila1, limite_mochila2, lista_pesos, lista_valores): #Esta funcion obtiene los resultados de las dos mochilas

    aux = limite_mochila1
    limite_mochila1 = max(limite_mochila1, limite_mochila2) #Esto hace que la mochila 1 sea la de mas peso para facilitarnos el trabajo
    limite_mochila2 = max(aux, limite_mochila2)

    valor_mochila1, mochila1 = obtener_valor_optimo(limite_mochila1, lista_pesos, lista_valores) #Se obtiene el valor optimo de la mochila

    elementos_restantes(mochila1, lista_pesos, lista_valores) #Mira los elementos restantes que se pueden introducir en la mochila 2

    valor_mochila2, mochila2 = obtener_valor_optimo(limite_mochila2, lista_pesos, lista_valores) #Valor optimo de la segunda mochila

    return valor_mochila1, valor_mochila2


listaPeso = [1,2,5,6,7]#Se inicializa cada lista y cada posicion de cada una se relaciona con la posicion de la otra
listaValores = [1,6,18,22,28]

listaPeso2 = [5,7,9,1,3]
listaValores2 = [10,10,23,7,8]


m1, m2 = valores_dos_mochilas(11, 8, listaPeso, listaValores)
m21,m22 = valores_dos_mochilas(14, 12, listaPeso2, listaValores2)

print(obtener_valor_optimo(7,listaPeso,listaValores))


#print("Valor optimo de la mochila 1: ", m1)
#print("Valor optimo de la mochila 2: ", m2)

#print("Valor optimo de la mochila 1: ", m21)
#print("Valor optimo de la mochila 2: ", m22)
