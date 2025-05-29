def maximo_personalizado(valores: list[float]) -> float:
    valores.sort(reverse=True)
    return valores[0]