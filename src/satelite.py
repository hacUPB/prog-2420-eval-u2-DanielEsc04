import time
def main():
    Altitud = float(input("Ingrese la altitud del satelite: "))
    Altitud_Minima = float(input("Ingrese la altitud minima de seguridad: "))
    Cd = float(input("Ingrese el coeficiente de arrastre del satelite: "))
    Altitud_Perdida = 0 
    Orbitas = 0
    if Cd < 0.00001:
        print("Satelite estable")
    while Altitud > Altitud_Minima and Cd > 0:
        Altitud_Perdida = Altitud*Cd
        Altitud = Altitud - Altitud_Perdida
        Orbitas = Orbitas + 1
        Cd = Cd + 0.0001
        print(f'En la orbita #{Orbitas} la altitud del satelite es: {Altitud}')
        time.sleep(0.25)
        
    if Altitud < Altitud_Minima:
        print(f"Se ha perdido conexión con satelite despues de {Orbitas} orbitas")
    pass


if __name__ == "__main__":
    main()
