if __name__ == '__main__':
soma = 0
Npositivos = 0
Nnegativos = 0
Ntotal = 0 

while true:
  numero = int(input("Digite um número (Caso queira sair, digite SAIR): "))
  if numero == SAIR:
    break 
  soma += numero 
  Ntotal += 1 
  if numero > 0: 
    Npositivos +=1
  elif valor < 0
    Nnegativos += 1 
if Ntotal > 0: 
  media = soma / Ntotal
  PorcentagemP = (Npositivos / Ntotal)*100
  PorcentagemN = (Nnegativos / Ntotal)*100 
  
  print("Média: ", media)
  print ("Números positivos: ", Npositivos)
  print ("Números negativos: ", Nnegativos) 
  print ("Percentual números positivos: ", PorcentagemP)
  print ("Percentual números negativos: ", PorcentagemN) 
  
  
