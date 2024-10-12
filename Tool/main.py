import tkinter as tk
from tkinter import filedialog, messagebox
import json
from qa_tool import iniciar_qa_tool  # Importamos la función desde qa_tool
import os

# Archivo de configuración para guardar las rutas
config_file = './config.json'

# Función para cargar las rutas guardadas desde el archivo de configuración
def cargar_rutas_guardadas():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    return {"path_excel": "", "carpeta_audios": ""}

# Función para guardar las rutas en el archivo de configuración
def guardar_rutas(path_excel, carpeta_audios):
    with open(config_file, 'w') as f:
        json.dump({"path_excel": path_excel, "carpeta_audios": carpeta_audios}, f)

# Ventana para seleccionar las rutas
def ventana_rutas():
    # Cargamos las rutas guardadas anteriormente
    rutas_guardadas = cargar_rutas_guardadas()

    # Creamos la ventana para seleccionar las rutas
    ruta_window = tk.Tk()
    ruta_window.title("Seleccionar Rutas")

    # Etiqueta y campo de entrada para la ruta del Excel
    tk.Label(ruta_window, text="Ruta Excel:").grid(row=0, column=0, padx=10, pady=10)
    entry_excel = tk.Entry(ruta_window, width=50)
    entry_excel.grid(row=0, column=1, padx=10, pady=10)
    entry_excel.insert(0, rutas_guardadas.get("path_excel", ""))

    # Botón para seleccionar la ruta del Excel
    def seleccionar_excel():
        path_excel = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Excel files", "*.xlsx")])
        entry_excel.delete(0, tk.END)
        entry_excel.insert(0, path_excel)

    tk.Button(ruta_window, text="Buscar Excel", command=seleccionar_excel).grid(row=0, column=2, padx=10, pady=10)

    # Etiqueta y campo de entrada para la ruta de la carpeta de audios
    tk.Label(ruta_window, text="Ruta Carpeta Audios:").grid(row=1, column=0, padx=10, pady=10)
    entry_audios = tk.Entry(ruta_window, width=50)
    entry_audios.grid(row=1, column=1, padx=10, pady=10)
    entry_audios.insert(0, rutas_guardadas.get("carpeta_audios", ""))

    # Botón para seleccionar la carpeta de audios
    def seleccionar_carpeta_audios():
        carpeta_audios = filedialog.askdirectory(title="Seleccionar carpeta de audios")
        entry_audios.delete(0, tk.END)
        entry_audios.insert(0, carpeta_audios)

    tk.Button(ruta_window, text="Buscar Carpeta", command=seleccionar_carpeta_audios).grid(row=1, column=2, padx=10, pady=10)

    # Botón para confirmar las rutas
    def confirmar_rutas():
        path_excel = entry_excel.get()
        carpeta_audios = entry_audios.get()

        if not path_excel or not carpeta_audios:
            messagebox.showerror("Error", "Debe seleccionar ambas rutas.")
            return

        guardar_rutas(path_excel, carpeta_audios)
        ruta_window.destroy()
        iniciar_qa_tool(path_excel, carpeta_audios)  # Llamar a la función que inicia la herramienta de QA

    tk.Button(ruta_window, text="Confirmar", command=confirmar_rutas).grid(row=2, column=1, pady=20)

    ruta_window.mainloop()

# Ejecutamos la ventana de selección de rutas al iniciar el programa
if __name__ == '__main__':
    ventana_rutas()
