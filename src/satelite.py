import time
def main():
    Altitud = float(input("Ingrese la altitud del satelite en km: "))
    Altitud_Minima = float(input("Ingrese la altitud minima de seguridad en km: "))
    Cd = float(input("Ingrese el coeficiente de arrastre del satelite: "))
    Altitud_Perdida = 0 
    Orbitas = 0
    stability = False
    if Altitud < Altitud_Minima:
        print("El satelite se encuentra por debajo de la altitud minima")
        stability = True
    else:
        while Altitud > Altitud_Minima and stability == False:
            Altitud_Perdida = Altitud*Cd
            Altitud = Altitud - Altitud_Perdida
            Orbitas = Orbitas + 1
            if Cd < -0.001 and Orbitas > 3:
                print("Satelite estable")
                stability = True
            elif Cd > 0: 
                Cd = Cd + 0.0001
            elif Cd < 0: 
                Cd = Cd - 0.0001
            print(f'En la orbita #{Orbitas} la altitud del satelite es: {Altitud}km')
            time.sleep(0.25)
        
        if Altitud < Altitud_Minima:
            print(f"Se ha perdido conexión con satelite despues de {Orbitas} orbitas")
    pass


if __name__ == "__main__":
    main()
