from datetime import datetime
# Programa: Portero de discoteca
# El portero pregunta nombre y año de nacimiento.
# Si el año es inválido (fuera de 1950-2026), pide reintento.
# Tras 2 intentos fallidos, se rinde y rechaza a la persona.

intentos = 0
tiempo = datetime.now()

while intentos < 2:
    nombre = input("¿Cómo te llamas? ")

    try:
        nacimiento = int(input("¿En qué año naciste? "))
    except ValueError:
        print("Lo siento eso no es un numero. Intenta de nuevo.")
        intentos += 1
        continue
    
    if nacimiento < 1950 or nacimiento > 2026:
        print("Ese año no es válido. Intenta de nuevo.")
        intentos += 1
    else:
        edad = tiempo.year - nacimiento
        if edad < 18:
            print(f"Lo siento {nombre}, eres menor de edad. No puedes entrar.")
        else:
            print(f"Adelante {nombre}, buena noche.")
        break  # ← salimos del while porque ya verificamos

# Si salimos del while sin haber hecho break, fue por agotar intentos
if intentos == 2:
    print("Lo siento, se acabaron tus intentos. No puedo dejarte entrar.")
