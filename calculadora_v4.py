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
    print("Tus intentos se acabaron lo siento. Cerrando el programa... ")
    sys.exit()

# === PROGRAMA PRINCIPAL === #

nombre_cajero = input("¿Quien trabajara hoy?").strip().title()

cuentas_dia = [] #Lista para almacenar el total de cuentas con propina de cada usuario.

while True: #Bucle para  agregar otra cuenta o cerrar el sistema.
    respuesta = input("¿Otra cuenta? (sí/no): ").strip().lower() #Preguntamos al usuario si va agregar otra cuenta.
    if respuesta in ["no", "n", "nop"]: #Cuando la respuesta sea "no" cerramos el sistema.
        break
    elif respuesta in ["sí", "si", "s", "yeah"]: #Si la respuesta es si ejecutamos el programa.
        nombre_usuario = input("¿Cual es el nombre del cliente? ").strip().title()
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
        print(f"\nGracias por preferirnos.")
        cuenta_actual = {}

        cuenta_actual["cliente"] = nombre_usuario
        cuenta_actual["cuenta"] = cuenta  
        cuenta_actual["propina_pct"] = propina_porcentaje
        cuenta_actual["propina_monto"] = monto_propina
        cuenta_actual["total"] = total_con_propina
        cuenta_actual["personas"] = personas
        cuenta_actual["pago_por_persona"] = pago_por_persona

        cuentas_dia.append(cuenta_actual) #Se agrega un elemento a la lista vacia.


if len(cuentas_dia) == 0:
    print("No registraste ninguna cuenta esta noche. Cerrando el programa...")
else:
    cuenta_mas_alta = max(cuentas_dia, key=lambda x: x["total"])
    cuenta_mas_baja = min(cuentas_dia, key=lambda x: x["total"])
    total_facturado = sum(c["total"] for c in cuentas_dia)

    #Se hace un resumen de todas las cuentas, guardadas para el cierre.
    print("\n--- Resumen del día ---")
    print(f"Total de cuentas registradas: {len(cuentas_dia)}")
    print(f"Cuenta más alta: {cuenta_mas_alta['total']}")
    print(f"Cuenta más baja: {cuenta_mas_baja['total']}") 
    print(f"Suma total de la noche: {total_facturado}")
    print(f"Promedio por cliente:  {round(total_facturado / len(cuentas_dia), 2)}")
    print("Clientes atendidos:")
    for cuenta in cuentas_dia:
        print(f"  - {cuenta['cliente']}: ${cuenta['total']}")
    print(f"Gracias por tu servicio {nombre_cajero}.")
