# Pseudocodigo reservas
## Analisis de variables
Genero: El usuario selecciona M(masculino) o F(femenino).(Entrada)

Sr@: Escribe Sr o Sra(Salida)

Nombre: Nombre completo de usuario(Entrada)

Origen: Ciudad de origen del pasajero.(Entrada)

Destino: Ciudad destino del pasajero.(Entrada)

Fecha_dia: Dia de la semana en que viaja el pasajero.(Entrada)

Fecha_Num: Fecha en numeros del vuelo.(Entrada)

Distancia: Calculo de distancia entre ciudades.(Salida)

Precio: Precio segun dia y distancia del vuelo.(Salida)

Asiento: Asiento deseado por pasajero.(Entrada)

Fila: Numero aleatorio de 1 a 29(Salida)


` ` `
Inicio

    Leer Genero("Ingrese su genero: ")
    Definir Sr@: 0
    Si Genero = M:
        Sr@ = ("Sr")
    Sino
        Sr@ = ("Sra")
    Leer Nombre("Ingrese su nombre completo: ")
    Escribir((Sr@)(Nombre)Bienvenido a fast fast airlines.)
    Leer Origen("Ingrese la ciudad de origen: ")
    Leer Destino("Ingrese la ciudad destino: ")
    Definir distancia = 0
    Definir Precio = 0
    Si Origen = Medellin y Destino = Bogotá:
        Definir distancia = 240
    Si Origen = Medellin y Destino = Cartagena: 
        Definir distancia = 461
    Si Origen = Bogotá y Destino = Cartagena:
        Definir distancia = 657
    Si Origen = Bogotá y Destino = Medellin:
        Definir distancia = 240
    Si Origen = Cartagena y Destino = Medellin: 
        Definir distancia = 461
    Si Origen = Cartagena y Destino = Bogotá:
        Definir distancia = 657
    Leer Fecha_Dia("Que dia de la semana es su vuelo: ")
    Leer Fecha_Num("En que fecha es su vuelo: ")
    Si Fecha_Dia = [Lunes, Martes, Miercoles, Jueves] y distancia < 400
        Precio = 79900
        Si Fecha_Dia = [Lunes, Martes, Miercoles, Jueves] y distancia > 400
        Precio = 156900
        Si Fecha_Dia = [Viernes, Sabado, Domingo] y distancia < 400
        Precio = 119900
        Si Fecha_Dia = [Viernes, Sabado, Domingo] y distancia > 400       
        Precio = 213000
    Leer Asiento("Escriba que asiento desea(A:Ventanilla, C:Pasillo, B:Sin preferencia): ")
    Definir Fila = Numero aleatorio(1,29)
    Escribir("(Sr@) (Nombre) su vuelo tendrá un costo de $(Precio) el dia (Fecha_Dia) (Fecha_Num) en la silla (Fila)(Asiento))
    
Fin
` ` `