'''Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio (Norte/Sur) e
indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).'''

dia=int(input("dime el dia que es: "))
mes=int(input("dime el mes en el que estamos: "))
hemisferio = int(input("Introduce el hemisferio (Norte/Sur): ")) 
estacion =""


if hemisferio == "Norte":
    if (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
        estacion = "Otoño"
    elif (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    else:
        estacion = "Verano"
        
elif hemisferio == "Sur":
    if (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        estacion = "Otoño"
    else:
        estacion = "Invierno"


print(f"La estación actual en el hemisferio {hemisferio} es: {estacion}.")
