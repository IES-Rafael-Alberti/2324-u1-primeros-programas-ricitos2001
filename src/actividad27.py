def crear_mensaje (nombre,precio,unidad,preciounidad):
    return nombre+", "+str(precio)+"€"+", "+str(unidad)+", "+str(preciounidad)+"€"
if __name__=="__main__":
    nombre=(input("nombre del articulo: "))
    precio=int(input("precio del producto: "))
    unidad=int(input("unidad del producto: "))
    preciounidad=precio*unidad
    mensaje = nombre+", ", str(precio), "€", ", ", str(unidad), ", ", str(preciounidad), "€"
    mensaje = crear_mensaje (nombre,precio,unidad,preciounidad)
    print (mensaje)