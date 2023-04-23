
n1 = float(input("Digite a 1ª nota: ")
n2 = float(input("Digite a 2ª nota: ")
n3 = float(input("Digite a 3ª nota: ")
n4 = float(input("Digite a 4ª nota: ")

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

if media >= 7.0:
    print("Media: {}".format(media))
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: {}".format(media))
    print("Aluno reprovado.")
else:
    print("Media: {}".format(media))
    print("Aluno em exame.")
   
    exame = float(input())
    final = (media + exame) / 2
   
 if final >= 5.0:
        print("Nota do exame: {}".format(exame))
        print("Aluno aprovado.")
 else:
      print("Nota do exame: {}".format(exame))
      print("Aluno reprovado.")
      print("Media final: {}".format(final))
