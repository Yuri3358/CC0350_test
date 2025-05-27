def eh_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

def soma_positivos(valores: list[float]) -> float:
    acc = 0
    for number in valores:
        if number >= 0:
            acc += number
    return acc

def maximo_personalizado(valores: list[float]) -> float:
    valores.sort(reverse=True)
    return valores[0]

def conta_ocorrencias(lista: list[int]) -> dict[int, int]:
    frequency_info = {}
    for index, number in enumerate(lista):
        frequency_info[number] = lista.count(number)
    return frequency_info

def filtra_maiores_que(valores: list[float], limiar: float) -> list[float]:
    filtered_list = []
    for value in valores:
        if value > limiar:
            filtered_list.append(value)
    return filtered_list

def classifica_notas(notas: list[float]) -> list[str]:
    feedback_grades = []
    for nota in notas:
        if nota >= 6:
            feedback_grades.append("Aprovado")
        elif nota >= 4 and nota < 6:
            feedback_grades.append("Recuperação")
        elif nota < 4:
            feedback_grades.append("Reprovado")
    return feedback_grades
