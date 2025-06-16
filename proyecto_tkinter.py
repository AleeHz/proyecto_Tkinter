
import tkinter as tk

# import pedidos as pd

ventana = tk.Tk()
ventana.title("Calculadora de comidas compartidas")
ventana.geometry("700x570+300+100") #esos +400+200 son las coordenadas de la ventana en la pantalla
ventana.configure(bg='purple')

frame1 = tk.Frame(ventana)
frame1.configure(bg='purple')
texto = tk.Label(ventana, text="Bienvenido a la calculadora de comidas compartidas",
font=("Arial", 16), bg='purple', fg='white', relief=
"raised", padx=10, pady=10)
texto.pack(pady=10)


button_registrar = tk.Button(frame1, text="Registrar votante", bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
# button_registrar.config(bg='green', fg='white')
button_registrar.pack(side=tk.LEFT, padx=20,pady=20)


entrada_votante = tk.Entry(frame1,justify=tk.RIGHT)
entrada_votante.pack(side=tk.RIGHT, padx=20,pady=20)  
entrada_votante.get()  

frame1.pack()

frame2 = tk.Frame(ventana)
frame2.configure(bg='purple')

button_ver_votantes = tk.Button(frame2, text="Ver votantes", bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
button_ver_votantes.pack(pady=20,padx=20,side=tk.LEFT)

frame2.pack()

frame3 = tk.Frame(ventana)
frame3.configure(bg='purple')

button_agregar = tk.Button(frame3, text="Agregar comida",bg="orange", fg="white",relief="raised", padx=10, pady=10,border=5)
button_agregar.pack(pady=20,padx=20,side=tk.LEFT)

entrada_comida = tk.Entry(frame3,justify=tk.RIGHT)
entrada_comida.pack(pady=20,padx=20,side=tk.RIGHT)


frame3.pack()

frame5 = tk.Frame(ventana)
frame5.configure(bg='purple')

button_precios = tk.Button(frame5, text="Agregar precios",bg="orange", fg="white",relief="raised", padx=10, pady=10,border=5)
button_precios.pack(pady=20,padx=20,side=tk.LEFT)

entrada_precios = tk.Entry(frame5,justify=tk.RIGHT)
entrada_precios.pack(pady=20,padx=20,side=tk.RIGHT)

frame5.pack()

frame4 = tk.Frame(ventana)
frame4.configure(bg='purple')

button_calcular = tk.Button(frame4, text="Calcular total", bg="orange", fg="white",relief="raised", padx=10, pady=10,border=5)
button_calcular.pack(pady=20,padx=20,side=tk.LEFT)

frame4.pack()


button_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="orange", fg="white", relief="raised", padx=10, pady=10,border=5)
button_salir.pack()



ventana.mainloop()

