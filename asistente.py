from anthropic import Anthropic
import json

cliente = Anthropic()

def cargar_historial(ruta="memoria_asistente.json"): #Definimos cargar_historial con la ruta a buscar.

    try: #Capturamos el codigo.
        with open(ruta, "r", encoding="utf-8") as archivo: #Buscamos la ruta y la abrimos en modo lectura.
            return json.load(archivo) #Si existe el archivo devolvemos su contenido.
    except json.JSONDecodeError: #Si el archivo esta dañado empezamos con uno vacío.
        print("Advertencia: el historial estaba corrupto. Empezando vacío.") #Avisamos al usuario.
        return{}
    except FileNotFoundError: #Si no existe el archivo empezamos con uno vacío.
        print(f"\nNo se encontro un chat previo. Empezando uno nuevo.") #Avisamos al usuario.
        return{}


def guardar_historial(chats, ruta="memoria_asistente.json"): #Definimos guardar_historial con los parametros chats, y ruta con un valor por defecto.
    with open(ruta, "w", encoding="utf-8") as archivo: #Abrimos la ruta en modo escritura para guardar los nuevos datos.
        json.dump(chats, archivo, indent=2, ensure_ascii=False) #Escribimos el contenido de chats en el archivo de formato JSON.




def analizar_con_ia(pregunta):
    todas_las_conversaciones = cargar_historial()
    nombre_usuario = input("¿Cual es tu nombre? ").strip().lower()
    historial_prompts = todas_las_conversaciones.get(nombre_usuario, [])
    todas_las_conversaciones[nombre_usuario] = historial_prompts
    print(f"[DEBUG] Conversación cargada de {nombre_usuario}: {len(historial_prompts)} mensajes")
    while True:
        prompt = input(pregunta).strip().lower()
        if prompt in ['salir', 's', 'exit']:
            print(f"\nFue un gusto atenderte, esperamos que vuelvas pronto. 👋")
            break
            
        save_prompt = {}
        assistant = {}
        save_prompt["role"] = "user"
        save_prompt["content"] = prompt
        historial_prompts.append(save_prompt)

        mensaje = cliente.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            system= f"""Eres un experto en programación y analisis de datos, eres amable. Eres el asistente virtual en una agencia llamada nexo.
            Debes de analizar cada prompt y antes de entregar una respuesta analizar tu respuesta 3 veces. Siempre debes de saludar de forma amable y preguntar en que le puedes ayudar al cliente.
            Responde de forma amable y profesional las dudas de clientes potenciales. Las respuestas deben ser precisas y breves.""",
            messages=historial_prompts
        )

        assistant["role"] = "assistant"
        assistant["content"] = mensaje.content[0].text
        historial_prompts.append(assistant)
        print(f"\n{mensaje.content[0].text}")
        guardar_historial(todas_las_conversaciones)

analizar_con_ia(f"\nEscribe o pregunta algo: ")