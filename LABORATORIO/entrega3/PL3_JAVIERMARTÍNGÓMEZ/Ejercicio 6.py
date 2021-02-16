
# funcion para comprobar la altura
def f(x):
    return x**2

def buscar_min(inicio, fin):
    long_puente = fin - inicio #Longitud puente

    if (long_puente < 3): #Si la longitud del puente es menor que 3, ya que tomamos 3 como el valor maximo
        valor_min = inicio #Valor minimo que puede retornar la funcion
        for i in range(inicio, fin + 1):
            if(f(i) < f(valor_min)):
                valor_min = i
        return valor_min

    else:
        tercio_long = long_puente // 3  # Longitud de cada tercio, ya que dividimos al puente en tres partes
        valor_final = f(inicio + tercio_long)  # Ultimo valor del primer tercio
        valor_inicial = f(inicio + 2 * tercio_long)  # Primer valor del ultimo tercio

        if (valor_final <= valor_inicial):  # Me quedo con los dos primeros tercios, si son los mas profundos
            return buscar_min(inicio, fin - tercio_long)

        elif (valor_final > valor_inicial):  # Me quedo con los dos ultimos, si son los mas profundos
            return buscar_min(inicio + tercio_long, fin)

print(buscar_min(0, 5))


