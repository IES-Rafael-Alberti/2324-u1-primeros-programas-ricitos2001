def crear_mensaje (nombre):
    return "hola "+nombre
if __name__=="__main__":
    nombre=(input("introduce tu nombre: "))
    mensaje = "hola ", nombre
    mensaje = crear_mensaje (nombre)
    print (mensaje)
