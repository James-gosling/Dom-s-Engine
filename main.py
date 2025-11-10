# Archivo principal de Dom's Engine
import ollama

def main():
  print("🚀 Dom's Engine Iniciado 🚀")
  print("Probando conexión con Ollama...")

  try:
    models = ollama.list()
    print("Modelos de Ollama disponibles:")
    for model in models['models']:
      print(f"- {model['name']}")
  except Exception as e:
    print(f"Error al conectar con Ollama: {e}")
    print("Asegúrate de que el servidor de Ollama esté corriendo.")

if __name__ == "__main__":
  main()
