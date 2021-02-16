

def unirEscaleras(escaleras, costes):

    if (len(escaleras) == 0):
        costeUnion = 0
        for i in costes:
            costeUnion += i
        print("El coste minimo de soldar las escaleras es: " + str(costeUnion))
    else:

        primer_minimo= min(escaleras) #obtenemos la escalera de longitud minima
        escaleras.remove(primer_minimo) #eliminamos la escalera, ya que la vamos a usar

        segundo_minimo = min(escaleras)  #obtenemos la siguiente escalera de longitud minima
        escaleras.remove(segundo_minimo) #volvemos a eliminar la escalera

        union = primer_minimo + segundo_minimo #se suma el coste de las dos escaleres unidas
        costes.append(union)

        if(len(escaleras) != 0): #si no es vacia, se introduce la union como ora escalera nueva
            escaleras.append(union)

        unirEscaleras(escaleras, costes) #llamada recursiva

escaleras1=[6,8,7,5]
unirEscaleras(escaleras1,[])

escaleras2=[8,9,20,5,3]
unirEscaleras(escaleras2,[])

    













































    








