if __name__ == '__main__':
cod1 = int(input("Digite o código da peça 1: "))
peca1 = int(input("Digite a quantidade da peça 1: "))
valor_peca1 = float(input("Digite o valor da peça 1: "))

cod2 = int(input("Digite o código da peça 2: "))
peca2 = int(input("Digite a quantidade da peça 2: "))
valor_peca2 = float(input("Digite o valor da peça 2: "))

total = (peca1 * valor_peca1) + (peca2 * valor_peca2)

print("VALOR A PAGAR R$ {}".format(total))
