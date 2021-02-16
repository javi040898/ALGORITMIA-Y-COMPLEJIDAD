

A = [1,1,1,1,1,0,0,0,1,1,1,1,1,0]
B = [0,0,0,1,1,1,1,0,1]

a=[0,1,0]
b=[0,0,1]







def buscar_secuencia(secuencia1,secuencia2):

    matriz = [[0 for i in range(len(secuencia2)+1)]  # Se inicializa la matriz llena de 0s
              for j in range(len(secuencia1)+1)]


    for i in range(1,len(matriz)): #Rellenamos la matriz para buscar coincidencias
        for j in range(1,len(matriz[i])):
            if(secuencia1[i-1] == secuencia2[j-1]): #Si coinciden, tomamos el anterior diagonalmente y le sumamos 1
                matriz[i][j] = matriz[i-1][j-1]+1
            elif(matriz[i-1][j]>=matriz[i-1][j-1]+1):#Si no, ahora compara con los anteriores vertical y horizontalmente
                matriz[i][j] = matriz[i-1][j]
            else:
                matriz[i][j] = matriz[i][j-1]
    print("Matriz de las secuencias ",secuencia1," y ",secuencia2, ":")
    mostrar(matriz)
    print("")


    print("Longitud maxima: ",matriz[i][j]) #En la ultima posicion se guarda la mayor longitud


    i = len(secuencia1) #Se inicializan en la ultima posicion
    j = len(secuencia2)


    subsecuencia_comun = []

    while(len(subsecuencia_comun)<matriz[len(secuencia1)][len(secuencia2)]):

        if(matriz[i][j]>matriz[i-1][j-1]):
            #Se obtiene la posicion de la secuencia de longitud menor
            if(i > j): #Si es menor la segunda, se coge la posicion de j (columnas)
                subsecuencia_comun.append(secuencia2[j-1])  #Se introduce de final a principio por lo que luego hay que darle la vuelta
            else: #Si no, se coge la de i(filas)
                subsecuencia_comun.append(secuencia1[i-1])

        i -= 1
        j -= 1

    subsecuencia_comun.reverse()#Se da la vuelta ya que se introducen al reves

    return subsecuencia_comun



def mostrar(matriz):
    for i in matriz:
        print(i)


print(buscar_secuencia(A,B))
print("")
print(buscar_secuencia(a,b))





