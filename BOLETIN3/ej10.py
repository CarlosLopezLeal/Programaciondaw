'''En el gimnasio Jacatfitness para el que ya hemos trabajado nos piden que
realicemos un programa para determinar si deberías acudir al médico para que te
haga una revisión, para ello debemos hacer las siguientes preguntas:
● ¿Peso?
● ¿Edad?
● ¿Tipo de vida? (Sedentaria/Activa/Muy activa)
Las recomendaciones para ir al médico son:
● Si tienes más de 70 años y lleva una vida Sedentaria
● Si pesa más de 100 kg sea cual sea la edad.
● Si pesa más de 74,4 kg y tiene más de 50 años
En cualquier otro caso se mostrará “No es urgente que acuda al médico si no tiene
problemas de salud”'''



'''peso= int(input("Dime tu peso="))
edad= int(input("Dime tu edad="))
tipodvida= (input("Dime tu tipo de vida="))

if (edad>=70) and (tipodvida=="s"):
    print("Usted debería ir al médico.")
elif (peso>=100):
    print("Usted debería ir al médico.")
elif (peso>=74,4) and (edad>50):
    print("Usted debería ir al médico.")
else:
    print("No es urgente que acuda al médico si no tiene problemas de salud")'''

'''4'''

numero= int(input("Introduce un número en el rango 0 - 10000: \t"))

suma = 0
count = 0

while 0 <= numero <= 10000:
    suma+=numero
    count+=1
    numero = int(input("Introduce un número en el rango 0 - 10000\t"))


if count>0:
    print(f"Se ha introducido {count} números y la media es de {suma/count}")
else :
    print("No se ha introducido ningún número válido en ese rango")
