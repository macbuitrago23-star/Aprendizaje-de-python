import requests
name = input("Calculemos tu edad, cual es tu nombre?").strip()
respuesta = requests.get("https://api.agify.io?name=" + name)

print(respuesta.status_code)

datos = respuesta.json()
datos["name"] = name

print(f"Tu nombre es: {datos['name']}")
print(f"Tu edad estimada es de: {datos['age']} años")
print(f"El numero de personas con este nombre es de: {datos['count']} personas")