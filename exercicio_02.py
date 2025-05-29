def soma_positivos(valores: list[float]) -> float:
    acc = 0
    for number in valores:
        if number >= 0:
            acc += number
    return acc
