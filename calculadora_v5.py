import sys
from datetime import datetime
import json
from collections import Counter
from pathlib import Path

#Funciones 

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


def cargar_historial(ruta="historial.json"): #Definimos cargar_historial con el parametro ruta que define el nombre del archivo json.

    try:
        with open(ruta, "r", encoding="utf-8") as archivo: #Leemos el archivo json
            return json.load(archivo)
    except json.JSONDecodeError: #Si el archivo json esta dañado empieza con uno nuevo vacío.
        print("Advertencia: el historial estaba corrupto. Empezando vacío.") #Mensaje de aviso
        return[]
    except FileNotFoundError: #Si el archivo no se encuentra o no existe se crea uno nuevo vacío.
        print("No se encontro un historial previo. Empezando vacío.") #Mensaje de aviso
        return[]


def guardar_historial(cuentas, ruta="historial.json"): #Definimos guardar_historial con el parametro cuentas que es la lista de diccionarios a guardar y ruta que define el nombre del archivo json.
    with open(ruta, "w", encoding="utf-8") as archivo: #Escribimos sobre el archivo json usando utf-8 para legilibilidad.
        json.dump(cuentas, archivo, indent=2, ensure_ascii=False) 



# === PROGRAMA PRINCIPAL === #

nombre_cajero = input("¿Quien trabajara hoy?").strip().title()
archivo = Path("historial.json") #¿Existe este archivo?
cuentas_dia = [] #Lista para almacenar el total de cuentas con propina de cada usuario.
historial_cuentas = [] #Lista de diccionarios vacia para el historial de caja.
historial_cuentas = cargar_historial()

if archivo.exists(): #Usamos funciones de pathlib para validar si existe archivo.
    print(f"Historial previo cargado: {len(historial_cuentas)} cuentas registradas.") #Mensaje para usuario final.

while True: #Bucle para  agregar otra cuenta o cerrar el sistema.
    respuesta = input("¿Otra cuenta? (sí/no): ").strip().lower() #Preguntamos al usuario si va agregar otra cuenta.
    if respuesta in ["no", "n", "nop"]: #Cuando la respuesta sea "no" cerramos el sistema.
        break
    elif respuesta in ["sí", "si", "s", "yeah"]: #Si la respuesta es si ejecutamos el programa.
        nombre_usuario = input("¿Cual es el nombre del cliente? ").strip().title()
        cuenta = pedir_numero("¿Cual es la cuenta del cliente?", float, 10, 9999999)
        propina_porcentaje = pedir_numero("¿Que porcentaje de propina? (0-100) ", int, 0, 100)
        personas = pedir_numero("¿Cuantas personas pagan? ", int, 1, 100)
        registro_fecha = datetime.now()
        fecha = registro_fecha.strftime("%Y-%m-%d %H:%M")

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

        #Guardamos toda la información de la cuenta actual en un diccionario para luego agregarlo a la lista del día y al historial.
        cuenta_actual["cliente"] = nombre_usuario
        cuenta_actual["cuenta"] = cuenta  
        cuenta_actual["propina_pct"] = propina_porcentaje
        cuenta_actual["propina_monto"] = monto_propina
        cuenta_actual["total"] = total_con_propina
        cuenta_actual["personas"] = personas
        cuenta_actual["pago_por_persona"] = pago_por_persona
        cuenta_actual["fecha"] = fecha

        cuentas_dia.append(cuenta_actual) #Se agrega el diccionario a la lista.
        historial_cuentas.append(cuenta_actual) #Se agrega el diccionario a la segunda lista historica.
        guardar_historial(historial_cuentas)


if len(cuentas_dia) == 0:
    print("No registraste ninguna cuenta esta noche. Cerrando el programa...")
else:
    cuenta_mas_alta = max(cuentas_dia, key=lambda x: x["total"])
    cuenta_mas_baja = min(cuentas_dia, key=lambda x: x["total"])
    total_facturado = sum(c["total"] for c in cuentas_dia)

    #Se hace un resumen de todas las cuentas, guardadas para el cierre.
    print("\n--- Resumen del día ---")
    print(f"La fecha de hoy es: {fecha}")
    print(f"Total de cuentas registradas: {len(cuentas_dia)}")
    print(f"Cuenta más alta: {cuenta_mas_alta['total']}")
    print(f"Cuenta más baja: {cuenta_mas_baja['total']}") 
    print(f"Suma total de la noche: {total_facturado}")
    print(f"Promedio por cliente:  {round(total_facturado / len(cuentas_dia), 2)}")
    print("Clientes atendidos:")
    for cuenta in cuentas_dia:
        print(f"  - {cuenta['cliente']}: ${cuenta['total']}")
    print(f"Gracias por tu servicio {nombre_cajero}.")


if len(historial_cuentas) == 0:
    print("No hay registros de cuentas existente. Empieza a manejar tu caja.") #Si el historial esta vacio se muestra este mensaje.
else:
    facturado_historico = sum(c["total"] for c in historial_cuentas) #Sumamos el total de cada cuenta en el historial para obtener el total facturado historico.
    clientes_recurrentes = [item["cliente"] for item in historial_cuentas] #Creamos una lista con el nombre de los clientes de todo el historial para luego usarla en el conteo de clientes recurrentes.
    conteo_clientes = [elemento for elemento, conteo in Counter(clientes_recurrentes).items() if conteo > 1] #Usamos Counter para contar cuantas veces se repite cada cliente en el historial y asi identificar clientes recurrentes.

    #Se hace un resumen del historial completo de cuentas, guardadas para el cierre.
    print("\n--- Resumen Historico ---")    
    print(f"Total de cuentas en el historial: {len(historial_cuentas)}")
    print(f"Total facturado historico: {round(facturado_historico, 2)}")
    print(f"Clientes recurrentes: {conteo_clientes}") #Buscamos clientes que se repiten en el historial para identificar recurrentes.