import openai  # Librería para interactuar con la API de OpenAI y utilizar modelos de IA.
import requests  
import easyocr # EasyOCR es una librería de reconocimiento óptico de caracteres (OCR) que permite extraer texto de imágenes.
from PIL import Image  # Módulo de la biblioteca Pillow para manejar y procesar imágenes.
import json  
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar el archivo .env donde he guardado la API KEY

# Configurar la API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


#  Traducción de texto: Implementa una función que reciba un texto y un idioma objetivo, ambos
# proporcionados en formato JSON, y realice la traducción del texto al idioma indicado. El
# resultado debe ser mostrado en la consola.

def traducir_texto():
    datos = input("Ingrese el JSON con el texto y el idioma destino: ")
    try:
        datos_json = json.loads(datos)
        texto = datos_json["texto"]
        idioma = datos_json["idioma"]
        
        respuesta = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un traductor."},
                {"role": "user", "content": f"Traduce '{texto}' al idioma {idioma}."}
            ]
        )
        traduccion = respuesta.choices[0].message.content
        print("Traducción:", traduccion)
    except Exception as e:
        print("Error en la traducción:", str(e))


# Generación y descarga de imágenes desde una URL: El asistente debe permitir al usuario
# ingresar una URL de una imagen. Implementa una función que descargue la imagen desde la
# URL proporcionada y la guarde en el sistema local del usuario.

def descargar_imagen():
    url = input("Ingrese la URL de la imagen: ")
    nombre_archivo = input("Ingrese el nombre para guardar la imagen (ejemplo: imagen.png): ")
    
    try:
        respuesta = requests.get(url, stream=True)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                # Descargamos la imagen en fragmentos de 1024 bytes (1 KB) para evitar consumir mucha memoria
                for chunk in respuesta.iter_content(1024):
                    archivo.write(chunk)  # Escribimos cada fragmento en el archivo
            print("Imagen descargada con éxito.")
        else:
            print("Error al descargar la imagen.")
    except Exception as e:
        print("Error:", str(e))


# Resolución de problemas mediante imágenes: El asistente debe incluir una opción para cargar
# una imagen (en formato PNG), que puede representar un problema matemático. Implementa
# una función que reciba la ruta del archivo PNG y lo procese de acuerdo con el tipo de problema
# que debe resolver (esto puede variar según la naturaleza del ejercicio).

def resolver_problema_imagen():
    ruta = input("Ingrese la ruta de la imagen PNG con el problema matemático: ")

    try:
        # Cargar y mostrar la imagen
        imagen = Image.open(ruta)
        imagen.show()

        # Usar EasyOCR para extraer texto
        reader = easyocr.Reader(['es'])  # Español
        texto_extraido = " ".join(reader.readtext(ruta, detail=0))

        if not texto_extraido.strip():
            print("No se detectó texto en la imagen.")
            return

        print("Texto detectado en la imagen:", texto_extraido)

        # Enviar el problema a GPT-4 para resolverlo
        respuesta = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un experto en matemáticas."},
                {"role": "user", "content": f"Resuelve el siguiente problema matemático: {texto_extraido}"}
            ]
        )

        print("Solución:", respuesta.choices[0].message.content if respuesta.choices else "No se recibió respuesta.")

    except Exception as e:
        print("Error procesando la imagen:", str(e))


# Transcripción de audio: El asistente debe tener una función que permita al usuario cargar un
# archivo de audio y lo transcriba a texto. Implementa una funcionalidad para leer el archivo de
# audio desde la ubicación proporcionada y devolver la transcripción de su contenido.

def transcribir_audio():
    ruta = input("Ingrese la ruta del archivo de audio: ")
    
    try:
        with open(ruta, "rb") as archivo_audio:
            respuesta = openai.audio.transcriptions.create(
                model="whisper-1",
                file=archivo_audio
            )
            print("Transcripción:", respuesta.text)
    except Exception as e:
        print("Error en la transcripción:", str(e))


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Traducir texto")
        print("2. Descargar imagen desde URL")
        print("3. Resolver problema desde imagen")
        print("4. Transcribir audio")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            traducir_texto()
        elif opcion == "2":
            descargar_imagen()
        elif opcion == "3":
            resolver_problema_imagen()
        elif opcion == "4":
            transcribir_audio()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()


#traducir texto
# json: frase.json
# Imagen de prueba: https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png
# imagen problema: problemas.png
# audio: gpt4.mp3
