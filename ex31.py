if __name__ == '__main__':
salario = float(input("Digite o seu salário: "))

    if salario <= 400:
        novo_salario = salario * 1.15
        reajuste = novo_salario - salario
        percentual = 15
    elif salario <= 800:
        novo_salario = salario * 1.12
        reajuste = novo_salario - salario
        percentual = 12
    elif salario <= 1200:
        novo_salario = salario * 1.10
        reajuste = novo_salario - salario
        percentual = 10
    elif salario <= 2000:
        novo_salario = salario * 1.07
        reajuste = novo_salario - salario
        percentual = 7
    else:
        novo_salario = salario * 1.04
        reajuste = novo_salario - salario
        percentual = 4

    print("Novo salario: {}".format(novo_salario))
    print("Reajuste ganho: {}".format(reajuste))
    print("Em percentual: {} %".format(percentual))
