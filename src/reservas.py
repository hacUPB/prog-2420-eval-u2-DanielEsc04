import random
from random import randint
def main():
    Distancia = 0 
    Precio = 0 
    Nombre = input("Ingrese su nombre completo: ")
    Genero = input ("Ingrese su genero (M) o (F)")
    if Genero not in ["M", "F"]:
        print("Genero no valido")
    elif Genero == ("M"):
        Genero = ("Sr")
        print(f"{Genero} {Nombre} bienvenido a fast airlines.")
    elif Genero == ("F"):
        Genero = ("Sra")
        print(f"{Genero} {Nombre} bienvenida a fast airlines.")
    Origen = int(input("Ingrese la ciudad origen:\nMedellín(1)\nBogotá(2)\nCartagena(3)"))
    if Origen not in range (1,3):
        print ("Seleccione una ciudad correcta")
    Destino = int(input("Ingrese la ciudad destino:\nMedellín(1)\nBogotá(2)\nCartagena(3)"))
    if Destino not in range (1,3):
        print ("Seleccione una ciudad correcta")
    elif Origen == 1 and Destino == 2:
        Distancia == 240
    elif Origen == 2 and Destino == 1:
        Distancia == 240
    elif Origen == 1 and Destino == 3:
        Distancia == 461
    elif Origen == 3 and Destino == 1:
        Distancia == 461
    elif Origen == 2 and Destino == 3:
        Distancia == 657
    elif Origen == 3 and Destino == 2:
        Distancia == 657
    else:
        print("Viaje no disponible")

    Fecha_Dia = int(input("Ingrese el dia de la semana que viajará: \nLunes(1)\nMartes(2)\nMiercoles(3)\nJueves(4)\nViernes(5)\nSabado o Domingo(6)"))
    Fecha_Num = int(input("Ingrese la fecha del mes que viajará"))
    Fecha_Mes = input("En que mes viajará?")
    if Fecha_Dia <= 4 and Distancia < 400:
        Precio = 79900
    elif Fecha_Dia <= 4 and Distancia > 400:
        Precio = 156900
    elif Fecha_Dia > 4 and Distancia < 400:
        Precio = 119900
    elif Fecha_Dia > 4 and Distancia > 400:
        Precio = 213000
    Asiento = input("Ingrese el asiento que desee: \nA: Ventanilla\nB: Sin preferencia\nC: Pasillo")
    Fila = randint(1,29)
    print(f"{Genero} {Nombre} su vuelo será el {Fecha_Num} de {Fecha_Mes} su silla será {Fila}{Asiento}, tendrá un valor de ${Precio}")

    pass


if __name__ == "__main__":
    main()
