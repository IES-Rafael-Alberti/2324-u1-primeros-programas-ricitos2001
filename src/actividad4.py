def crear_farenheit (farenheit):
    return "grados farenheit: "+str(farenheit)+"Fº"
if __name__=="__main__":
    celsius=int(input("grados celsius: "))
    farenheit=celsius*9/5+32
    importetotal = "importe total: ", str(farenheit),"Fº"
    importetotal = crear_farenheit (farenheit)
    print (importetotal)