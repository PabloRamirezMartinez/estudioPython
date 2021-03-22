


class Coordenada:
    def crearPunto(self):
        punto = input("ingrese las coordenadas del punto acá: ")
        puntoint =punto.split(",")
        x = int(puntoint[0])
        y = int(puntoint[1])
        return(x,y)

    def cuadrante(self):

        c = Coordenada()
        p = c.crearPunto()
        x = p[0]
        y = p[1]
        if x > 0 and y > 0:
            print("pertenece al cuadrante 1")
        if x < 0 and y > 0:
            print("pertenece al cuadrante 2")
        if x < 0 and y < 0:
            print("pertenece al cuadrante 3")
        if x > 0 and y < 0:
            print("pertenece al cuadrante 4")

    def vector(self):
        c = Coordenada()
        p1 = c.crearPunto()
        p2 = c.crearPunto()
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        vx = x2-x1
        vy = y2-y1
        print("(",vx,",",vy,")")
        
    def distancia(self):
        import math
        c = Coordenada()
        p1 = c.crearPunto()
        p2 = c.crearPunto()
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        vx = x2-x1
        vy = y2-y1
        d = math.sqrt((vx*vx) + (vy*vy))

        print("la distancia entre los puntos es: ", d)

class Rectangulo:
    def crearPuntos(self):
        p1 = input("ingrese el punto de inicio del rectángulo en coordenadas: ")
        p2 = input("ingrese el punto final del rectángulo en coordenadas: ")
        a = p1.split(",")
        b = p2.split(",")
        x1 = int(a[0])
        y1 = int(a[1])
        x2 = int(b[0])
        y2 = int(b[1])
        return((x1,y1),(x2,y2))
    
    def base(self):
        a = crearPuntos()
        x1 = a([0][0])
        x2 = a([1][0])
        base = x2-x1
        return(base)

    def altura(self):
        a = crearPuntos()
        y1 = b([0][1])
        y2 = b([1][1])
        base = y2-y1
        return(altura)

    def area(self):
        a = altura
        




r = Rectangulo()
r1 = r.crearPuntos()
print(r1)



            





