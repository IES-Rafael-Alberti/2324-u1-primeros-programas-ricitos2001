def crear_minusculas(letrasminusculas):
    return "nombre en minusculas: "+letrasminusculas
def crear_mayusculas(letrasmayusculas):
    return "nombre en mayusculas: "+letrasmayusculas
def crear_capitalizado(letrascapitalizadas):
    return "nombre capitalizado: "+letrascapitalizadas
if __name__ == "__main__":
    nombrecompleto = input("escriba su nombre completo: ")
    letrasminusculas=nombrecompleto.lower()
    letrasmayusculas=nombrecompleto.upper()
    letraspalabras=nombrecompleto.split()
    letrascapitalizadas =' '.join([palabra.capitalize() for palabra in letraspalabras])
    nombreminusculas= "nombre en minusculas: ", letrasminusculas
    nombremayusculas= "nombre en mayusculas: ", letrasmayusculas
    nombrecapitalizado= "nombre capitalizado: ", letrascapitalizadas
    nombreminusculas=crear_minusculas(letrasminusculas)
    nombremayusculas=crear_mayusculas(letrasmayusculas)
    nombrecapitalizado=crear_capitalizado(letrascapitalizadas)
    print(nombreminusculas)
    print(nombremayusculas)
    print(nombrecapitalizado)