import sys

def pedir_numero(mensaje, tipo, minimo, maximo, max_intentos=3):#Definimos pedir_numero con 3 parametros mesnaje, tipo y max_intentos con un valor predeterminado.
    intentos = 0 #contador de intentos para limitar reintentos del usuario.
    while intentos < max_intentos: #Condicionamos al while si intentos es menor a max_intentos vuelve a intentarlo.
        try: #Capturamos nuestro codigo con try.
            numero = tipo(input(mensaje)) #Pedimos una entrada de datos al usuario.
            if numero < minimo or numero > maximo:
                print(f"El numero debe estar en un rango entre {minimo} y {maximo}. Intenta de nuevo.")
                intentos += 1
            else:
                return numero 
        except ValueError: #Capturamos el error con except.
            print("Eso no es un numero valido. Intenta de nuevo.")#Mensaje de intenta de nuevo para el usuario.
            intentos += 1 #Sumamos un intento a la cuenta
    print("Tus intentos se acabaron lo siento. Cerrando programa... ")
    sys.exit()



edad = pedir_numero("¿Cuantos años tienes? ", int, 0, 120) #Llamamos a la funcion y le damos los argumento de mensaje y tipo.
print(f"Tu edad es {edad}") #Imprimimos la edad del usuario.

peso = pedir_numero("¿Cuanto pesas (kg)? ", float, 30, 300)#Llamamos una segunda vez a la funcion con argumentos diferentes para mensaje y tipo.
print(f"Tu peso es {peso}")#Imprimimos el peso del usuario.