# atividade passada em aula para treino de condicionais...
NOTA1 = float(input("Digite a nota 1:"))
NOTA2 = float(input("Digite a nota 2:"))
MEDIA = (NOTA1 + NOTA2) / 2

if MEDIA <=4:
    print("Aluno reprovado.")
if MEDIA >=6:
    print("Aluno aprovado direto!") 
 

    if MEDIA >4 or MEDIA <6:
        print("Aluno em recuperação!")
else:

    RECUPERACAO = float(input("Digite a nota da recuperação:"))
if RECUPERACAO <=5:
    print("Reprovado na recuperação." )
if RECUPERACAO >5:
    print("Aprovado na recuperação!")    


