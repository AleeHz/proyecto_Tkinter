# import pedidos as pd
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora de comidas compartidas")
ventana.geometry("700x500+300+100") #esos +400+200 son las coordenadas de la ventana en la pantalla
ventana.configure(bg='purple')

frame = tk.Frame(ventana)
frame.configure(bg='purple')
texto = tk.Label(ventana, text="Bienvenido a la calculadora de comidas compartidas",
font=("Arial", 16), bg='purple', fg='white', relief=
"raised", padx=10, pady=10)
texto.pack(pady=10)


button_registrar = tk.Button(frame, text="Registrar votante", bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
# button_registrar.config(bg='green', fg='white')
button_registrar.pack(pady=10)

button_ver_votantes = tk.Button(frame, text="Ver votantes", bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
button_ver_votantes.pack(pady=10)

button_agregar = tk.Button(frame, text="Agregar comida",bg="orange", fg="white",relief="raised", padx=10, pady=10,border=5)
button_agregar.pack(pady=10)

entrada_comida = tk.Entry(ventana)
entrada_comida.pack(pady=10)



button_calcular = tk.Button(frame, text="Calcular total", bg="orange", fg="white",relief="raised", padx=10, pady=10,border=5)
button_calcular.pack(pady=10)

button_salir = tk.Button(frame, text="Salir", command=ventana.destroy, bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
button_salir.pack(pady=10)


frame.pack(pady=10)
ventana.mainloop()

