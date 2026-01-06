def gerar_relatorio(temp, umid,press):
    return f"""
    relatorio de condições  climáticas
    ----------------------------------
    Temperatura média:{temp:.2f} ªC
    Umidade média:{umid:.2f}%
    Pressão média:{press:.2}hPa
    """