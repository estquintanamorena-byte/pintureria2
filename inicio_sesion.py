import tkinter as tk
from tkinter import messagebox

# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("Sistema Gestión")
ventana.geometry("1366x768")
ventana.config(bg="#f0f2f5")  # Fondo gris claro

# ---------------- HEADER ----------------

header = tk.Frame(
    ventana,
    bg="#1e3a8a",   # Azul
    height=80
)

header.pack(fill="x")

titulo_header = tk.Label(
    header,
    text="SISTEMA DE GESTIÓN",
    bg="#1e3a8a",
    fg="white",
    font=("Arial", 24, "bold")
)

titulo_header.pack(pady=20)

# ---------------- CONTENEDOR LOGIN ----------------

frame_login = tk.Frame(
    ventana,
    bg="white",
    padx=40,
    pady=40,
    bd=2,
    relief="solid"
)

frame_login.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- TITULO LOGIN ----------------

titulo = tk.Label(
    frame_login,
    text="INICIO DE SESIÓN",
    bg="white",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=10)

# ---------------- USUARIO ----------------

titulo_usuario = tk.Label(
    frame_login,
    text="Usuario",
    bg="white",
    font=("Arial", 12)
)

titulo_usuario.pack(anchor="w")

entrada_usuario = tk.Entry(
    frame_login,
    width=30,
    font=("Arial", 12)
)

entrada_usuario.pack(pady=10)

# ---------------- CONTRASEÑA ----------------

titulo_contra = tk.Label(
    frame_login,
    text="Contraseña",
    bg="white",
    font=("Arial", 12)
)

titulo_contra.pack(anchor="w")

entrada_pass = tk.Entry(
    frame_login,
    show="*",
    width=30,
    font=("Arial", 12)
)

entrada_pass.pack(pady=10)

# ---------------- FUNCIÓN NUEVA VENTANA ----------------

def abrir_bienvenida():

    nueva_ventana = tk.Tk()
    nueva_ventana.title("Bienvenido")
    nueva_ventana.geometry("1366x768")
    nueva_ventana.config(bg="#f0f2f5")

    # Header
    header2 = tk.Frame(
        nueva_ventana,
        bg="#1e3a8a",
        height=80
    )

    header2.pack(fill="x")

    titulo2 = tk.Label(
        header2,
        text="PANEL PRINCIPAL",
        bg="#1e3a8a",
        fg="white",
        font=("Arial", 24, "bold")
    )

    titulo2.pack(pady=20)

    # Mensaje
    mensaje = tk.Label(
        nueva_ventana,
        text="¡Bienvenido al sistema!",
        bg="#f0f2f5",
        font=("Arial", 22)
    )

    mensaje.pack(expand=True)

    nueva_ventana.mainloop()

# ---------------- VALIDAR LOGIN ----------------

def validar_acceso():

    usuario = entrada_usuario.get()
    clave = entrada_pass.get()

    if usuario == "admin" and clave == "123":

        ventana.destroy()

        abrir_bienvenida()

    else:

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

# ---------------- BOTÓN ----------------

boton = tk.Button(
    frame_login,
    text="Ingresar",
    command=validar_acceso,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

boton.pack(pady=20)

# ---------------- EJECUTAR ----------------

ventana.mainloop()