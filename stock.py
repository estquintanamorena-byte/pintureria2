import tkinter as tk
from tkinter import ttk


#----------------- CONECTAR BASE DE DATOS ---

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="pintureria"
)

cursor = conn.cursor()

def obtener_productos():
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def eliminar_producto(id):
    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conn.commit()

    def actualizar_producto(id, nombre, marca, tipo, precio, stock):
    sql = """
    UPDATE productos
    SET nombre=%s, marca=%s, tipo=%s, precio=%s, stock=%s
    WHERE id=%s
    """
    cursor.execute(sql, (nombre, marca, tipo, precio, stock, id))
    conn.commit()

def agregar_producto(nombre, marca, tipo, precio, stock):
    sql = """
    INSERT INTO productos (nombre, marca, tipo, precio, stock)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, marca, tipo, precio, stock))
    conn.commit()
# ---------------- DATOS MOCK ----------------
productos = [
    ["Pintura Látex Interior", "Alba", "Látex", 25000, 45],
    ["Esmalte Sintético Blanco", "Sherwin", "Esmalte", 32000, 28],
    ["Acrílico Exterior", "Tersuave", "Acrílico", 38000, 15],
]

# ---------------- LOGIN ----------------
def login():
    usuario = usuario_var.get()
    rol = rol_var.get()

    if usuario:
        login_frame.destroy()
        crear_dashboard(usuario, rol)

# ---------------- DASHBOARD ----------------
def crear_dashboard(usuario, rol):
    header = tk.Frame(root, bg="#f5f5f5")
    header.pack(fill="x")

    tk.Label(header, text="Pinturería Sistema", font=("Arial", 16, "bold")).pack(anchor="w", padx=10)
    tk.Label(header, text=f"Bienvenido, {usuario} ({rol})").pack(anchor="w", padx=10)

    # Cards
    cards_frame = tk.Frame(root)
    cards_frame.pack(pady=10)

    crear_card(cards_frame, "Total Productos", "6", 0)
    crear_card(cards_frame, "Valor Inventario", "$4462k", 1)
    crear_card(cards_frame, "Stock Bajo", "2", 2)
    crear_card(cards_frame, "Ventas Hoy", "$156k", 3)

    # Tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    tab_inventario = tk.Frame(notebook)
    tab_ventas = tk.Frame(notebook)
    tab_clientes = tk.Frame(notebook)
    tab_empleados = tk.Frame(notebook)

    notebook.add(tab_inventario, text="Inventario")
    notebook.add(tab_ventas, text="Ventas")
    notebook.add(tab_clientes, text="Clientes")
    notebook.add(tab_empleados, text="Empleados")

    crear_tab_inventario(tab_inventario, rol)

# ---------------- CARDS ----------------
def crear_card(parent, titulo, valor, col):
    frame = tk.Frame(parent, bd=1, relief="solid", padx=10, pady=10)
    frame.grid(row=0, column=col, padx=5)

    tk.Label(frame, text=titulo).pack()
    tk.Label(frame, text=valor, font=("Arial", 14, "bold")).pack()

# ---------------- INVENTARIO ----------------
def crear_tab_inventario(frame, rol):
    top_frame = tk.Frame(frame)
    top_frame.pack(fill="x", pady=5)

    buscador = tk.Entry(top_frame)
    buscador.pack(side="left", padx=5)
    buscador.insert(0, "Buscar productos...")

    if rol == "Administrador":
        tk.Button(top_frame, text="+ Nuevo Producto", command=nuevo_producto).pack(side="right")

    # Tabla
    columnas = ("Producto", "Marca", "Tipo", "Precio", "Stock", "Valor Total")

    tabla = ttk.Treeview(frame, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)

    tabla.pack(fill="both", expand=True)

    # Cargar datos
    for p in productos:
        valor_total = p[3] * p[4]
        tabla.insert("", "end", values=(*p, valor_total))

# ---------------- NUEVO PRODUCTO ----------------
def nuevo_producto():
    ventana = tk.Toplevel(root)
    ventana.title("Nuevo Producto")

    labels = ["Nombre", "Marca", "Tipo", "Precio", "Stock"]
    entries = []

    for i, l in enumerate(labels):
        tk.Label(ventana, text=l).grid(row=i, column=0)
        e = tk.Entry(ventana)
        e.grid(row=i, column=1)
        entries.append(e)

    def guardar():
        datos = [e.get() for e in entries]
        productos.append([
            datos[0],
            datos[1],
            datos[2],
            int(datos[3]),
            int(datos[4])
        ])
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, columnspan=2)

# ---------------- UI PRINCIPAL ----------------
root = tk.Tk()
root.title("Sistema Pinturería")
root.geometry("900x600")

# Login UI
login_frame = tk.Frame(root)
login_frame.pack(pady=100)

tk.Label(login_frame, text="Usuario").pack()
usuario_var = tk.StringVar()
tk.Entry(login_frame, textvariable=usuario_var).pack()

tk.Label(login_frame, text="Rol").pack()
rol_var = tk.StringVar(value="Trabajador")
ttk.Combobox(login_frame, textvariable=rol_var, values=["Administrador", "Trabajador"]).pack()

tk.Button(login_frame, text="Ingresar", command=login).pack(pady=10)

root.mainloop()