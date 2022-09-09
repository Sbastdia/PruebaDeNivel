
if __name__=="__main__":

    coche = Coche("azul", 4, 150, 1200)
    camioneta = Camioneta("blanca", 6, 90, 1500, 2000)
    bicicleta= Bicicleta("roja", 2, "deportiva")
    motocicleta= Motocicleta("negra", 2, "deportiva", 180, 125)

    vehiculos= []
    vehiculos.append(coche)
    vehiculos.append(camioneta)
    vehiculos.append(bicicleta)
    vehiculos.append(motocicleta)

    def catalogar(lista):
        for i in lista:
            print(type(i).__name__, i)
