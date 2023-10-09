def crear_total (total):
    return "total: "+ str(total)
if __name__=="__main__":
    ancho = int(input("ancho: "))
    alto = int(input("alto: "))
    cocienteancho = ancho / 2
    cocienteancho2 = ancho // 2
    cocientealto= alto / 3
    total = cocienteancho + cocienteancho2 + cocientealto
    sumatotal = "total: ", total
    sumatotal = crear_total (total)
    print (sumatotal)