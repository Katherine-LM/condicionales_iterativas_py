# W : corresponde al peso de la persona en Kg.
# H: corresponde a la altura en metros.
# IMC: EL valor del IMC, en [Kg/m2]

# Ingreso de los datos a través de input
W = float(input("Ingrese el peso en Kg: "))
H = float(input("Ingrese su altura en centímetros: "))

# Convertir la altura de centímetros a metros
H_metro = H / 100

# calcular el indice de masa corporal (imc)
imc = W / (H_metro ** 2)

# determinar el rango o categoría según los datos ingresados por usuario
if imc < 18.5:
    rango = "Bajo Peso"
elif 18.5 <= imc < 25:
    rango = "Adecuado"
elif 25 <= imc < 30:
    rango = "Sobrepeso"
elif 30 <= imc < 35:
    rango = "Obesidad Grado I"
elif 35 <= imc < 40:
    rango = "Obesidad Grado II"
else:
    rango = "Obesidad Grado III"

print(f"\nSu IMC es de: {imc:.2f}")
print(f"La clasificación OMS es: {rango}")
print("\n")

