import pygame
import os

# Inicializar pygame mixer para reproducir audio
pygame.mixer.init()

def reproducir_audio(ruta_archivo):
    """Reproduce un archivo de audio dado."""
    if os.path.exists(ruta_archivo):
        pygame.mixer.music.load(ruta_archivo)
        pygame.mixer.music.play()
    else:
        print(f"El archivo {ruta_archivo} no existe.")

def detener_audio():
    """Detiene la reproducción de audio."""
    pygame.mixer.music.stop()
