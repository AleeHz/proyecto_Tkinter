votantes = set ()
comidas = set ()
comida_y_montos =  {}

print("Regístrese o escriba 'salir' para terminar: ")
def registro ():
        while True:
                nombre = input().strip().lower()
                if nombre == "salir":
                                break
                if nombre in votantes:
                        print("Usted ya voto o escribe salir para finalizar")
                else:
                        votantes.add(nombre)
                        print("Voto registrado. Siga registrando votantes o escriba salir para finalizar")
registro()
print("Votantes registrados:",votantes)

print("Elija una comida o escriba 'salir' para terminar: ")
def menu():
        while True:
                plato = input().strip().lower()
                if plato == "salir":
                        break
                if plato in comidas:
                        print("Ya se agrego esta comida o escribe salir para finalizar")
                        continue
                try:
                        precio = float(input(f" Precio de {plato}:" ))
                        comidas.add(plato)
                        comida_y_montos[plato]=precio
                        print("comida y precio registrado")
                        print("Escriba salir si termino, de lo contrario siga")
                except ValueError:
                        print("Precio invalido. Intentelo de nuevo")
menu()
print("Comida registrada:",comida_y_montos)

for comida,precio in comida_y_montos.items():
        print(f"{comida} su precio es {precio}")
        continue 
suma_votantes = len(votantes)
suma_precio= sum(comida_y_montos.values())

if suma_votantes !=0:
        total_cada_uno= suma_precio / suma_votantes
        print(f"En total cada uno debe pagar es: {total_cada_uno}")
else:
        print("Debe haber minimo una persona para hacer esta dividion de precios")

        def agregar_comida(comida, precio):
                if comida in comidas:
                        return False
                try:
                        precio = float(precio)
                        comidas.add(comida)
                        comida_y_montos[comida] = precio
                        return True
                except ValueError:
                        return None            



def calcular_total():
        
        if len(votantes) ==0 :
                return 0
        total= sum(comida_y_montos.values())
        return round(total / len(votantes),2 )
