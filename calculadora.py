# inputs
cra = float(input("Qual é o seu CR atual? "))
p = int(input("\nQual período você está cursando? "))
crf = float(input("\nQuanto de CR vc quer ter/manter? "))

# function
def calcular_media_necessaria(cra, p, crf):
    media_necessaria = crf * p - cra * (p - 1)
    return media_necessaria
media = calcular_media_necessaria(cra, p, crf)

if media > 10:
    # Calcula o CR máximo possível com média 10
    cr_maximo = (cra * (p - 1) + 10) / p
    print(f"A média necessária ({media:.2f}) é impossível de atingir!")
    print(f"Com média máxima de 10.0, o CR máximo que você pode alcançar é: {cr_maximo:.2f}")
else:
    print(f"Você precisa tirar uma média de {media:.2f} neste semestre para atingir um CR de {crf}.")
