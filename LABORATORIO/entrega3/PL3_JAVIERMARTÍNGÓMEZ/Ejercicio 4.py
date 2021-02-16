botellas=[2,3,7,1,3]
corchos=[7,1,2,5,3]

""" Dadas un lista de corchos y botellas,
ordena los corchos de menor a mayor usando como pivotes las botellas"""
def ordenar_corchos(corchos, botellas, indice_pivote):

    if(indice_pivote >= len(botellas)): #Si ya se ha pivotado todo, se retornan los corchos ordenados
        return corchos
    else:
        pivote = botellas[indice_pivote] #pivote en las botellas
        indice_pivote_en_corchos = corchos.index(pivote) #obtenemos la posicion en corchos del pivote de botellas
        indice_recorrido = 0 #vemos que elemento esta pivotando en corchos
        while(indice_recorrido < len(corchos)):
            if(corchos[indice_recorrido] > pivote and indice_recorrido < indice_pivote_en_corchos): #si el elemento es mayor y estoy a la izquierda:
                valor = corchos[indice_recorrido]
                seccion_izquierda = corchos[0:indice_pivote_en_corchos+1] #sacamos la parte izquierda
                seccion_izquierda.remove(valor) #eliminamos el elemento mayor a la izquierda del pivote
                seccion_derecha = corchos[indice_pivote_en_corchos+1:] #sacamos la parte derecha
                corchos = seccion_izquierda + [valor] + seccion_derecha #coloco el elemento mayor a la derecha del pivote
                indice_pivote_en_corchos = corchos.index(pivote) #actualizo el indice del pivote en caso de que haya cambiado de sitio:
                
            elif(corchos[indice_recorrido] < pivote and indice_recorrido >= indice_pivote_en_corchos): #si el elemento es menor y estoy a la derecha:
                valor = corchos[indice_recorrido] #valor a reordenar:
                seccion_izquierda = corchos[0:indice_pivote_en_corchos] #saco la parte de la izquierda
                seccion_derecha = corchos[indice_pivote_en_corchos:] #saco la parte derecha
                seccion_derecha.remove(valor) #elimino el elemento menor a la derecha del pivote
                corchos = seccion_izquierda + [valor] + seccion_derecha #coloco el elemento mayor a la izquierda del pivote
                indice_pivote_en_corchos = corchos.index(pivote) #actualizo el indice del pivote en caso de que haya cambiado de sitio:
                
            else: #si el elemento está correctamente ordenado, a la izquierda del pivote si es menor o a la derecha si es mayor
                indice_recorrido += 1 #se avanza al siguiente elemento:
                indice_pivote_en_corchos = corchos.index(pivote)
        return ordenar_corchos(corchos, botellas, indice_pivote+1)


print(ordenar_corchos(corchos,botellas,0))
