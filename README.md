# QA Tool 0.1

QA Tool 0.1 es una herramienta diseñada para realizar controles de calidad en archivos de audio. Este proyecto automatiza el análisis, detección de errores y evaluación de audio, lo que lo convierte en una solución útil para desarrolladores, ingenieros de sonido y cualquier persona interesada en la calidad del audio.

## 🚀 Características

- **Análisis automatizado de archivos de audio**: Evalúa múltiples parámetros como niveles de ruido, clipping, y otras métricas relevantes.
- **Soporte para múltiples formatos**: Trabaja con MP3, WAV, FLAC, y más.
- **Interfaz sencilla**: Diseñado para ser fácil de usar tanto desde la línea de comandos como con una interfaz gráfica (opcional).
- **Escalable y modular**: Fácil de adaptar e integrar en otros sistemas.

---

## 🛠️ Instalación

Sigue estos pasos para instalar y usar la herramienta en tu entorno local:

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/mario-sound/QA_Tool_0.1.git
   ```
2. **Navega al directorio del proyecto**:
   ```bash
   cd QA_Tool_0.1
   ```
3. **Crea un ambiente virtual con Conda (opcional pero recomendado)**:
   ```bash
   conda create --name qa_tool_env python=3.9
   conda activate qa_tool_env
   ```
4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Uso

### Desde la línea de comandos:

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```

---

## 📂 Estructura del proyecto

```

QA_Tool_0.1/
├── Tool/main.py # Script principal con la interfaz gráfica y algunas funcionalidades
├── Tool/audio_player.py # Módulo de reproducción del audio
├── Tool/excel_manager.py # Módulo de manejo de información respecto a archivos excel
├── Tool/qa_tool.py # Módulo con la lógica principal del programa
├── English/ # Carpeta con audios en inglés como ejemplo
├── Spanish/ # Carpeta con audios en español como ejemplo
├── counter_tool.xlsx # Archivo de excel para probar la herramienta
├── config.json # Archivo que guarda la configuración de las últimas rutas escogidas
└── README.md # Documentación del repositorio

```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar esta herramienta:

1. Haz un fork de este repositorio.
2. Crea una rama para tu funcionalidad o mejora: `git checkout -b nueva-funcionalidad`.
3. Realiza un pull request describiendo tus cambios.

---

## 📄 Licencia

No se permite el uso comercial sin permiso para esta licencia. Su uso está limitado a un uso educativo o divulgativo. Siempre que se haga público algún contenido relacionado, deberá mencionarse al autor de la herramienta.

---

## 📧 Contacto

Para dudas o sugerencias, puedes contactar a Mario Sound en [mario16msound@gmail.com](mailto:mario16msound@gmail.com) o abrir un [issue](https://github.com/mario-sound/QA_Tool_0.1/issues).

```

```
