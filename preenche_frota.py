def define_posicoes (linha,coluna,orientacao,tam):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tam):
            posicoes.append([linha + i, coluna])
    else:
        for i in range(tam):
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tam):
    posicoes = define_posicoes(linha, coluna, orientacao, tam)
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
        
    return frota