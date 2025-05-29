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