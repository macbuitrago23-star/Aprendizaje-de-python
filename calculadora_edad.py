from datetime import datetime
#Pedimos el nombre de el usuario y se guarda en la variable 'nombre'
nombre = input("¿Como te llamas?")
#Pedimos la fecha de nacimiento del usuario y se guarda en la variable 'nacimiento'
nacimiento = int(input("¿Cuando naciste?"))

tiempo = datetime.now()

#Hacemos anidamiento de funciones el primer if valida que los años de nacimiento sean razonables
#Luego si el año de nacimiento es correcto se ejecuta la 2 funcion.
if nacimiento < 1900 or nacimiento > 2026: 
    print(f"Parece que te equivocaste. {nacimiento} No es un año valido.")
else:
    #Definimos la funcion si el resultado de edad es menor a 18 es menor de edad.
    edad = tiempo.year - nacimiento
    if edad < 18:
        print(f"Lo siento {nombre} eres menor de edad. Tienes {edad} años.")
    else:
        print(f"Encantado de conocerte {nombre}, eres mayor de edad. Tienes {edad} años.")
