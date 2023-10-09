#definicion del programa
def crear_funcion(funcion3):
    return "la funcion es: "+funcion3
if __name__=="__main__":
    #valores de la funcion
    nombre=(input("introduce tu nombre: "))
    funcion1=(input("nombre de la primera funcion: "))
    funcion2=(input("nombre de la segunda funcion: "))
    #funcion del programa
    funcion3=funcion1+" "+funcion2
    funcion="la funcion es: ", funcion3
    funcion= crear_funcion (funcion3)
    #resultado de la funcion
    print (funcion)