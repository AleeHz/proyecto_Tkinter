
import tkinter as tk

from pedidos import votantes, comida_y_montos, agregar_comida, calcular_total   

#------------------------Funciones de la lógica del programa------------------------
from tkinter import messagebox
def registrar_votante():
    nombre = entrada_votante.get().strip().lower()
    if  nombre == "":
        messagebox.showwarning("Error", "Debe ingresar un nombre.")
        return
    if nombre in votantes:
        messagebox.showinfo("Ya registrado", f"{nombre} Usted ya ha votado.")
    else:
        votantes.add(nombre)
        messagebox.showinfo("Registrado", f"{nombre} Voto registrado.")
    entrada_votante.delete(0, tk.END)


def ver_votantes():
    if votantes:
        lista = "\n".join(votantes)
        messagebox.showinfo("Votantes registrados", lista)
    else:
        messagebox.showinfo("Sin votantes", "No hay votantes registrados.")

def agregar_alimento():
    comida = entrada_comida.get().strip().lower()
    precio = entrada_precios.get().strip()
    if not comida or not precio:
        messagebox.showwarning("Error", "Debe ingresar una comida y un precio.")
        return
    resultado = agregar_comida(comida, precio)
    if resultado is True:
        messagebox.showinfo("Exito", f"{comida} ha sido agregada con un precio de {precio}.")
    elif resultado is False:
        messagebox.showwarning("Error", f"{comida} ya ha sido agregada.")
    entrada_comida.delete(0, tk.END)
    entrada_precios.delete(0, tk.END)

def mostrar_comidas():
    if  comida_y_montos:
        list = ""
        for comida, precio in comida_y_montos.items():
            list += f"{comida} su precio es {precio}\n"
        messagebox.showinfo("Comidas registradas", list)
    else:
        messagebox.showinfo("Sin comidas", "No hay comidas registradas.")

def monto_total():
    if not votantes or not comida_y_montos:
        messagebox.showwarning("Error", "Debe haber al menos un votante y una comida registrada.")
        return
    total = calcular_total()
    messagebox.showinfo("Total a pagar", f"Cada votante debe pagar: {total}")





#------------------------Interfaz Gráfica con Tkinter------------------------


ventana = tk.Tk()
ventana.title("Calculadora de comidas compartidas")
ventana.geometry("800x1500") #esos +400+200 son las coordenadas de la ventana en la pantalla
ventana.configure(bg='purple')

frame1 = tk.Frame(ventana)
frame1.configure(bg='purple')
texto = tk.Label(ventana, text="Bienvenido a la calculadora de comidas compartidas",
font=("Arial", 16), bg='purple', fg='white', relief=
"raised", padx=10, pady=10)
texto.pack(pady=10)


button_registrar = tk.Button(frame1, text="Registrar votante", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=registrar_votante)
# button_registrar.config(bg='green', fg='white')
button_registrar.pack(side=tk.LEFT, padx=20,pady=20)


entrada_votante = tk.Entry(frame1,justify=tk.RIGHT)
entrada_votante.pack(side=tk.RIGHT, padx=20,pady=20)  
entrada_votante.get()  

frame1.pack()

frame2 = tk.Frame(ventana)
frame2.configure(bg='purple')

button_ver_votantes = tk.Button(frame2, text="Ver votantes", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=ver_votantes)
button_ver_votantes.pack(pady=20,padx=20,side=tk.LEFT)

frame2.pack()

frame3 = tk.Frame(ventana)
frame3.configure(bg='purple')

button_agregar = tk.Button(frame3, text="Agregar comida", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=agregar_alimento)
button_agregar.pack(pady=20,padx=20,side=tk.LEFT)

entrada_comida = tk.Entry(frame3,justify=tk.RIGHT)
entrada_comida.pack(pady=20,padx=20,side=tk.RIGHT)


frame3.pack()

frame5 = tk.Frame(ventana)
frame5.configure(bg='purple')

button_precios = tk.Button(frame5, text="Agregar precios", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=agregar_alimento)

button_precios.pack(pady=20,padx=20,side=tk.LEFT)

entrada_precios = tk.Entry(frame5,justify=tk.RIGHT)
entrada_precios.pack(pady=20,padx=20,side=tk.RIGHT)

frame5.pack()

frame6 = tk.Frame(ventana)
frame6.configure(bg='purple')

button_mostrar_comidas = tk.Button(frame6, text="Mostrar comidas", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=mostrar_comidas)
button_mostrar_comidas.pack(pady=20,padx=20,side=tk.LEFT)

frame6.pack()

frame4 = tk.Frame(ventana)
frame4.configure(bg='purple')


button_calcular = tk.Button(frame4, text="Calcular total", bg="orange", fg="white", relief="raised", padx=10, pady=10, border=5, command=monto_total)
button_calcular.pack(pady=20,padx=20,side=tk.LEFT)

frame4.pack()


button_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
button_salir.pack()

#------------------------Conectar los botones con las funciones------------------------








ventana.mainloop()

