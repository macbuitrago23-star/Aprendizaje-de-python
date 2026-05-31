import requests

pais = input("Dime un nombre de un país en inglés: ").strip().lower()
url = f"https://restcountries.com/v3.1/name/{pais}"

try:
    respuesta = requests.get(url)
except requests.exceptions.ConnectionError:
    print("No hay conexión a internet o el servidor no responde. Revisa tu red.")
    exit()

print(f"Código de estado: {respuesta.status_code}")

if respuesta.status_code == 200:
    datos = respuesta.json()
    info = datos[0]

    print(f"El pais que buscaste es: {info['name']['official']}")
    print(f"Su capital es: {info['capital'][0]}")
    print(f"Su población es de: {info['population']} habitantes.")
    print(f"Esta ubicada en la region de {info['region']}")

    monedas = info["currencies"]
    for codigo, detalle in monedas.items():
        print(f"Su moneda es: {detalle['name']} ({codigo})")
else:
    print("El país no se encontro o no existe. Verifica el nombre e intenta de nuevo.")