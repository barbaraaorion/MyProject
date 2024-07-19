#atividades para treino de condicionais antes das férias...
POSICAO = (input("Digite uma posição: "))

if POSICAO == ("goleiro") or POSICAO == ("zagueiro") or POSICAO == ("lateral"):
    print("defesa!")
elif POSICAO == ("volante") or POSICAO == ("meia"):
    print("Meio-campo!")
elif POSICAO == ("ponta") or POSICAO == ("centro-avante") or POSICAO == ("atacante"):
    print("ataque!")
else:
    print("Teimoso!")    
