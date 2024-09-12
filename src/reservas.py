from random import randint
import datetime
def main():
    Distancia = 0 
    Precio = 0 
    Verficar_Genero = True
    Nombre = input("Ingrese su nombre completo: ")
    while Verficar_Genero == True:
        Genero = (input ("Ingrese su genero (M) o (F)")).upper()
        if Genero not in ["M", "F"]:
            print("Genero no valido")
        elif Genero == ("M"):
            Genero = ("Sr")
            print(f"{Genero} {Nombre} bienvenido a fast airlines.")
            Verficar_Genero = False
        elif Genero == ("F"):
            Genero = ("Sra")
            print(f"{Genero} {Nombre} bienvenida a fast airlines.")
            Verficar_Genero = False 
    Verficar_origen = True
    while Verficar_origen == True:
        Origen = input("Ingrese la ciudad origen:\nMedellín(1)\nBogotá(2)\nCartagena(3)")
        if Origen not in ["1", "2", "3"]:
            print ("Seleccione una ciudad correcta")
        else:
            Origen = int(Origen)
            Verficar_origen = False
    Verficar_destino = True
    while Verficar_destino == True:
        Destino = input("Ingrese la ciudad destino:\nMedellín(1)\nBogotá(2)\nCartagena(3)")
        if Destino not in ["1", "2", "3"]:
            print ("Seleccione una ciudad correcta")
        else:
            Destino = int(Destino)
            Verficar_destino = False

        if Origen == 1 and Destino == 2:
            Distancia = 240
        elif Origen == 2 and Destino == 1:
            Distancia = 240
        elif Origen == 1 and Destino == 3:
            Distancia = 461
        elif Origen == 3 and Destino == 1:
            Distancia = 461
        elif Origen == 2 and Destino == 3:
            Distancia = 657
        elif Origen == 3 and Destino == 2:
            Distancia = 657
        else:
            print("Viaje no disponible")
            Verficar_origen = True
            Verficar_destino = True
            
    Verificar_fecha = True
    print("Fecha del vuelo")
    while Verificar_fecha == True:
        Dia = int(input("Ingrese el dia que viajará"))            
        Fecha_Mes = int(input("En que mes viajará?"))
        Año = int(input("Año en que viajará"))
        date = datetime.date(Año, Fecha_Mes, Dia)
        Fecha_Dia = date.isoweekday()
        Fecha_actual = datetime.now().date()
        if date <= Fecha_actual:
            "No se puede ingresar una fecha pasada"
        else:
            Verificar_fecha = False

    if Fecha_Dia <= 3 and Distancia < 400:
        Precio = 79900
        Verificar_fecha = False
    elif Fecha_Dia <= 3 and Distancia > 400:
        Precio = 156900
        Verificar_fecha = False
    elif Fecha_Dia > 3 and Distancia < 400:
        Precio = 119900
        Verificar_fecha = False
    elif Fecha_Dia > 3 and Distancia > 400:
        Precio = 213000
        Verificar_fecha = False
    else:
        print("Ingrese una fecha adecuada.")
    Verificar_silla = True
    while Verificar_silla == True:
        Asiento = input("Ingrese el asiento que desee: \nA: Ventanilla \nB: Sin preferencia \nC: Pasillo ").upper()
        if Asiento not in ["A", "B", "C"]:
            print("Ingrese un asiento adecuado.")
        else:
            Fila = randint(1,29)
            Verificar_silla = False
    print(f"{Genero} {Nombre} su vuelo será el {date}, su silla será {Fila}{Asiento}, tendrá un valor de ${Precio}")

    pass


if __name__ == "__main__":
    main()
