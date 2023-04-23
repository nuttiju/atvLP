if __name__ == '__main__':
  cod = int(input("Digite o código do item: "))
  quant = int(input("Digite a quantidade do item: "))
  

if cod == 1:
    preco = quant * 4.00
elif cod == 2:
    preco = quant * 4.50
elif cod == 3:
    preco = quant * 5.00
elif cod == 4:
    preco = quant * 2.00
elif cod == 5:
    preco = quant *1.50
else:
    print("Código inválido.")

print("Total: R$ {}".format(total))
