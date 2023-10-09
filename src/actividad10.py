def crear_calculo(calculo):
    return "el resultado es: "+str(calculo)
if __name__=="__main__":
    calculo=(3+2)/(2*5)**2
    resultado="el resultado es: ", str(calculo)
    resultado= crear_calculo (calculo)
    print (resultado)