def afundados(frota, tabuleiro):
    afundados = 0
    for embarcacao in frota:
        for posicao in frota[embarcacao]:
            afundado = True
            for coordenada in posicao:
                if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                    afundado = False
            if afundado:
                afundados += 1
    return afundados