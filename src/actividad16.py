def crear_precio(precio):
    return "precio del pan: "+str(precio)+"€"
def crear_descuento(descuento):
    return "descuento de las barras tiesas: "+str(descuento)+"€"
def crear_costetotal(costetotal):
    return "coste total de las barras tiesas: "+str(costetotal)+"€"

if __name__ == "__main__":
    pantieso=int(input("numero de barras tiesas de pan: "))
    precio=float(3.49)
    descuento=float(0.6)
    calculo=round(precio*descuento, 2)
    costetotal=(precio-calculo)*pantieso
    preciopan="precio del pan :", str(precio), "€"
    descuentopan="descuento de las barras tiesas: ", str(descuento), "€"
    costepan="coste total de las barras tiesas: ", str(costetotal), "€"
    preciopan=crear_precio(precio)
    descuentopan=crear_descuento(descuento)
    costepan=crear_costetotal(costetotal)
    print(preciopan)
    print(descuentopan)
    print(costepan)