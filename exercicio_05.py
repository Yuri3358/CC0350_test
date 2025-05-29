def filtra_maiores_que(valores: list[float], limiar: float) -> list[float]:
    filtered_list = []
    for value in valores:
        if value > limiar:
            filtered_list.append(value)
    return filtered_list