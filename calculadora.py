numero1 = 0
numero2 = 0
resultado = 0
operação = ""

while True:
    numero1 = int(input("digite o numero 1:"))
    operação = input("digite a operação:")
    numero2 = int(input("digite o numero 2:"))

    if operação == "+":
        resultado = numero1 + numero2
    elif operação == "-":
        resultado = numero1 - numero2
    elif operação == "/":
        resultado = numero1 / numero2
    elif operação == "*":
        resultado = numero1 * numero2
    elif operação == "**":
        resultado = numero1 ** numero2
    else:
        resultado = "operação invalida"

    print(str(numero1) + "" + str(operação) + "" + str(numero2) + "=" + str(resultado))
