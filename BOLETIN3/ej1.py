''' Escribe un programa que reciba las coordenadas de un punto respecto a los ejes XY y
determine el cuadrante en el que se encuentra el punto. Si se encuentra sobre un eje
debe indicar cuál..'''

x = int(input("Introduce la coordenada X: "))
y = int(input("Introduce la coordenada Y: "))

if(x > 0) and (y > 0):
    print("La coordenada está en el primer cuadrante")
elif(x < 0) and (y > 0):
    print("La coordenada está en el segundo cuadrante")
elif (x < 0) and (y < 0):
    print("El punto está en el tercer cuadrante.")
elif (x > 0) and (y < 0):
    print("El punto está en el cuarto cuadrante.")
elif (x == 0) and (y != 0):
       print("El punto está sobre el eje Y.")
elif (y == 0) and (x != 0):
    print("El punto está sobre el eje X.")
else:
    print("El punto está en el origen.")
