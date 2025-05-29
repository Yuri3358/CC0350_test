def maximo_personalizado(valores: list[float]) -> float:
    max_value = valores[0]
    for value in valores:
        if max_value < value:
            max_value = value
    return max_value