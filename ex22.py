if __name__ == '__main__':

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

triangulo = (a * c) / 2
circulo = 3.14159 * c ** 2
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print("TRIANGULO: {} ".format(triangulo))
print("CIRCULO: {} ".format(circulo))
print("TRAPEZIO: {} ".format(trapezio))
print("QUADRADO: {} ".format(quadrado))
print("RETANGULO: {} ".format(retangulo))
