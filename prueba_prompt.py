import os
from anthropic import Anthropic

cuentas_ejemplo = [
    {"cliente": "Samuel", "total": 33000.0, "personas": 5, "propina_pct": 10.0, "hora": "15:51"},
    {"cliente": "Carlos", "total": 210.0, "personas": 1, "propina_pct": 5.0, "hora": "18:30"},
    {"cliente": "Samuel", "total": 2600.0, "personas": 1, "propina_pct": 30.0, "hora": "16:30"}
]

detalle = ""
for c in cuentas_ejemplo:
    detalle += f"- Cliente: {c['cliente']}, Total: ${c['total']}, Personas: {c['personas']}, Propina: {c['propina_pct']}%, Hora: {c['hora']}\n"

    total_facturado = sum(c['total'] for c in cuentas_ejemplo)
    cantidad = len(cuentas_ejemplo)


    prompt = f"""Eres un analista de mercado especializado en negocios pequeños. Analizà los siguientes datos de la jornada de caja y dame 3 observaciones útiles y accionables para el dueño. Sé concreto y breve.
    
    Datos de la jornada:
    - Cantidad de cuentas: {cantidad}
    - Total facturado: ${total_facturado}

    Detalle de cuentas:
        \n{detalle}

    Dame tu análisis en lenguaje claro, como si le hablaras al dueño del restaurante."""



cliente = Anthropic()

mensaje = cliente.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\n=== ANÁLISIS DE LA IA ===\n")
print(mensaje.content[0].text)