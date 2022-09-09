class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)


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
