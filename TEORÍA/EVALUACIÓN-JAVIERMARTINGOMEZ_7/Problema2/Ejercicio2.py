

#Para potencia de 2
def media_dyv_pot2(notas,li,ls,f):

    if(li == ls):
        return notas[li]
    else:
        # Se divide en mitades hasta que el valor es unico (if de arriba)
        mitad = int((li + ls)/2)

        mediaIzq = media_dyv_pot2(notas,li,mitad,f) #Media de la parte izquierda desde el limite inferior (0) hasta la mitad
        f.write("Media de mitad izquierda: " + str(mediaIzq) + "\n")
        mediaDcha = media_dyv_pot2(notas,mitad+1,ls,f) #Media de la parte derecha desde la mitad + 1 hasta el limite superior
        f.write("Media de mitad derecha: " + str(mediaDcha) + "\n")

        return (mediaIzq + mediaDcha)/2 #Se hace la media de los dos elementos

#Funcion auxiliar que nos dice si un numero es potencia de dos
def potencia_de_dos(numero):
    if (numero < 1):
        return False
    elif (numero == 1):
        return True
    else:
        return potencia_de_dos(numero/2)


#Funcion que annade ceros hasta que sea potencia de 2
def annadir_elementos(notas,f):
    while(not(potencia_de_dos(len(notas)))): #Annadimos 0 hasta que sea potencia de dos
        notas.append(0)
    f.write("Annadimos ceros a la lista y queda: " + str(notas)+"\n")
    return notas

#Suma elementos con dyv (para cuando no es potencia de dos)
def suma_elementos(notas,li,ls,f):
    if(li == ls):
        return notas[li]
    else:
        #El procedimiento es el mismo que con la media pero haciendo la suma de dos elementos
        mitad = int((li+ls)/2)
        sumaIzq = suma_elementos(notas,li,mitad,f)
        f.write("Suma de mitad izquierda: " + str(sumaIzq)+"\n")
        sumaDcha = suma_elementos(notas,mitad+1,ls,f)
        f.write("Suma de mitad derecha: " + str(sumaDcha)+"\n")

        return sumaIzq + sumaDcha

#Funcion para calcular la media de cualquier lista, se le pasa el txt desde donde se lee y el txt donde escribe
def media_cualquiera(archivo_leido,archivo_escribir):
    notas = leer_archivo(archivo_leido)
    f = open(archivo_escribir, "w")
    f.write("Lista inicial: " + str(notas) + "\n")
    if(potencia_de_dos(len(notas))):
        f.write("La longitud de la lista es potencia de 2 por lo que vamos haciendo la media de cada mitad y de cada mitad de mitad y sucesivamente\n")
        f.write("Media final: " + str(media_dyv_pot2(notas,0,len(notas)-1,f))+"\n")
    else:
        f.write("La longitud de la lista no es potencia de 2 por lo que annadimos ceros hasta que sea potencia de 2. Despues hacemos la suma con dyv de la lista con los ceros"
                " y lo dividimos por la longitud de la lista inicial\n")
        longitud = len(notas)  # Lo usaremos para dividir al final
        notas_pot_2 = annadir_elementos(notas,f)  # Annadimos los ceros
        suma = suma_elementos(notas_pot_2, 0, len(notas_pot_2) - 1,f)
        f.write("Suma total lista: "+str(suma)+ "\n")
        f.write("Dividimos " + str(suma) + " entre " + str(longitud) + "\n")
        f.write("Media final: " + str(suma / longitud) + "\n")
    f.close()

#Funcion para leer archivo y que lo transforme en una lista, ya que solo se pueden leer strings
def leer_archivo(archivo):
    text_file = open(archivo)
    salida = text_file.read().split(',')
    for i in range(len(salida)):
        salida[i] = float(salida[i])
    text_file.close()
    return salida

media_cualquiera('ejemplo_dyv.txt','archivo_salida.txt')















