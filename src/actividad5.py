def crear_precio (importe):
    return "precio total: "+str(importe)+"€"
if __name__=="__main__":
    nombre=(input("nombre del articulo: "))
    precio=int(input("precio del producto: "))
    iva=float(input("iva del producto: "))
    importe=precio*iva
    preciototal = "importe total: ", str(importe),"€"
    preciototal = crear_precio (importe)
    print (preciototal)