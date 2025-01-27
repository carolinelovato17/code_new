INDICE, SOMA, K = 13, 0, 0
while K < INDICE:
    K += 1
    SOMA += K
print(SOMA)  # Resultado: 91


def fibonacci(num):
    seq, a, b = [0, 1], 0, 1
    while b < num:
        a, b = b, a + b
        seq.append(b)
    return num in seq

n = int(input("Número: "))
print(f"O número {n} pertence à Fibonacci." if fibonacci(n) else f"O número {n} não pertence.")


import json

faturamento = '{"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}'
dados = json.loads(faturamento)

valores = list(dados.values())
menor, maior, media = min(valores), max(valores), sum(valores) / len(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor: {menor}, Maior: {maior}, Dias acima da média: {dias_acima_media}")


faturamento = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
total = sum(faturamento.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")


def inverter(s):
    return s[::-1]

print(inverter(input("String: ")))
