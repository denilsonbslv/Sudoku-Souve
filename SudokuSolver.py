import sys
import math

def criar_tabuleiro(lines):                     # Função que recebe um array das linhas e cria um tabuleiro com os valores
    tabuleiro = [                               # Criando a tabuleiro (matriz)
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""]
    ]
    for i in range(9):                          # Pegando os valores das linhas e adiconando ao tabuleiro
        j = 0
        for num in lines[i]:
            tabuleiro[i][j] = num
            j += 1
    return(tabuleiro)                           # Aqui retorno o tabuleiro para ser resolvido

def solucionarZero(tabuleiro, i, j):            # Função que retorna o número corresponde a cordenada recebida
    return 0;

def selecionarLinCol(tabuleiro):                # Função para pegar a linha ou a coluna para iniciar
    qtdZeroLin = [0,0,0,0,0,0,0,0,0]
    qtdZeroCol = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
        for j in range(9):
            if(tabuleiro[i][j] == "0"):
                qtdZeroLin[i] += 1
            if(tabuleiro[j][i] == "0"):
                qtdZeroCol[j] += 1
    linCol = [
        [qtdZeroLin.index(min(qtdZeroLin)), min(qtdZeroLin)],
        [qtdZeroCol.index(min(qtdZeroCol)), min(qtdZeroCol)]]

    return linCol


def solucionarCol(tabuleiro, coluna):
    print()

def solucionarLin(tabuleiro, linhaInd):         # Função para solucionar uma linha
    indicesZerados = []
    numerosFaltantes = []
    linha = tabuleiro[linhaInd]
    for i in range(9):
        if(linha[i] == '0'):
            indicesZerados.append(i)

        if(linha.count(str(i+1)) == 0):
            numerosFaltantes.append(i+1)

    print(numerosFaltantes)

def pegarColuna(tabuleiro, indColuna):
    coluna = []
    for i in range(9):
        coluna.append(tabuleiro[i][indColuna])
    return coluna;

def solucionarTabuleiro(tabuleiro):             # função que retorna o tabuleiro solucionado
    linCol = selecionarLinCol(tabuleiro)
    if(linCol[0][1] == linCol[1][1]):
        solucionarLin(tabuleiro, linCol[0][0])
    elif(linCol[0][1] < linCol[1][1]):
        solucionarLin(tabuleiro, linCol[0][0])
    else:
        solucionarCol(tabuleiro, linCol[1][0])                

lines = [                                       # Linhas usadas para testes
    "120070560",
    "507932080",
    "000001000",
    "010240050",
    "308000402",
    "070085010",
    "000700000",
    "080423701",
    "034010028"]

tabuleiro = criar_tabuleiro(lines)
solucionarTabuleiro(tabuleiro)