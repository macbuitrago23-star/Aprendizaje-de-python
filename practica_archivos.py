import json

#Datos de ejemplo

cuentas_ejemplo = [
    {"cliente": "Luisa", "total": 1800.0, "personas": 8},
    {"cliente": "Eduardo", "total": 360.0, "personas": 3},
    {"cliente": "Verónica", "total": 9900.0, "personas": 1}
]

# 1. Guardar
with open("prueba.json", "w", encoding="utf-8") as archivo:
    json.dump(cuentas_ejemplo, archivo, indent=2, ensure_ascii=False)
print("Guardado en prueba.json")

# 2. Leer
with open("prueba.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
print(f"Leído del archivo: {len(datos)} cuentas")

# 3. Mostrar
for cuenta in datos:
    print(f"  - {cuenta['cliente']}: ${cuenta['total']}")