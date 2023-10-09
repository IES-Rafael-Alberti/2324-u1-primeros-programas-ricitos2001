def crear_lista(resultadolista):
    return resultadolista

if __name__ == "__main__":
    listacompra = input("Escriba los productos de una cesta de la compra, separados por comas: ")
    productos = listacompra.split(",")
    resultadolista = ""
    for producto in productos:
        resultadolista += producto.strip() + "\n"
    lista=resultadolista
    lista=crear_lista(resultadolista)
    print(lista)




