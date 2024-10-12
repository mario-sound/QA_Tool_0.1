import os
import tkinter as tk
from tkinter import ttk
from audio_player import reproducir_audio
from excel_manager import cargar_datos_excel, guardar_datos_excel
import platform

def iniciar_qa_tool(path_excel, carpeta_audios):
    # Crear la ventana principal
    root = tk.Tk()
    root.title('Herramienta QA de Audio')

    # Configurar estilo para cambiar el color de fondo de las cabeceras
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", background="black", foreground="white", fieldbackground="black")

    # Cargar datos del Excel
    datos = cargar_datos_excel(path_excel)

    # Verificar si la columna AsRec está vacía y copiar los valores de Spanish si es necesario
    if 'AsRec' not in datos.columns or datos['AsRec'].isnull().all():
        datos['AsRec'] = datos['Spanish'].copy()

    # Crear tabla con los datos
    tree = ttk.Treeview(root, columns=("Filename", "Transcripción Inglés", "Transcripción Español", "AsRec", "Reproducir"), show='headings')
    tree.heading("Filename", text="Nombre de Archivo")
    tree.heading("Transcripción Inglés", text="Transcripción Inglés")
    tree.heading("Transcripción Español", text="Transcripción Español")
    tree.heading("AsRec", text="AsRec (Editable)")
    tree.heading("Reproducir", text="Reproducir")

    # Insertar datos en la tabla solo si el archivo existe
    for index, row in datos.iterrows():
        nombre_archivo = row['filename'] + ".wav"  # Añadir la extensión .wav
        ruta_audio = os.path.join(carpeta_audios, nombre_archivo)

        # Comprobar si el archivo existe en la carpeta
        if os.path.exists(ruta_audio):
            tree.insert("", "end", values=(row['filename'], row['English'], row['Spanish'], row['AsRec'], "Play"))
        else:
            tree.insert("", "end", values=(row['filename'], row['English'], row['Spanish'], row['AsRec'], ""))  # No mostrar Play si no existe

    tree.pack()

    # Función para reproducir audios cuando se selecciona una fila
    def seleccionar_fila(event=None):
        item = tree.selection()[0]
        nombre_archivo = tree.item(item, 'values')[0] + ".wav"  # Obtener el nombre del archivo
        ruta_audio = os.path.join(carpeta_audios, nombre_archivo)  # Crear la ruta completa
        if os.path.exists(ruta_audio):  # Verificar que el archivo existe
            reproducir_audio(ruta_audio)

    # Función para reproducir la fila seleccionada al presionar la tecla espacio
    def reproducir_con_espacio(event=None):
        seleccionar_fila()  # Llamamos a la misma función que reproduce el audio

    # Vincular la tecla espacio para reproducir el archivo de la fila seleccionada
    root.bind('<space>', reproducir_con_espacio)
    
    # Reproducir al hacer doble clic en una fila
    tree.bind('<Double-1>', seleccionar_fila)

    # Reproducir automáticamente al moverse con las flechas
    tree.bind('<<TreeviewSelect>>', seleccionar_fila)

    # Función para editar la columna AsRec directamente en la tabla
    def edit_cell(event):
        # Detectar la fila y columna seleccionada
        item_id = tree.selection()[0]
        column = tree.identify_column(event.x)
        
        if column == '#4':  # Si es la columna "AsRec"
            # Obtener las coordenadas y mostrar Entry sobre la celda seleccionada
            x, y, width, height = tree.bbox(item_id, 3)
            entry = tk.Entry(root)
            entry.place(x=x, y=y, width=width, height=height)

            # Obtener el valor actual
            valor_actual = tree.item(item_id, 'values')[3]
            entry.insert(0, valor_actual)

            # Función para guardar el nuevo valor y cambiar el color de fondo
            def guardar_cambio(event):
                nuevo_valor = entry.get()
                tree.set(item_id, column="AsRec", value=nuevo_valor)

                # Actualizar el DataFrame para que se guarde correctamente
                idx = tree.index(item_id)  # Obtener el índice de la fila seleccionada
                datos.at[idx, 'AsRec'] = nuevo_valor  # Actualizar el DataFrame con el nuevo valor

                # Cambiar el color de la celda editada a gris claro
                tree.tag_configure('modificado', background='#d3d3d3')
                tree.item(item_id, tags='modificado')

                entry.destroy()

            # Guardar al presionar Enter
            entry.bind('<Return>', guardar_cambio)

            # Destruir el Entry al perder el foco
            entry.bind("<FocusOut>", lambda e: entry.destroy())

            entry.focus()

    # Vincular doble clic en la columna "AsRec" para editar directamente
    tree.bind('<Double-1>', edit_cell)

    # Función para guardar cambios y mostrar el mensaje temporal
    def guardar_cambios():
            guardar_datos_excel(datos, path_excel)
            # Mostrar mensaje de cambios guardados temporalmente
            label_guardado.config(text="Cambios guardados")
            root.after(2000, lambda: label_guardado.config(text=""))  # Borrar el mensaje después de 2 segundos

    # Crear un frame para colocar el botón y el mensaje en la parte inferior
    frame_inferior = tk.Frame(root)
    frame_inferior.pack(side="bottom", fill="x", pady=5)  # Espacio mínimo vertical para hacer más compacto

    # Botón para guardar cambios, alineado a la izquierda
    boton_guardar = tk.Button(frame_inferior, text="Guardar cambios", command=guardar_cambios)
    boton_guardar.pack(side="left", padx=10)

    # Añadir etiqueta que mostrará el mensaje de "Cambios guardados", alineado a la izquierda
    label_guardado = tk.Label(frame_inferior, text="", fg="green", width=20, anchor='w')
    label_guardado.pack(side="left", padx=10)

    # Añadir firma en la esquina inferior derecha dentro del mismo frame
    firma_label = tk.Label(frame_inferior, text="Digital Audio Dev 2024 ©", fg="lightgrey", anchor="e")
    firma_label.pack(side="right", padx=10)


    # Función para guardar con "cmd+s" en macOS
    def guardar_con_tecla(event=None):
        sistema = platform.system()
        if sistema == 'Darwin':  # Si estamos en macOS
            guardar_cambios()
        elif sistema == 'Windows':  # Si estamos en Windows
            guardar_cambios()

    # Vincular la combinación de teclas "cmd+s" en macOS y "ctrl+s" en Windows
    if platform.system() == 'Darwin':
        root.bind('<Command-s>', guardar_con_tecla)  # macOS
    else:
        root.bind('<Control-s>', guardar_con_tecla)  # Windows

    root.mainloop()
