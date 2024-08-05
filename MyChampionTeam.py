#atividade qual o melhor clube de futebol do Brasil...

CONTADOR = 0 ; CLUBE = ""
while CLUBE !="Botafogo":
    print("Qual o melhor clube de futebol  do Brasil?")
    CLUBE = input()

    if CLUBE == "Botafogo":
        print("Acertou! Parabéns!")
        break
    else:
        print("Errou. Vamos tentar novamente, digite o melhor clube de futebol do Brasil:")
        CLUBE = input()
