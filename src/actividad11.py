def crear_calculo(calculo):
    return "el resultado es: "+str(calculo)
if __name__=="__main__":
    numero=int(input("introduce un numero: "))
    calculo=(numero*(numero+1))/2
    resultado="el resultado es: ", str(calculo)
    resultado= crear_calculo (calculo)
    print (resultado)