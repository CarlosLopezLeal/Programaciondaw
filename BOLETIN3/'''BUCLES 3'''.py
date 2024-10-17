'''BUCLES 3'''

#SACAR INGRESAR DINERO ...
MENU= '''
    Seleccione una opción:
        1.Ingresar dinero
        2.Retirar efectivo
        3.Consultar saldo
        4.Salir
    '''
print(MENU)
opcion_seleccionada = -1

dinero_en_cuenta= 0
ingreso=0
retirada=0
historico=""

while opcion_seleccionada != 4:
    if opcion_seleccionada == 1:
        cantidad_ingresar=int(input("¿Qué cantidad desea ingresar?:"))

        while cantidad_ingresar<0:
            cantidad_ingresar = int(input("Introduzca una cantidad válida"))

        dinero_en_cuenta+=cantidad_ingresar
        historico += f"Operación {ingreso+retirada}: Ingreso realizado por {cantidad_ingresar}, Total {dinero_en_cuenta}"

    elif opcion_seleccionada == 2:
        
        cantidad_retirar = int(input("¿Qué cantidad desea retirar?"))
        dinero_en_cuenta-=cantidad_retirar

        while cantidad_retirar > dinero_en_cuenta or cantidad_retirar < 0 :
        
            cantidad_retirar=int(input("Introduzca un importe valido ¿Qué cantidad desea retirar?:"))
            historico += f"Operación {ingreso+retirada}: Ingreso realizado por {cantidad_retirar}, Total {dinero_en_cuenta}"

    elif opcion_seleccionada == 3:
        print(f"Dispone un saldo en la cuenta corriente de {dinero_en_cuenta}")

    opcion_seleccionada = int(input("¿Qué operación quiere realizar?"))



