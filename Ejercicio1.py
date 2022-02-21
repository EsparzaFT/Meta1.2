#Calcular estimacion de importe de impuestos, Fernando Esparza Tinoco ,  20/02/2022, 20/02/2022


def imp(x):

    IMP = 0

    if x < 8000:
        IMP = 0
    if x > 8000 and x < 20000:
        IMP = x * .18
    if x > 20000 and x < 35000:
        IMP = x * .27
    if x > 35000:
        IMP = x * .38

    print("Impuestos Correspondientes ${0:.2f}".format(IMP))

imp(float(input("Ingresa los impuestos: ")))
