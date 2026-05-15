import sys #Llamamos a sys
nombre = input("Hola ¿Cual es tu nombre? ") #Establecemos una entrada de datos

intentos_propina = 0
intentos_personas = 0  #Establecemos los intentos para cada while
intentos_cuenta = 0


while intentos_cuenta < 3: #Establecemos el bucle de validacion #2

    try: 
        cuenta = float(input("¿Cual es la cuenta del cliente?")) #Entrada de datos con validacion.
        if cuenta <= 10: #Si la cuenta es menor o igual a 10 el usuario debe volver a intentarlo
            print("Lo siento debes agregar un valor valido. Vuelve a intentarlo") 
            intentos_cuenta += 1 #Se suma un intento al usuario
        else:
            print(f"Perfecto {nombre} tu cuenta es:  {cuenta}") #Si es mayor a 10 el usuario sigue
            break
    except ValueError: #Establecemos el except para que solo sea una entrada de numero y no de letras.
        print(f"Lo siento eso no es un numero. Intenta de nuevo")
        intentos_cuenta += 1 #Se suma un intento al usuario.
        continue

if intentos_cuenta == 3:
    print("Lo siento tus intentos se han agotado") #Mensaje de cierre para el usuario
    sys.exit() #Si los intentos son igual a 3 se cierra el sistema



while intentos_propina < 3: #Establecemos el bucle de validacion #2

    try:

        propina = int(input("Dime que porcentaje de propina ponemos: 10%, 15%, 20%... ")) #Se establece una entrada de datos numericos int()
        total2 = cuenta * propina / 100 #Calculamos el porcentaje de la cuenta

        if propina >= 100 or propina < 0: #Hacemos validacion la propina no debe ser menor a 0 ni mayor o igual a 100
            print(f"Lo siento eso no es un porcentaje valido. Vuelve a intentarlo") #Se invita al usuario a intentarlo de nuevo.
            intentos_propina +=1 #Se suma un intento mas al usuario.
        else:
            print(f"Y diste una propina de: {total2} en total") #Si la condicion se cumple muestra el total de la cuenta.
            break

    except ValueError: #Nuevamente se usa ValueError para permiter unicamente entrada de datos numericos.
        print("Lo siento eso no es un numero. Intenta de nuevo.") #Se invita al usuario a intentar de nuevo.
        intentos_propina += 1 #Se suma un intento mas al usuario
        continue

if intentos_propina == 3: #Se establece una condicion si intentos_propina llega a 3 cerramos sistema.
    print("Lo siento tus intentos se agotaron.") #Se le indica al usuario que sus intentos se agotaron.
    sys.exit() #Cerramos el sistema con sys.exit

cuenta_2 = cuenta + total2

while intentos_personas < 3: #Establecemos el bucle de validacion #3

    try:
        personas = int(input("¿Cuantas personas pagan 1,2,3...?")) #Se establece una entrada de numeros enteros con int()

        if personas <= 0: #Establecemos la condicion si personas es igual o menos a 0 no hacemos la cuenta final.
            print("Lo siento el numero de personas es minimo de 1. Intenta de nuevo.") #Invitamos al usuario a intentar de nuevo
            intentos_personas += 1 #Se le suma un intento al usuario
        else:
            cuenta_personas = cuenta_2 / personas #Se divide la cuenta con propina entre las personas que pagaran.
            print(f"Perfecto {nombre} tu cuenta se dividira en {personas} y la cuenta por persona es {round(cuenta_personas, 2)} gracias por preferirnos.") #Se imprime mensaje final con cuenta final.
            break #Terminamos el bucle

    except ValueError: #Nuevamente validamos con ValueError si son letras no nos deja pasar.
        print("Lo siento eso no es un numero. Intenta de nuevo.") #Invitamos al usuario a intentar nuevamente.
        intentos_personas += 1 #Le sumamos un intento
        continue #Continuamos con el bucle hasta que intentos_personas sea igual a 3

if intentos_personas == 3: #Si intentos_personas llega a 3 se cierra el sitema.
    print("Lo siento tus intentos se agotaron.") #Le indicamos al usuario que sus intentos se acabaron.
    sys.exit() #se cierra el sistema.
