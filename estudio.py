#Manual Asignatura Introducciíon a la programación

#Ejercicios Propuestos. 
#Ejercicio 1.

#gurpo cada estudiante correspondiente a una lista, con los datos en el siguiente orden, [nombre, edad, sexo, promedio notas,]

estudiante1 = ["pablo",26, "H", 6.5]
estudiante2 = ["camila",18, "M", 6.8]
estudiante3 = ["Juan",23, "H", 5.8]
estudiante4 = ["camilo",18, "H", 6.0]
estudiante5 = ["fernando",17, "H", 6.0]

#creamos listas para almacenar los datos con los cuales se realizarán operaciones
listaEdades = []
listaSexo = []
listaPromedio = []

#creamos una función para llenar nuestra lista de edades.
def LLenarListas(lista):
    a = lista[1]
    b = lista[2]
    c = lista[3]
    listaEdades.append(a)
    listaSexo.append(b)
    listaPromedio.append(c)
#aplicamos la función a los datos de cada estudiante.
LLenarListas(estudiante1)
LLenarListas(estudiante2)
LLenarListas(estudiante3)
LLenarListas(estudiante4)
LLenarListas(estudiante5)

#inicializamos las variables
contadorEdades = 0
sumadorEdades = 0
mayores18 = 0
menores18 = 0
contadorH = 0
contadorM = 0
contadorPromedio = 0

#usamos un bucle for para calcular el promedio de las edades.
for elemento in listaEdades:
    sumadorEdades = sumadorEdades + elemento
    contadorEdades = contadorEdades + 1
    if elemento >= 18:
        mayores18 = mayores18 + 1
    else:
        menores18 = menores18 + 1
promedio = sumadorEdades/contadorEdades

#con un bucle for y una sentencia if, mas la ayuda de contadores, podemos determinar la cantidad de hombres y mujeres en el grupo.

for elemento in listaSexo:
    if elemento == "H":
        contadorH = contadorH + 1
    else:
        contadorM = contadorM + 1
#con un bucle for y una sentencia if, compararemos los datos de la lista de promedios para comparar cuales salieron con nota menor o igual a 5.0.
for elemento in listaPromedio:
    if elemento <= 5.0:
        contadorPromedio = contadorPromedio + 1


#Mostrar las respuestas por consola
print("Ejercicio 1 a): El promedio de las edades de los alumnos del grupo es:",promedio)
print("Ejercicio 1 b): Los alumnos mayores de 18 son",mayores18,",los menores de 18 son",menores18)
print("Ejercicio 1 c): La cantidad de hombres es",contadorH, "y la cantidad de mujeres es", contadorM)
print("Ejercicio 1 d): La cantidad de alumnos que obtuvieron un promedio menor a 5.0 son",contadorPromedio)

#fin Ejercicio 1.

##Actividad 2.2.2 Principios de Almacenamiento

#ejercicio 1
#Ingresamos la información de la memoria en un diccionario:

memoria = {"X":3,"R":12,"Y":4,"S":9,"L":100,"P":8,"T":100,"G":6,"A":20,"J":5,"W":80,"Z":5}

#realizamos las operaciones para obetener los valores finales:

memoria["X"] = memoria["G"] + 5
memoria["W"] = memoria["A"] * memoria["X"]
memoria["T"] = memoria["S"] + memoria["P"] - memoria["J"]
memoria["J"] = memoria["T"] + memoria["L"]
memoria["Z"] = memoria["P"] * memoria["R"] + memoria["Y"]
memoria["Y"] = memoria["Y"] + memoria["Z"]
memoria["Y"] = memoria["Y"] + 1

print("los valores finales de memoria son para el ejercicio 2.2.2 - 1:",memoria)

#Ejercicio 2:
memoria2 = {"X":14,"R":8,"Y":0,"S":-9,"L":130,"P":0,"T":16,"G":-56,"A":-4,"J":5,"W":-8,"Z":0}

#realizamos las operaciones para los valores finales:

memoria2["X"] = memoria2["X"] + memoria2["A"] - memoria2["W"]
memoria2["S"] = memoria2["X"] - memoria2["J"] * memoria2["Z"]
memoria2["R"] = memoria2["R"] + 1
memoria2["Y"] = memoria2["R"] - memoria2["X"] + 2
memoria2["L"] = memoria2["Y"] + memoria2["L"]
memoria2["T"] = memoria2["G"] + memoria2["J"] - memoria2["Z"] * 3
memoria2["W"] = memoria2["W"] + 5
memoria2["J"] = memoria2["J"] + memoria2["Z"] / memoria2["X"] + 2

print ("los valores finales de la memoria para el ejercicio 2.2.2 - 2 son:",memoria2)











    



