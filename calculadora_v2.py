import sys
from datetime import datetime

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

# === PROGRAMA PRINCIPAL === #
nombre = input("Hola ¿Cual es tu nombre? ")

cuenta = pedir_numero("¿Cual es la cuenta del cliente?", float, 0, 9999999)
propina_porcentaje = pedir_numero("¿Que porcentaje de propina? (0-100) ", int, 0, 100)
personas = pedir_numero("¿Cuantas personas pagan? ", int, 1, 100)

# Calculos
monto_propina = cuenta * propina_porcentaje / 100
total_con_propina = cuenta + monto_propina
pago_por_persona = total_con_propina / personas

# Salida final
print(f"\n--- Resumen ---")
print(f"Cuenta: {cuenta}")
print(f"Propina ({propina_porcentaje}%): {round(monto_propina, 2)}")
print(f"Total con propina: {round(total_con_propina, 2)}")
print(f"Pago por persona: {round(pago_por_persona, 2)}")
print(f"\nGracias por preferirnos, {nombre}.")
