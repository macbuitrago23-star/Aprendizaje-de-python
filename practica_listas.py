cuentas = [100.0, 250.5, 180.0, 75.3, 320.0]

print("Total de cuentas registradas:", len(cuentas))
print("Cuenta más alta:", max(cuentas))
print("Cuenta mas baja:", min(cuentas))
print("Suma total de la noche:", sum(cuentas))
print("Promedio por cliente:", sum(cuentas) / len(cuentas))

print("\nDetalle de cada cuenta:")
for cuenta in cuentas:
    print(f"  - ${cuenta}")
