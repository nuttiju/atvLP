if __name__ == '__main__':
  a = float(input("Digite o primeiro número: ")
  b = float(input("Digite o segundo número: ")
  c = float(input("Digite o terceiro número: ")
  
if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print("PERIMETRO = {}".format(perimetro))
else:
    area = (a + b) * c / 2
    print("AREA = {}".format(area))
