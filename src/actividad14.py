def crear_payasos (pesototalpayasos):
    return "el peso total del ultimo paquete de payasos es de "+ str(pesototalpayasos)+ "g"
def crear_muñecas (pesototalmuñecas):
    return "el peso total del ultimo paquete de muñecas es de "+ str(pesototalmuñecas)+ "g"
if __name__=="__main__":
    numeropayasos=int(input("numero de payasos vendidos: "))
    numeromuñecas=int(input("numero de muñecas vendidas: "))
    pesopayasos=int(112)
    pesomuñecas=int(75)
    pesototalpayasos=numeropayasos*pesopayasos
    pesototalmuñecas=numeromuñecas*pesomuñecas
    totalpayasos= "el peso total del ultimo paquete de payasos es de "+str(pesototalpayasos)+"g"
    totalmuñecas= "el peso total del ultimo paquete de muñecas es de "+str(pesototalmuñecas)+"g"
    print (totalpayasos)
    print (totalmuñecas)
    totalpayasos = crear_payasos (pesototalpayasos)
    totalmuñecas = crear_muñecas (pesototalmuñecas)
