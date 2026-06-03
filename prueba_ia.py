import os
from anthropic import Anthropic

cliente = Anthropic()

mensaje = cliente.messages.create(
    model="claude-opus-4-8",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Hola Claude, decime en una frase qué es un sistema de caja."}
    ]
)

print(mensaje.content[0].text)