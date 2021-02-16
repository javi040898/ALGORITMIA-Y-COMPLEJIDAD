
escaleras1=[3,2,5,1,4,6,7,2,4,5]
escaleras2=[6,8,7]

def unirEscaleras(escaleras):
    escaleras.sort() #se ordena para obtener el tiempo minimo
    tiempo_acumulado=0
    escalera1=escaleras[0]
    escalera2=escaleras[1]
    escaleras.pop(0)#borramos las dos escaleras para saber el tiempo de las dos primeras
    escaleras.pop(0)
    tiempo_acumulado = escalera1 + escalera2
    for i in escaleras: #recorremos el resto de la escalera y le vamos sumando al tiempo el primer valor de la lista
        tiempo_union=tiempo_acumulado+i
        tiempo_acumulado=tiempo_acumulado+tiempo_union
    return tiempo_acumulado

print(unirEscaleras(escaleras1))
    
    













































    








