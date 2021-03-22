lista1 = [1,2,3,4,5]

def funcion1(elemento):
    elemento = elemento + 1
    return (elemento)

def funcion2(lista,funcion):
    lista2 = []
    for i in lista:
        lista2.append(funcion(i))
    return(lista2)

print(funcion2(lista1,funcion1))    
    
