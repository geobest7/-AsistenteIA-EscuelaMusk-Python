# Asistente Interactivo en Python

## Descripción
Este proyecto es un asistente en Python que permite realizar diversas tareas a través de un menú interactivo. Cada opción del menú corresponde a una función específica implementada en el asistente.

## Funcionalidades
1. **Traducción de texto**: Traduce un texto a un idioma especificado utilizando la API de OpenAI.
2. **Descarga de imágenes desde una URL**: Permite al usuario descargar una imagen desde una URL y guardarla en su sistema local.
3. **Resolución de problemas desde imágenes**: Carga una imagen en formato PNG que representa un problema matemático y utiliza OCR para extraer el texto y resolver el problema con GPT-4.
4. **Transcripción de audio**: Transcribe un archivo de audio a texto usando la API de OpenAI.
5. **Salir**: Termina la ejecución del programa.

## Requisitos
Para ejecutar este proyecto, necesitas instalar las siguientes dependencias:

```bash
pip install openai requests easyocr pillow python-dotenv
```

También debes configurar tu clave de API de OpenAI en un archivo `.env`:

```
OPENAI_API_KEY=tu_api_key_aqui
```

## Uso
Ejecuta el script principal en la terminal:

```bash
python ejercicio_gpt4.py
```

Luego, selecciona una opción del menú para realizar la tarea deseada.

## Ejemplo de Entrada/Salida

### 1. Traducción de texto
**Entrada:**
```json
{"texto": "Hola, ¿cómo estás?", "idioma": "en"}
```
**Salida:**
```plaintext
Traducción: Hello, how are you?
```

### 2. Descarga de imagen
**Entrada:**
```
Ingrese la URL de la imagen: https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png
Ingrese el nombre para guardar la imagen (ejemplo: imagen.png): logo.png
```
**Salida:**
```
Imagen descargada con éxito.
```

### 3. Resolución de problemas desde imágenes
**Entrada:**
```
Ingrese la ruta de la imagen PNG con el problema matemático: problema.png
```
**Salida:**
```
Texto detectado en la imagen: Calcula el área de un triángulo de base 5 cm y altura 10 cm.
Solución: El área del triángulo es 25 cm².
```

### 4. Transcripción de audio
**Entrada:**
```
Ingrese la ruta del archivo de audio: gpt4.mp3
```
**Salida:**
```
Transcripción: "Hola, este es un mensaje de prueba."
```

## Autor
Desarrollado para el Módulo 2 de IA & LLM.

## Notas adicionales
- El código usa `EasyOCR` para el reconocimiento de texto en imágenes.
- Para la transcripción de audio, se usa el modelo `whisper-1` de OpenAI.
- Asegúrate de contar con acceso a Internet para realizar las consultas a la API de OpenAI.

---

Si tienes alguna pregunta o sugerencia, no dudes en mejorar el código y contribuir al proyecto. 🚀

