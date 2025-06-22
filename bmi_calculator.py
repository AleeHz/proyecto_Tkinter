import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # pasar a metros
        imc = peso / (altura ** 2)
        resultado = f"Tu IMC es: {imc:.2f}\n"

        if imc < 18.5:
            resultado += "Estás bajo de peso."
        elif 18.5 <= imc < 24.9:
            resultado += "Peso normal."
        elif 25 <= imc < 29.9:
            resultado += "Sobrepeso."
        else:
            resultado += "Obesidad."

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("300x300")
ventana.config(bg="#f0f0f0")

label_titulo = tk.Label(ventana, text="Calculadora de IMC", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_titulo.pack(pady=10)

label_peso = tk.Label(ventana, text="Peso (kg):", bg="#f0f0f0")
label_peso.pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

label_altura = tk.Label(ventana, text="Altura (cm):", bg="#f0f0f0")
label_altura.pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

btn_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="", bg="#f0f0f0", font=("Arial", 12))
label_resultado.pack()

ventana.mainloop()
