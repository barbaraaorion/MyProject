#treinando condicionais...
TIME = str(input("Digite o nome de seu time:"))
POSICAO = int(input("Digite a posição no ranking:"))

if POSICAO == 1:
    print("É campeão!")
elif POSICAO >1 and POSICAO <=6:
    print("Libertadores!") 
elif POSICAO >6 and POSICAO <=12:
    print("Sul-Americana!")
elif POSICAO >12 and POSICAO <=16:
    print("Sem classificação.")
elif POSICAO >=17 and POSICAO <=20:
     print("Rebaixado...") 
else:
     print("Digite a posição correta!")               

