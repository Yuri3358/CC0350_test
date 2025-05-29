def conta_ocorrencias(lista: list[int]) -> dict[int, int]:
    frequency_info = {}
    for number in lista:
        frequency_info[number] = lista.count(number)
    return frequency_info