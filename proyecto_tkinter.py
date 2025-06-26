
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
        lista_nombre.insert(tk.END,nombre)
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
        lista_comida_y_precio.insert(tk.END, f"{comida} : {precio}")
    elif resultado is False:
        messagebox.showwarning("Error", f"{comida} ya ha sido agregada.")
    entrada_comida.delete(0, tk.END)
    entrada_precios.delete(0, tk.END)

def mostrar_comidas():
    if  comida_y_montos:
        list = ""
        for comida, precio in comida_y_montos.items():
            list += f"{comida} su precio es: {precio}\n"
        messagebox.showinfo("Comidas registradas", list)
    else:
        messagebox.showinfo("Sin comidas", "No hay comidas registradas.")

def monto_total():
    if not votantes or not comida_y_montos:
        messagebox.showwarning("Error", "Debe haber al menos un votante y una comida registrada.")
        return
    try:
        total = calcular_total()
        messagebox.showinfo("Total a pagar", f"Cada votante debe pagar: {total}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al calcular el total: {str(e)}")


def habilitar_agregar_comida():
    entrada_comida.pack(pady=20, padx=20, side=tk.RIGHT)
    entrada_precios.pack(pady=20, padx=20, side=tk.RIGHT)
    button_agregar.pack(pady=20, padx=20, side=tk.LEFT)
    frame_lista_comida.pack(side=tk.LEFT)
    button_mostrar_comidas.pack(pady=20, padx=20, side=tk.LEFT)
    button_terminar_comidas.pack(pady=20)

    entrada_votante.config(state=tk.DISABLED)
    button_registrar.config(state=tk.DISABLED)
    lista_nombre.config(state=tk.DISABLED)
    button_terminar_votacion.pack_forget()


def habilitar_agregar_precios():
    button_calcular.pack(pady=20, padx=20, side=tk.LEFT)
    button_salir.pack(pady=20)
    button_terminar_comidas.pack_forget()

def validar_string(s):
        return all(c.isalpha() or c.isspace() for c in s)
    
def validar_float(texto):
        try:
            if texto == "":
                return True
            float(texto)
            return True
        except ValueError:
            return False


#------------------------Interfaz Gráfica con Tkinter------------------------


ventana = tk.Tk()
ventana.title("Calculadora de comidas compartidas")
ventana.geometry("800x1500") #esos +400+200 son las coordenadas de la ventana en la pantalla
ventana.configure(bg='DeepSkyBlue3')

validar_str = ventana.register(validar_string)
validar_flt = ventana.register(validar_float)

frame1 = tk.Frame(ventana)
frame1.configure(bg='DeepSkyBlue3')



texto = tk.Label(ventana, text="Bienvenido a la calculadora de comidas compartidas",
font=("Arial", 16), bg='DeepSkyBlue3', fg='white', relief=
"raised", padx=10, pady=10)
texto.pack(pady=10)


button_registrar = tk.Button(frame1, text="Registrar votante", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=registrar_votante)

button_registrar.pack(side=tk.LEFT, padx=20,pady=20)


entrada_votante = tk.Entry(frame1,justify=tk.RIGHT, validate="key", validatecommand=(validar_str, '%P'))
entrada_votante.pack(side=tk.RIGHT, padx=20,pady=20)  
entrada_votante.get()  

frame1.pack()

frame2 = tk.Frame(ventana)
frame2.configure(bg='DeepSkyBlue3')

frame_lista = tk.Frame(frame2)
frame_lista.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_nombre = tk.Listbox(frame_lista,height=4, width=25, yscrollcommand= scrollbar.set)
lista_nombre.pack(side=tk.LEFT)

scrollbar.config(command=lista_nombre.yview)    

button_ver_votantes = tk.Button(frame2, text="Ver votantes", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=ver_votantes)
button_ver_votantes.pack(padx=20,side=tk.RIGHT)

button_terminar_votacion = tk.Button(frame2, text="Terminar votación", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=habilitar_agregar_comida)
button_terminar_votacion.pack(padx=20,side=tk.RIGHT)


frame2.pack()

frame3 = tk.Frame(ventana)
frame3.configure(bg='DeepSkyBlue3')

button_agregar = tk.Button(frame3, text="Agregar comida y precios", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=agregar_alimento)
button_agregar.pack(pady=20,padx=20,side=tk.LEFT)


entrada_comida = tk.Entry(frame3,justify=tk.RIGHT, validate="key", validatecommand=(validar_str, '%P'))
entrada_comida.pack(pady=20,padx=20,side=tk.RIGHT)



frame3.pack()

frame5 = tk.Frame(ventana)
frame5.configure(bg='DeepSkyBlue3')

frame_lista_comida = tk.Frame(frame5)
frame_lista_comida.pack(side=tk.LEFT)

scrollbar_comidas = tk.Scrollbar(frame_lista_comida)
scrollbar_comidas.pack(side=tk.RIGHT, fill=tk.Y)

lista_comida_y_precio = tk.Listbox(
    frame_lista_comida,
    height=4,
    width=25,
    yscrollcommand=scrollbar_comidas.set
)
lista_comida_y_precio.pack(side=tk.LEFT)

scrollbar_comidas.config(command=lista_comida_y_precio.yview)

entrada_precios = tk.Entry(frame5,justify=tk.RIGHT, validate="key", validatecommand=(validar_flt, '%P'))
entrada_precios.pack(pady=20,padx=20,side=tk.RIGHT)

frame5.pack()

frame6 = tk.Frame(ventana)
frame6.configure(bg='DeepSkyBlue3')

button_mostrar_comidas = tk.Button(frame6, text="Mostrar comidas", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=mostrar_comidas)
button_mostrar_comidas.pack(pady=20,padx=20,side=tk.LEFT)

button_terminar_comidas = tk.Button(frame6, text="Terminar comidas", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=habilitar_agregar_precios)
button_terminar_comidas.pack_forget()  
button_terminar_comidas.pack(pady=20) 

frame6.pack()

frame4 = tk.Frame(ventana)
frame4.configure(bg='DeepSkyBlue3')


button_calcular = tk.Button(frame4, text="Calcular total", bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10, border=5, command=monto_total)
button_calcular.pack(pady=20,padx=20,side=tk.LEFT)

frame4.pack()


button_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="SeaGreen2", fg="black", relief="raised", padx=10, pady=10,border=5)
button_salir.pack()



entrada_comida.pack_forget()
entrada_precios.pack_forget()
button_agregar.pack_forget()
frame_lista_comida.pack_forget()
button_mostrar_comidas.pack_forget()
button_terminar_comidas.pack_forget()
button_calcular.pack_forget()
button_salir.pack_forget()


ventana.mainloop()
