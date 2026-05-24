cliente = {
    "nombre": "Miguel",
    "edad": 25,
    "ciudad": "Bogotá",
    "ocupacion": "Desarrollador"
}

print(f"Nombre: {cliente['nombre']}")
print(f"Edad: {cliente['edad']}")

#Modificar
cliente["edad"] = 26
cliente["telefono"] = "300-123-4567"
print(f"\nDespues de modificar:")

#Iterar con items
for clave, valor in cliente.items():
    print(f" {clave}: {valor}")

#Lista de diccionarios

cuentas_noche = [
    {"cliente": "Miguel", "total": 110.0, "personas": 3},
    {"cliente": "Ana", "total": 287.5, "personas": 4},
    {"cliente": "Carlos", "total": 96.0, "personas": 2}
]

print(f"\n--- Cuentas de la noche ---")
for cuenta in cuentas_noche:
    print(f" {cuenta['cliente']} pago ${cuenta['total']} (con {cuenta['personas']} personas)")
    