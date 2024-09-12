import time
def main():
    Altitud = float(input("Ingrese la altitud del satelite en km: "))
    Altitud_Minima = float(input("Ingrese la altitud minima de seguridad en km: "))
    Cd = float(input("Ingrese el coeficiente de arrastre del satelite: "))
    Altitud_Perdida = 0 
    Orbitas = 0
    accent = True
    stability = False
    if Altitud < Altitud_Minima:
        print("El satelite se encuentra por debajo de la altitud minima")
    else:
        while Altitud > Altitud_Minima and stability == False:
            Altitud_Perdida = Altitud*Cd
            Altitud = Altitud - Altitud_Perdida
            Orbitas = Orbitas + 1
            if Cd <= 0 and Orbitas == 3:
                print("Satelite estable")
                stability = True
            elif Cd > 0: 
                Cd = Cd + 0.0001
            elif Cd < 0: 
                Cd = Cd - 0.0000001
            print(f'En la orbita #{Orbitas} la altitud del satelite es: {Altitud}km')
            time.sleep(0.25)
        
        while stability == True: 
            if Orbitas % 2 == 0:
                print("Stability burn")
                Cd = Cd - 0.1
                print(f'En la orbita #{Orbitas} la altitud del satelite es: {Altitud}km')
                time.sleep(0.5)
            else:
                print("Coasting")
                print(f'En la orbita #{Orbitas} la altitud del satelite es: {Altitud}km')
                time.sleep(0.5)

        if Altitud < Altitud_Minima:
            print(f"Se ha perdido conexión con satelite despues de {Orbitas} orbitas")
        elif Orbitas == 50 and stability == True:
            print("Satelite estable")
    pass


if __name__ == "__main__":
    main()
