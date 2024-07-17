# calculando IMC utilizando as condicionais...
PESO = float(input("Digite o seu peso em Kg:"))
ALTURA = float(input("Digite a sua altura em m:"))
IMC = PESO / ALTURA ** 2

print(f"O seu IMC é {IMC}.")
if IMC > 25:
    print("Você está acima do peso!")
elif IMC < 18:
    print("Você está abaixo do peso!")
else:
    print("O seu peso está ok!")    