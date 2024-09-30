def percentual_faturamento():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = 0
    for valor in faturamento.values():
        total += valor

    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

percentual_faturamento()