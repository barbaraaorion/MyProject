# Programa para Converter Temperaturas...
print("Converter de Celsium para Kelvin e Fahrenheit...")
CELSIUS = int(input("Digite a temperatura:"))

KELVIN = CELSIUS + 273
FAHRENHEIT = (9 / 5 * CELSIUS) - 32
print(f"A temperatura em Kelvin será {KELVIN}.")
print(f"A temperatura em Fahrenheit será {FAHRENHEIT}.")

# Seria possível utilizar as estruturas condicionais if/elif/else ou match/case,
# para personalizar este programa, de forma que ele ofereça as três conversões?
# por exemplo, ele poderia perguntar ao usuário qual a unidade de medida e qual
# valor de temperatura ele quer converter e a partir daí, realizar os cálculos
# necessários...

# Atividade dia da semana treinando o uso da condicionaL if...
print("Motivação do dia:")
SEMANA = (input("Digite o dia da semana:"))
if SEMANA == "segunda":
    print("Respire fundo e seja corajoso!")
if SEMANA == "terça":
    print("Foco! Pense em seus objetivos!")
if SEMANA == "quarta": 
    print("Isso aí! Você está no caminho!")   

if SEMANA ==  "quinta":
    print("Não se desespere, você vai conseguir cumprir as metas!")

if SEMANA == "sexta":
    print("Concentre-se no trabalho e quando terminar, descanse!")

# Atividade conversão de temperatura treinando as condicionais match/case...
print("Qual conversão deseja realizar?")
ESCOLHA = int(input("1. Celsius / 2. Kelvin / 3. Fahrenheit:"))
TEMPERATURA = int(input("Digite o valor da temperautura:"))

match ESCOLHA:
    case 1:
        KELVIN = TEMPERATURA + 273
        FAHRENHEIT = (9 / 5 * TEMPERATURA) - 32
        print(f"A conversão de Celsius para Kelvin será {KELVIN}.")
        print(f"A conversão de Celsius para Fahrenheit será {FAHRENHEIT}.")
    case 2:
        CELSIUS = TEMPERATURA - 273
        FAHRENHEIT = 1.8 * (TEMPERATURA - 273) + 32  
        print(f"A conversão de Kelvin para Celsius será {CELSIUS}.")
        print(f"A conversão de Kelvin para Fahrenheit será {FAHRENHEIT}.")
    case 3:
        CELSIUS = 5/9 * (TEMPERATURA - 32)
        KELVIN = (TEMPERATURA - 32) / 1.8 + 273
        print(f"A conversão de Fahrenheit para Celsius será {CELSIUS}.")
        print(f"A conversão de Fahrenheit para Kelvin será {KELVIN}.")

                  