import tkinter as tk
from tkinter import messagebox


# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("SISTEMA GESTIÓN")
ventana.geometry("1366x768")

# Título
titulo = tk.Label(ventana, text="INICIO DE SESIÓN", font=("arial", 25))
titulo.pack(pady=10)
PRINT("HOLA")
# Usuario
titulo_usuario = tk.Label(ventana, text="Ingrese el usuario")
titulo_usuario.pack()

entrada_usuario = tk.Entry(ventana, width=30)
entrada_usuario.pack(pady=5)
# Contraseña
titulo_contra = tk.Label(ventana, text="Ingrese la contraseña")
titulo_contra.pack()

entrada_pass = tk.Entry(ventana, show="*", width=30)
entrada_pass.pack(pady=5)

# ---------------- FUNCIÓN PARA NUEVA VENTANA ----------------

def abrir_bienvenida():

    nueva_ventana = tk.Tk()
    nueva_ventana.title("Bienvenido")
    nueva_ventana.geometry("1366x768")

    mensaje = tk.Label(
        nueva_ventana,
        text="¡Bienvenido!",
        font=("Arial", 18)
    )

    mensaje.pack(expand=True)#Esto nos sirve para que el texto ocupe todo

    nueva_ventana.mainloop()

# ---------------- VALIDAR LOGIN ----------------

def validar_acceso():

    usuario = entrada_usuario.get() #aca guara en esta variable lo que el usuario escriba
    clave = entrada_pass.get()

    if usuario == "admin" and clave == "123":

        

        ventana.destroy()   # Cierra login

        abrir_bienvenida()  # Abre nueva ventana

    else:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )


        

# ---------------- BOTÓN ----------------

boton = tk.Button(
    ventana,
    text="Ingresar",
    command=validar_acceso,
     bg="#3d32e2",
     fg="white",
     
)


boton.pack(pady=10)




# ---------------- EJECUTAR ----------------

ventana.mainloop()