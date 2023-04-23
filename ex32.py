salario = float(input("Digite seu salario: "))

if salario >= 0 and salario <= 2000:
print("Isento")
elif salario > 2000 and salario <= 3000:
print("R$ {}".format((salario - 2000) * 0.08))
elif salario > 3000 and salario <= 4500:
print("R$ {}".format(((salario - 3000) * 0.18) + 80))
else:
print("R$ {}".format(((salario - 4500) * 0.28) + 350))
