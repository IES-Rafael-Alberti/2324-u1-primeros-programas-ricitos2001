def crear_mayusculas (letrasmayusculas):
    return "nombre en mayusculas: "+letrasmayusculas
def crear_total (numeroletras):
    return "numero de letras: "+str(numeroletras)
if __name__=="__main__":
    nombre=input("introduce tu nombre: ")
    letrasmayusculas=nombre.upper()
    numeroletras= len(letrasmayusculas)
    nombremayusculas="nombre en mayusculas: ",letrasmayusculas
    totalletras="numero de letras: "+str(numeroletras)
    nombremayusculas= crear_mayusculas(letrasmayusculas)
    totalletras= crear_total(totalletras)
    print(nombremayusculas)
    print(totalletras)