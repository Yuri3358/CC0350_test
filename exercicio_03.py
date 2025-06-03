def maximo_personalizado(valores: list[float]) -> float:
    highest_value = valores[0]
    for value in valores:
        if highest_value < value:
            highest_value = value
    return highest_value