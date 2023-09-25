from random import*

def generarNumeroAleatorio(minimo,maximo)
    if minimo>maximo:
        aux=minimo
        minimo=maximo
        maximo=aux

    return randint(minimo,maximo)

i=0
while i<5:
    print (generarNumeroAleatorio(1,10))
    i=i+1
