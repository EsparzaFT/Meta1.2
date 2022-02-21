#Es o no un numero primo, Fernando Esparza Tinoco,  20/02/2022, 20/02/2022

num = int(input("Ingresa un numero: "))
def es_primo(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
print(es_primo(num))

