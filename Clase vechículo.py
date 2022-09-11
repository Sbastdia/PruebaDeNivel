from automoviles.coche import Coche
from automoviles.bicicleta import Bicicleta
from automoviles.motocicleta import Motocicleta
from automoviles.camioneta import Camioneta

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

    def catalogar(lista, rueda):
        cantidad=0
        list= []
        for i in lista:
            if rueda== i.ruedas:
                list.append(i)
                cantidad+=1
        print ("Se han encontrado {} vehiculos con {} ruedas:".format(cantidad,rueda))

        for i in list:
            print(type(i).__name__, i)

    catalogar(vehiculos, 0)
