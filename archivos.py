n = int(input("ingrese un número entre 1 y 10: "))
#una función para crear la tabla
def tabla(numero):
    for i in range (1,11):
        r = "tabla-" + str(numero) + ".txt"
        archivo = open(r,"a")
        n = numero * i
        archivo.write(str(numero) + "x" + str(i) + "=" + str(numero*i) + "\n")
        archivo.close()


import os.path
def leer(numero):
    r = "tabla-" + str(numero) + ".txt"
    if os.path.isfile(r):
        archivo = open(r,"r")
        data = archivo.read()
        print(data)
    else:
        print("el archivo no existe")

if (n >= 1 and n <= 10):
    tabla(n)
    leer(n)
else:
    n = int(input("ingrese un número entre 1 y 10: "))
   

        
 

