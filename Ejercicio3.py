#Determinar numero perfecto, Fernando Esparza Tinoco ,  20/02/022, 20/02/2022.

def NumPer(num):
    suma = 0
    for i in range(1, num):
        if (num % i == 0):
            suma += i
        if num == suma:
            return True
    else:
        return False

num = int(input("Introduce un numero para saber si es perfecto: "))

if NumPer(num):
    print("%s Es un numero perfecto" % num)
else:
    print("%s NO es un numero perfecto" % num)