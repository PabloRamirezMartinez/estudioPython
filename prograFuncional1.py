precios_y_dsctos = {1000:20,500:10,100:1}

def funcion1(diccionario):
    lista = []
    for i in diccionario:
       precio_con_dscto = int(i) - (int(i) * int(diccionario[i])/100)
       lista.append(precio_con_dscto)
    return(lista)


def funcion2(numero):
    valor = numero + (numero * 0.19)
    return valor

def funcion3(diccionario,funcion1,funcion2):
    sumador1 = 0
    a = funcion1(diccionario)
    for element in a:
        sumador1 = sumador1 + int(element)
    total = funcion2(sumador1)
        

        
    return(print("el precio de la compra tras aplicar los descuentos es:", sumador1,"\n","el precio de la compra tras aplicar el IVA es:",total))
        
funcion3(precios_y_dsctos,funcion1,funcion2)
