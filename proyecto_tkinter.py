# import pedidos as pd
import tkinter as tk







ventana = tk.Tk()
ventana.title("Calculadora de comidas compartidas")
ventana.geometry("400x300")


frame = tk.Frame(ventana)

texto = tk.Label(ventana, text="Bienvenido a la calculadora de comidas compartidas")
texto.pack(pady=10)


button_registrar = tk.Button(frame, text="Registrar votante", command=lambda: print("Función de registrar votante no implementada"))
button_registrar.config(bg='green', fg='white')
button_registrar.pack(pady=10)

button_ver_votantes = tk.Button(frame, text="Ver votantes", command=lambda: print("Función de ver votantes no implementada"))
button_ver_votantes.pack(pady=10)

button_agregar = tk.Button(frame, text="Agregar comida", command=lambda: print("Función de agregar comida no implementada"))
button_agregar.pack(pady=10)

entrada_comida = tk.Entry(ventana)
entrada_comida.pack(pady=10)



button_calcular = tk.Button(frame, text="Calcular total", command=lambda: print("Función de calcular total no implementada"))
button_calcular.pack(pady=10)

button_salir = tk.Button(frame, text="Salir", command=ventana.destroy)
button_salir.pack(pady=10)


frame.pack(pady=10)
ventana.mainloop()

