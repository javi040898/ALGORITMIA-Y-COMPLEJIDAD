n=[4,5,2,8,9,3,1,6,7]

def min_max(lista):
    for i in range (int(len(lista)/2)):#Cambiamos cada valor por su simetrico si el de la mitad izquierda                                
        izquierdo=lista[i]              #es mayor para dejar los menores a la izquierda
        derecho=lista[len(lista)-i-1]   #y los mayores a la derecha
        if(izquierdo>derecho):
           lista[i]=derecho
           lista[len(lista)-i-1]=izquierdo
           
    minimo=lista[0]      #minimo de la primera mitad
    for i in range (int(len(lista)/2)+1):#sumamos 1 por si la longitud es impar
        if(lista[i]<minimo):
            minimo=lista[i]
    
    maximo=lista[0]     #maximo de la segunda mitad
    for i in range((int(len(lista)/2)),len(lista)):
        if(lista[i]>maximo):
            maximo=lista[i]
    retorno="Lista dividida: " + str(lista) +" Maximo: " +str(maximo)+" Minimo: "+str(minimo)
    return retorno

print(min_max(n))
