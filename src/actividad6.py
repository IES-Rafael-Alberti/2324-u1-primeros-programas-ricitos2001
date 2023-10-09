def crear_precio (importe):
    return "precio total: "+str(importe)+"€"
if __name__=="__main__":
    nombre=(input("nombre del articulo: "))
    precio=int(input("precio del producto: "))
    iva = float(0.10)
    importe=precio*iva
    preciototal = "precio total: ", str(importe),"€"
    preciototal = crear_precio (importe)
    print (preciototal)