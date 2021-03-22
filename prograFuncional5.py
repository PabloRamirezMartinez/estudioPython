#escribir un programa que reciba uuna frase y devuelva un diccionario con las palabras que contiene y su ongitud.
palabra = input("ingrese una frase: ")

def funcion1(palabra):
    dicc = {}
    a = palabra.split()
    for elemento in a:
        b = len(elemento)
        dicc[elemento] = b
    return(dicc)

print(funcion1(palabra))



