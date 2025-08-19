def verificar_aprovacao(media: float) -> str:
    if media < 0:
        return "Média inválida"
    if media >= 7.0:
        return "Aprovado"
    if media >= 5.0:
        return "Recuperação"
    return "Reprovado"
    