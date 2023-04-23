if __name__ == '__main__':
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = (a + b + abs(a - b)) / 2
maior = (maior + c + abs(maior - c)) / 2

print("{} eh o maior".format(maior))
