if __name__ == '__main__':
  A = int(input("Digite o valor que voce quer calcular o !: "))
  fatorial= 1 
  resultado = str(A) + "! = "
  while A > 0:
     fatorial = A * fatorial  
      resultado += "x 1 = " + str(fatorial)
      print(resultado)
