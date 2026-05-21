import tkinter as tk  # Importamos la librería para crear interfaces gráficas
from tkinter import messagebox  # Importamos el módulo para mostrar alertas o mensajes

# --- LÓGICA ----
#adentro de esta función deben realizar la validación
def validar_acceso():
    """Función que se ejecuta al presionar el botón 'Ingresar'"""
    
    # .get() extrae lo que se coloca en los campos de texto
    usuario = campo_usuario.get()
    contraseña = campo_contraseña.get()
    

def abrir_pantalla_bienvenida(nombre):
    """Función para crear una nueva ventana tras un login exitoso"""
    
    # .withdraw() oculta la ventana de login sin cerrarla del todo
    ventana_login.withdraw()
    
    # Toplevel() crea una ventana nueva que vive por encima de la principal
    ventana_bienvenida = tk.Toplevel()
    ventana_bienvenida.title("Sistema")  # Título de la nueva ventana
    ventana_bienvenida.geometry("300x200")  # Tamaño (DEBEN PONER EL DE SU MONITOR)
    
    # Creamos un mensaje de bienvenida usando el nombre del usuario
    tk.Label(ventana_bienvenida, text=f"Bienvenido, {nombre}", 
             font=("Arial", 14), pady=50).pack()
    
    # Botón para cerrar todo el programa
    # .destroy() cierra la ventana y finaliza el proceso de Python
    tk.Button(ventana_bienvenida, text="Cerrar", command=ventana_login.destroy).pack()


# FRONT

# Creamos el objeto principal de la interfaz
ventana_login = tk.Tk()
ventana_login.title("Login de Usuario")  # Texto en la barra superior
ventana_login.geometry("300x350")  # tamaño inicial de la ventana (DEBEN PONER EL DE SU MONITOR)

# Etiqueta de título
# pady agrega espacio (padding) vertical para que no esté todo pegado
tk.Label(ventana_login, text="Inicio de Sesión", font=("Arial", 18, "bold"), pady=20).pack()

# Etiqueta para el usuario
tk.Label(ventana_login, text="Usuario:").pack(pady=(10, 0))

# Campo de texto para el usuario
campo_usuario = tk.Entry(ventana_login)
campo_usuario.pack(pady=5) # .pack() ubica el elemento en la ventana

# Etiqueta para la contraseña
tk.Label(ventana_login, text="Contraseña:").pack(pady=(10, 0))

# Campo de texto para contraseña
# show="*" hace que lo que se escriba se vea como asteriscos por seguridad
campo_contraseña = tk.Entry(ventana_login, show="*")
campo_contraseña.pack(pady=5)

# Botón de Ingreso
# 'command=validar_acceso' indica qué función debe ejecutarse al hacer clic
tk.Button(ventana_login, text="Ingresar", command=validar_acceso, 
          bg="#4CAF50", fg="white", width=15).pack(pady=30)

# El mainloop mantiene la ventana abierta y "escuchando" eventos (clics, teclas)
ventana_login.mainloop()