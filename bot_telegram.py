import os
from anthropic import Anthropic
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import json

cliente = Anthropic()

def cargar_historial(ruta="memoria_bot.json"): #Definimos cargar_historial con la ruta a buscar.

    try: #Capturamos el codigo.
        with open(ruta, "r", encoding="utf-8") as archivo: #Buscamos la ruta y la abrimos en modo lectura.
            return json.load(archivo) #Si existe el archivo devolvemos su contenido.
    except json.JSONDecodeError: #Si el archivo esta dañado empezamos con uno vacío.
        print("EL chat estaba corrupto. Empezando vacío.") #Avisamos al usuario.
        return{}
    except FileNotFoundError: #Si no existe el archivo empezamos con uno vacío.
        print(f"\nNo se encontro un chat previo. Empezando uno nuevo.") #Avisamos al usuario.
        return{}


def guardar_historial(chats, ruta="memoria_bot.json"): #Definimos guardar_historial con los parametros chats, y ruta con un valor por defecto.
    with open(ruta, "w", encoding="utf-8") as archivo: #Abrimos la ruta en modo escritura para guardar los nuevos datos.
        json.dump(chats, archivo, indent=2, ensure_ascii=False) #Escribimos el contenido de chats en el archivo de formato JSON.


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    todas_las_conversaciones = cargar_historial()
    id_usuario = str(update.message.from_user.id)
    historial_prompts = todas_las_conversaciones.get(id_usuario, [])
    todas_las_conversaciones[id_usuario] = historial_prompts
    texto_recibido = update.message.text

    save_messages = {}
    save_messages["role"] = "user"
    save_messages["content"] = texto_recibido
    historial_prompts.append(save_messages)

    mensaje = cliente.messages.create(
    model="claude-opus-4-8",
        max_tokens=1024,
        system= f"""Eres un experto en programación y analisis de datos, eres amable. Eres el asistente virtual en una agencia llamada nexo.
        Debes de analizar cada prompt y antes de entregar una respuesta analizar tu respuesta 3 veces. Siempre debes de saludar de forma amable y preguntar en que le puedes ayudar al cliente.
        Responde de forma amable y profesional las dudas de clientes potenciales. Las respuestas deben ser precisas y breves.""",
        messages=historial_prompts
    )

    assistant = {}
    assistant["role"] = "assistant"
    assistant["content"] = mensaje.content[0].text
    historial_prompts.append(assistant)
    guardar_historial(todas_las_conversaciones)
    await update.message.reply_text(f"{mensaje.content[0].text}")

app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot corriendo... (Ctrl + C para detener)")
app.run_polling()