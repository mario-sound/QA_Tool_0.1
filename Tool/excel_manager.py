import pandas as pd
import tkinter as tk

def cargar_datos_excel(ruta_excel):
    """Carga los datos del archivo Excel y los retorna como un DataFrame."""
    df = pd.read_excel(ruta_excel)
    return df

def guardar_datos_excel(datos, ruta_excel):
    """Guarda los datos modificados de nuevo en el archivo Excel."""
    datos.to_excel(ruta_excel, index=False)

def editar_asrec(tree, datos, item, root):
    """Permite editar el contenido de la columna AsRec al hacer doble clic."""
    # Editar el contenido de AsRec
    ventana_editar = tk.Toplevel(root)
    ventana_editar.title("Editar AsRec")

    # Obtener el valor actual de AsRec
    valor_actual = tree.item(item, 'values')[3]

    # Crear un campo de entrada con el valor actual
    entrada_editar = tk.Entry(ventana_editar, width=50)
    entrada_editar.pack()
    entrada_editar.insert(0, valor_actual)

    def guardar_cambio():
        nuevo_texto = entrada_editar.get()
        
        # Actualizar el valor en la tabla
        tree.set(item, column="AsRec", value=nuevo_texto)

        # Actualizar el DataFrame con el nuevo valor
        datos.at[tree.index(item), 'AsRec'] = nuevo_texto

        # Cerrar la ventana emergente
        ventana_editar.destroy()

    # Botón para guardar el cambio
    boton_guardar = tk.Button(ventana_editar, text="Guardar", command=guardar_cambio)
    boton_guardar.pack()

