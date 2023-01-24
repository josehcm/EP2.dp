def define_posicoes (linha,coluna,orientacao,tam):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tam):
            posicoes.append([linha + i, coluna])
    else:
        for i in range(tam):
            posicoes.append([linha, coluna + i])
    return posicoes