import tkinter as tk
import os
# ---------------- VENTANA PRODUCTOS ----------------

productos = tk.Tk()
productos.title("Productos")
productos.geometry("1200x700")
productos.config(bg="#f3f4f6")

# ---------------- HEADER ----------------

header = tk.Frame(
    productos,
    bg="#73d1d6",
    height=80
)

header.pack(fill="x")

titulo = tk.Label(
    header,
    text="GESTIÓN DE PRODUCTOS",
    bg="#73d1d6",
    fg="white",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=20)

# ---------------- CONTENEDOR ----------------

contenedor = tk.Frame(
    productos,
    bg="#f3f4f6"
)

contenedor.pack(pady=30)

# ---------------- TABLA ----------------

encabezados = [
    "ID",
    "Producto",
    "Color",
    "Precio",
    "Stock"
]

for i, texto in enumerate(encabezados):

    label = tk.Label(
        contenedor,
        text=texto,
        bg="#73d1d6",
        fg="white",
        font=("Arial", 12, "bold"),
        width=18,
        height=2,
        borderwidth=1,
        relief="solid"
    )

    label.grid(row=0, column=i)

# ---------------- PRODUCTOS ----------------

lista_productos = [
    ("1", "Latex Interior", "Blanco", "$15.000", "25"),
    ("2", "Esmalte Sintético", "Negro", "$12.000", "18"),
    ("3", "Barniz", "Natural", "$10.500", "12"),
    ("4", "Rodillo", "-", "$4.000", "30"),
    ("5", "Pincel", "-", "$2.500", "45")
]

for fila, datos in enumerate(lista_productos, start=1):

    for columna, valor in enumerate(datos):

        celda = tk.Label(
            contenedor,
            text=valor,
            bg="white",
            font=("Arial", 11),
            width=18,
            height=2,
            borderwidth=1,
            relief="solid"
        )

        celda.grid(row=fila, column=columna)

# ---------------- BOTÓN VOLVER ----------------

# ---------------- BOTÓN VOLVER ----------------

def volver():

    os.system("py inicio.py")

boton_volver = tk.Button(
    productos,
    text="Volver al Inicio",
    command=volver,
    bg="#73d1d6",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

boton_volver.pack(pady=30)