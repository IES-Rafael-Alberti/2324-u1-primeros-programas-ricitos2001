def crear_fecha(fechanacimiento):
    return "fecha de nacimiento: "+str(fechanacimiento)

if __name__ == "__main__":
    introducirfecha = input("introduce su fecha de nacimiento (DD/MM/AAAA): ")
    dianacimiento=introducirfecha.zfill(2).split("/")
    mesnacimiento=introducirfecha.zfill(2).split("/")
    añonacimiento=introducirfecha.zfill(4).split("/")
    fechanacimiento=dianacimiento+mesnacimiento+añonacimiento
    fecha="fecha de nacimiento: ", str(dianacimiento), str(mesnacimiento), str(añonacimiento)
    fecha=crear_fecha(fechanacimiento)
    print(fecha)
