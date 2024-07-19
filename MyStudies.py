# atividade passada em aula para treino de condicionais...
NOTA1 = float(input("Digite a nota 1:"))
NOTA2 = float(input("Digite a nota 2:"))
MEDIA = (NOTA1 + NOTA2) / 2

if MEDIA >= 6:
    print("Aluno aprovado.")
elif MEDIA >=4 and MEDIA <=6:
   NOTA3 = float(input("Digite a nota da recuperação: "))
   if NOTA3 >=5:
       print(" Aprovado na recuperação.")
   if NOTA3 < 5:
       print("Reprovado na recuperação")
else:
    print("Estudante reprovado.")           