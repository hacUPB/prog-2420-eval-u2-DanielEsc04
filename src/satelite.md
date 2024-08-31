# Pseudocodigo Satelite
## Analisis Variables
Altitud_Inicial: Altitud en la que se encuentra el satelite.(Entrada)
Altititud: Altitud actual del satelite(Salida)
Altitud_Minima: Altitud minima de seguridad a la que puede estar el satelite.(Entrada)
Altitud_Perdida: Cantidad de altitud que se pierde en cada orbita. (Salida)
Cd: Coeficiente de arrastre satelite.(Entrada)
Orbitas: Cantidad de orbitas que ha realizado el satelite.(Salida)

Inicio
    Leer Altitud_Inicial("Altitud en km del satelite: ")
    Leer Altitud_Minima("Altitud minima en que el satelite puede sobrevivir el satelite: ")
    Leer Cd("Coeficiente de arrastre del satelite: ")
    Definir Altitud_Perdida = 0
    Definir Orbitas = 0
    Definir Altitud = Altitud_Inicial
    Mientras Altitud > Altitud_Minima:
        Definir Altitud_Perdida: Altitud*Cd
        Definir Altitud = Altitud-Altitud_perdida
        Definir Orbitas = Orbitas + 1 
        Definir Cd = Cd + 0.0001
        Escribir("En la orbita #(Orbita) la altitud del statelite es: (Altitud)")
        Fin mientras 
    Si Altitud < Altitud_Minima 
        Escribir("Se ha perdido conexión con satelite")
    Si Altitud_Perdida < 0.1
        Escribir("Satelite estable")
Fin