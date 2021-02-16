
#Funcion auxiliar para buscar en la matriz
def buscar_elemento(letra):
    if(letra == 'a'):
        return 0
    elif (letra == 'b'):
        return 1
    elif(letra == 'c'):
        return 2
    elif(letra == 'd'):
        return 3

#Funcion que va sustituyendo hasta que quede 1 y lo comprueba
def sustituir(cadena,matriz,caracter):
    print(cadena)
    if(len(cadena) == 1 and cadena == [caracter]): #Si la cadena tiene un valor y es el caracter pedido, retorna True
        return True
    else:
        for i in range(0,len(cadena)-1): #Si no, recorremos la cadena posicion por posicion, sustituyendo hasta que quede 1 y lo comprobamos

            letra1 = buscar_elemento(cadena[i]) #Primera posicion
            letra2 = buscar_elemento(cadena[i+1]) #Segunda posicion
            cadena_nueva = cadena[:i] + [matriz[letra1][letra2]] + cadena[(i + 2):len(cadena)] #La cadena nueva seran los caracteres hasta el primer comprobado conc el sustituido conc el resto

            if (sustituir(cadena_nueva,matriz,caracter)): #Llamamos recursivamente a la funcion para ver si con la nueva cadena llegamos a la solucion
                return True
    return False




matriz_sustitucion = [['b','b','a','d'],
                      ['c','a','d','a'],
                      ['b','a','c','c'],
                      ['d','c','d','b']]

cadena_ini = ['a','c','a','b','a','d','a']


if(sustituir(cadena_ini,matriz_sustitucion,'b')):
    print("Solucion encontrada")
else:
    print("Solucion no encontrada")









