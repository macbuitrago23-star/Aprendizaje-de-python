#Imports 
import sys
from datetime import datetime
import json
from collections import Counter
import os
from anthropic import Anthropic

#   --- FUNCIONES ---   

def cuenta_nueva(mensaje, tipo, minimo, maximo, max_intentos= 2): #Definimos cuenta_nueva con los parametros mensaje, tipo, minimo, maximo y max_intentos con un valor por defecto.
    intentos = 0 #Guardamos la variable intentos, empieza en cero y se incremento si el usuario ingresa un valor incorrecto o no valido.

    while intentos < max_intentos: #Hacemos un bucle, mientras intentos sea menor a max_intentos le damos otro intento al usuario.
        try: #Capturamos nuestro codigo.
            numero = tipo(input(mensaje)) #Guardamos la variable numero y le asignamos el valor del input del usuario, con el mensaje que le pasamos a la funcion y lo convertimos al tipo que le pasamos a la funcion.

            if numero < minimo or numero > maximo: #Si el numero que el usuario ingresa es menor o mayor al establecido al llamar la funcion. Le damos un intento más al usuario.
                print(f"Lo siento pero la cuenta debe de estar en un rango valido entre: {minimo} y {maximo}. Itenta de nuevo")
                intentos += 1 #Sumamos un intento a la cuenta.
            else:
                return numero #Si los rangos son validos devolvemos numero.
        except ValueError: #Atrapamos el error para no permitir strings.
            print("Parece que eso no es un numero valido. Intenta de nuevo.")
            intentos += 1 #Sumamos un intento más al usuario.


        if intentos == 2: #Cuando los intentos se agotan cerramos el sistema.
            print(f"Lo siento pero tus intentos se agotaron. Cerrando el programa...")
            sys.exit()

# --- PERSISTENCIA ---

def cargar_historial(ruta="historial_caja.json"): #Definimos cargar_historial con la ruta a buscar.

    try: #Capturamos el codigo.
        with open(ruta, "r", encoding="utf-8") as archivo: #Buscamos la ruta y la abrimos en modo lectura.
            return json.load(archivo) #Si existe el archivo devolvemos su contenido.
    except json.JSONDecodeError: #Si el archivo esta dañado empezamos con uno vacío.
        print("Advertencia: el historial estaba corrupto. Empezando vacío.") #Avisamos al usuario.
        return[]
    except FileNotFoundError: #Si no existe el archivo empezamos con uno vacío.
        print("No se encontro un historial previo. Empezando vacío.") #Avisamos al usuario.
        return[]


def guardar_historial(cuentas, ruta="historial_caja.json"): #Definimos guardar_historial con los parametros cuentas, y ruta con un valor por defecto.
    with open(ruta, "w", encoding="utf-8") as archivo: #Abrimos la ruta en modo escritura para guardar los nuevos datos.
        json.dump(cuentas, archivo, indent=2, ensure_ascii=False) #Escribimos el contenido de cuentas en el archivo de formato JSON.




#   --- MENU PRINCIPAL ---
intentos_menu = 0 #Guardamos intentos_menu para el conteo de intentos del menu.
cuentas_dia = [] #Lista para guardar las cuentas del día, se reinicia cada vez que se ejecuta el programa.
historial_cuentas = cargar_historial() #Lista para guarda el historial de cuentas, se carga al iniciar el programa.

while intentos_menu < 2: #Mientras el contador de intentos_menu sea menor a 2 sigue en el bucle.
    cuenta_actual = {} #Diccionario para guardar cuentas.
    try:
        print(f"\n=== Sistema De Caja === ")
        print("1. Registrar nueva cuenta.")
        print("2. Ver resumen del día.")
        print("3. Ver historial completo.")
        print("4. Buscar cuentas por cliente")
        print("5. Analisis de caja con IA(CLAUDE)")
        print("6. Salir")

        opcion = int(input(f"\nElige una opción: ")) #Pedimos al usuario elegir una opcion entre 1 y 5, y lo convertimos a entero.

        if opcion in [1]: #Solo si 1 esta en opcion ejecutamos el codigo adentro.
            nombre_usuario = input("¿Cual es el nombre del cliente? ").strip().title() #Pedimos el nombre del cliente.
            cuenta = cuenta_nueva("¿Cual es la cuenta del cliente? ", float, 50, 100000000) #Llamamos a la funcion cuenta_nueva para obtener el valor de la cuenta, con un rango entre 50 y 100 millones.
            propina_porcentaje = cuenta_nueva("¿Que propina va a dejar el cliente? ", float, 0, 100) #Llamamos a la funcion cuenta_nueva para el porcentaje de propina, con un rango entre 0 y 100.
            personas = cuenta_nueva("¿Cuantas personas pagan? ", int, 1, 1000) #Llamamos a la funcion cuenta_nueva para el numero de personas, con un rango entre 1 y 1000.
            registro_fecha = datetime.now() #Guardamos la fecha y hora actual en la variable registro_fecha.
            fecha = registro_fecha.strftime("%Y-%m-%d") #Formateamos la fecha a un formato legible y la guardamos en la variable fecha.
            hora = registro_fecha.strftime("%H:%M") #Formateamos la hora a un formato legible y la guardamos en la variable hora.

            #Calculos
            monto_propina = cuenta * propina_porcentaje / 100
            cuenta_final = cuenta + monto_propina
            pago_por_persona = cuenta_final / personas

            #Resultados
            print(f"\nCuenta registrada con exito --- FECHA: {fecha} | HORA: {hora} ---")
            print(f"\nNombre del cliente: {nombre_usuario}")
            print(f"Cuenta del cliente: ${round(cuenta, 2)}")
            print(f"Propina: ({propina_porcentaje}%): ${round(monto_propina, 2)}")
            print(f"Total de la cuenta con propina: ${round(cuenta_final, 2)}")
            print(f"Total de pago por persona: ${round(pago_por_persona, 2)}")

            #Datos diccionario guardados en cuenta_actual.
            cuenta_actual["cliente"] = nombre_usuario
            cuenta_actual["cuenta"] = cuenta
            cuenta_actual["propina_pct"] = propina_porcentaje
            cuenta_actual["propina_monto"] = monto_propina
            cuenta_actual["total"] = cuenta_final
            cuenta_actual["personas"] = personas
            cuenta_actual["pago_por_persona"] = pago_por_persona
            cuenta_actual["fecha"] = fecha
            cuenta_actual["hora"] = hora

            cuentas_dia.append(cuenta_actual) #Agregamos la cuenta actual a la lista de cuentas_dia.
            historial_cuentas.append(cuenta_actual) #Agregamos la cuenta actual a la lista de historial_cuentas para mantener un registro completo.
            guardar_historial(historial_cuentas) #Llamamos a la funcion guardar_historial para actualizar el archivo JSON con el nuevo historial de cuentas.
        elif opcion in [2]: #Consultamos el registro diario si 2 esta en opcion.
            if len(cuentas_dia) == 0: 
                print("Lo siento no haz registrado ninguna cuenta. Registra una.") #Si no hay cuentas registradas se le avisa al usuario.
            else: #Si hay cuentas registradas se calcula la cuenta mas alta, la cuenta mas baja y el total facturado del día. Y se imprime el resumen diario.
                cuenta_mas_alta = max(cuentas_dia, key=lambda x: x["total"])
                cuenta_mas_baja = min(cuentas_dia, key=lambda x: x["total"])
                total_facturado = sum(c["total"] for c in cuentas_dia)

                # Resumen diario
                print(f"\n--- Resumen Del Día ---")
                print(f"Fecha y hora de consulta: {fecha} - {hora}.")
                print(f"Numero de cuentas registradas: {len(cuentas_dia)}")
                print(f"Total facturado hoy: ${round(total_facturado, 2)}")
                print(f"Cuenta más alta: ${cuenta_mas_alta['total']}")
                print(f"Cuenta más baja: ${cuenta_mas_baja['total']}")
                print(f"\nGracias por preferirnos.")
        elif opcion in [3]:
            if len(historial_cuentas) == 0:
                print("No hay cuentas registradas en el historial. Registra una.") #Si no hay cuentas en el historial avisamos al usuario.
            else: #Si hay cuentas en el historial se calcula el total.
                facturado_historico = sum(c["total"] for c in historial_cuentas) 
                clientes_recurrentes = [item["cliente"] for item in historial_cuentas]

                #Historial de cuentas.
                print(f"\n--- Historico De Cuentas ---")
                print(f"Numero de cuentas registradas: {len(historial_cuentas)}")
                print(f"Clientes atendidos: {', '.join(clientes_recurrentes)}")
                print(f"Total facturado: ${round(facturado_historico, 2)}")
        elif opcion in [4]:
            if len(historial_cuentas) == 0:
                print("No hay cuentas registradas. Para consultar una primero debes registrarla.") #Si no hay ningun registro no se consulta ninguna cuenta.
            else: #Si hay cuentas en el historial se le pide al usuario el nombre del cliente a buscar, se cuenta cuantas veces se repite ese cliente en el historial y se muestra la información de cada cuenta que coincida con el nombre del cliente buscado, incluyendo el gasto histórico total del cliente y las fechas y horas de cada cuenta encontrada. Si no se encuentra ninguna cuenta para ese cliente, se le informa al usuario.
                busqueda = input("¿Cual es el nombre del cliente que quieres buscar? ").strip().title()
                clientes_recurrencia = sum(1 for c in historial_cuentas if c["cliente"] == busqueda)
                encontrado = False
                for valor in historial_cuentas:
                    if valor["cliente"] == busqueda:
                        gasto_historico_cliente = sum(c["total"] for c in historial_cuentas if c["cliente"] == busqueda)
                        print(f"\n--- Cuenta Encontrada ---")
                        print(f"Cliente: {valor['cliente']}")
                        print(f"El cliente ha gastado en total: ${round(gasto_historico_cliente, 2)}")
                        print(f"Veces que el cliente nos ha visitado: {clientes_recurrencia}")
                        print(f"Fecha y hora de facturación: {valor['fecha']} - Hora: {valor['hora']}")
                        encontrado = True
                if not encontrado:
                    print(f"No se encontró ninguna cuenta para el cliente: {busqueda}")
        elif opcion in [5]:
            try:
                #Opciones
                print("1. Analizar el facturado historico.")
                print("2. Analizar facturado del día.")
                opcion_ia = int(input(f"\n¿Que quieres analizar hoy? "))
                cliente = Anthropic()

                if opcion_ia in [1]:
                    if len(historial_cuentas) == 0:
                        print("No hay ninguna cuenta registrada en el historial. Registra una y intenta de nuevo.")
                    else:
                        prompt_1 = input("¿Que análisis quieres que realice la IA? Escribe tu pregunta o indicación para el análisis: ")
                        detalles_historial = ""
                        for c in historial_cuentas:
                            detalles_historial += f"- Cliente: {c['cliente']}, Total: ${c['total']}, Propina: {c['propina_pct']}%, Personas: {c['personas']}, Hora: {c['hora']}\n"
                            facturado_total_ia = sum(c['total'] for c in historial_cuentas)

                        mensaje_historico = cliente.messages.create(
                            model="claude-opus-4-8",
                            max_tokens=1024,
                            system=f"""Eres un analista de mercado y economista especializado con negocios pequeños y medianos. Analizà los siguientes datos de caja y dame 3 observaciones útiles y accionables para el dueño. Sé concreto y breve.
                                        
                            === Datos de la jornada ===
                            - Cantidad de cuentas registradas: {len(historial_cuentas)}
                            - Total facturado historico: {facturado_total_ia}

                            Detalle cuentas:
                                \n{detalles_historial}

                            Dame tu análisis en lenguaje claro, como si le hablaras al dueño del restaurante.""",
                            messages=[
                                {"role": "user", "content": prompt_1}
                            ]
                        )

                    print("\n=== ANÁLISIS DE LA IA ===\n")
                    print(mensaje_historico.content[0].text)

                elif opcion_ia in [2]:
                    if len(cuentas_dia) == 0:
                        print("No haz registrado cuentas en el Día de hoy. Registra una y vuelve a intentarlo.") #Si no hay cuentas registradas en el día se le informa al usuario.
                    else:
                        prompt_2 = input("¿Que análisis quieres que realice la IA? Escribe tu pregunta o indicación para el análisis: ")
                        detalles_dia = ""
                        for c in cuentas_dia:
                            detalles_dia += f"- Cliente: {c['cliente']}, Total: ${c['total']}, Propina: {c['propina_pct']}%, Personas: {c['personas']}, Hora: {c['hora']}\n" 
                            facturado_dia_ia = sum(c['total'] for c in cuentas_dia)  


                        mensaje_dia = cliente.messages.create(
                            model="claude-opus-4-8",
                            max_tokens=1024,
                            system= f"""Eres un analista de mercado y economista especializado con negocios pequeños y medianos. Analizà los siguientes datos de caja y dame 3 observaciones útiles y accionables para el dueño. Sé concreto y breve.
                                        
                                === Datos de la jornada ===
                                - Cantidad de cuentas registradas: {len(cuentas_dia)}
                                - Total facturado historico: {facturado_dia_ia}

                                Detalle cuentas:
                                    \n{detalles_dia}

                                Dame tu análisis en lenguaje claro, como si le hablaras al dueño del restaurante.""",
                                messages=[
                                    {"role": "user", "content": prompt_2}
                                ]
                            )
                                    
                        print("\n=== ANÁLISIS DE LA IA ===\n")
                        print(mensaje_dia.content[0].text)

                else:
                    print("Lo siento eso no es una opcion valida. Intenta de nuevo.")
            except ValueError:
                print("Debes de elegir una opcion valida.")               
        elif opcion in [6]: #Si la opcion es 5 paramos el bucle y se cierra el sistema.
            print(f"\nSaliendo del programa...")
            break
        else: #Si la opcion no esta entre 1 y 5 el usuario debe de intentar de nuevo.
            print("Lo siento eso no es una opcion valida. Intenta de nuevo.")
    except ValueError: #Si el usuario pone texto se le informa.
        print("Debes elegir una opción valida.")
        intentos_menu += 1

        if intentos_menu == 2: #Cuando los intentos se agotan cerramos el sistema.
            print(f"Lo siento tus intentos se acabaron. Cerrando el programa...")
            sys.exit()
#TODO: 
# Raise
# Deuda tecnica crear un ID uno por cliente.
