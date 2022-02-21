#Calcular el indice de masa corporal, Fernando Esparza Tinoco,  20/02/2022, 20/02/2022.

p = float(input('Ingresa tu peso (Kg): '))
h = float(input("Ingresa tu altura (m): "))

imc = p / h**2

print("IMC: ", imc)
if imc < 16:
    print("criterio de ingreso hospitalario: ")
elif imc >= 16  and imc <17:
    print("Infrapeso: ")
elif imc >= 17 and imc <25:
    print("bajo peso: ")
elif imc >= 25 and imc <30:
    print("saludable: {}")
elif imc >= 30 and imc <35:
    print("Sobrepeso crónico")
elif imc >= 35 and imc <40:
    print("Obesidad premórbida")
elif imc > 40:
    print("Infrapeso")