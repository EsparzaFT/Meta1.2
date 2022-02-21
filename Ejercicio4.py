#Triangulo de asteriscos, Fernando Esparza Tinoco, 20/02/2022, 20/02/2020

num = int(input("Ingresa un numero: "))

for i in range(num):
    print(" " * (num - i - 1) + "*" * (2 * i + 1))