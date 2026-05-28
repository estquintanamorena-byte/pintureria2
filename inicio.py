import tkinter as tk
import os
# ---------------- VENTANA ----------------


inicio = tk.Tk()
inicio.title("Inicio - Pinturería ColorMix")
inicio.geometry("1366x768")
inicio.config(bg="#d1d5db")


# ---------------- HEADER ----------------


header = tk.Frame(
    inicio,
    bg="#73d1d6",
    height=100
)


header.pack(fill="x")


titulo = tk.Label(
    header,
    text="PINTURERÍA COLORMIX",
    bg="#73d1d6",
    fg="white",
    font=("Arial", 30, "bold")
)


titulo.pack(pady=20)


# ---------------- MENÚ ----------------


menu = tk.Frame(
    inicio,
    bg="#08122f",
    width=210
)


menu.pack(side="left", fill="y")


titulo_menu = tk.Label(
    menu,
    text="MENÚ",
    bg="#08122f",
    fg="white",
    font=("Arial", 18, "bold")
)


titulo_menu.pack(pady=30)


# ---------------- FUNCIÓN CERRAR SESIÓN ----------------


def cerrar_sesion():


    inicio.destroy()


    import inicio_sesion


# ---------------- BOTONES ----------------
# ---------------- ABRIR PRODUCTOS ----------------

def abrir_productos():

    inicio.destroy()

    os.system("py productos.py")

botones = [
    "Ventas",
    "Clientes",
    "Stock",
    "Proveedores",
    "Reportes"
]
# ---------------- ABRIR PRODUCTOS ----------------

# ---------------- BOTÓN PRODUCTOS ----------------

boton_productos = tk.Button(
    menu,
    text="Productos",
    command=abrir_productos,
    bg="#2563eb",
    fg="white",
    width=20,
    height=2,
    font=("Arial", 12, "bold"),
    cursor="hand2"
)

boton_productos.pack(pady=10)

# ---------------- OTROS BOTONES ----------------

botones = [
    "Ventas",
    "Clientes",
    "Stock",
    "Proveedores",
    "Reportes"
]

for texto in botones:

    tk.Button(
        menu,
        text=texto,
        bg="#2563eb",
        fg="white",
        width=20,
        height=2,
        font=("Arial", 12, "bold"),
        cursor="hand2"
    ).pack(pady=10)


# ---------------- BOTÓN CERRAR SESIÓN ----------------


boton_cerrar = tk.Button(
    menu,
    text="Cerrar Sesión",
    command=cerrar_sesion,
    bg="#73d1d6",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)


boton_cerrar.pack(pady=10)


# ---------------- CONTENIDO ----------------


contenido = tk.Frame(
    inicio,
    bg="#d1d5db"
)


contenido.pack(expand=True, fill="both")


bienvenida = tk.Label(
    contenido,
    text="¡Bienvenido al sistema de la Pinturería!",
    bg="#d1d5db",
    fg="#08122f",
    font=("Arial", 30, "bold")
)


bienvenida.pack(pady=50)


subtitulo = tk.Label(
    contenido,
    text="Administrá productos, ventas y stock fácilmente.",
    bg="#d1d5db",
    fg="#374151",
    font=("Arial", 18)
)


subtitulo.pack()
# ---------------- TARJETAS ----------------

frame_cards = tk.Frame(
    contenido,
    bg="#d1d5db"
)

frame_cards.pack(pady=50)

datos = [
    ("🎨 Productos", "250"),
    ("📦 Stock Bajo", "18"),
    ("🧾 Ventas Hoy", "34"),
    ("👥 Clientes", "120")
]

for titulo_card, numero in datos:

    card = tk.Frame(
        frame_cards,
        bg="white",
        width=220,
        height=140,
        bd=2,
        relief="solid"
    )

    card.pack(side="left", padx=20)

    card.pack_propagate(False)

    titulo_c = tk.Label(
        card,
        text=titulo_card,
        bg="white",
        font=("Arial", 16, "bold")
    )

    titulo_c.pack(pady=15)

    numero_c = tk.Label(
        card,
        text=numero,
        bg="white",
        fg="#73d1d6",
        font=("Arial", 28, "bold")
    )

    numero_c.pack()

inicio.mainloop()   