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
    indicesZeradosLin = []
    numerosFaltantesLin = []
    linha = tabuleiro[linhaInd]                 # Pegando a linha
    for i in range(9):                          # For para pegar os numeros que faltam e os indices para usar posteriormente
        if(linha[i] == '0'):
            indicesZeradosLin.append(i)
        if(linha.count(str(i+1)) == 0):
            numerosFaltantesLin.append(i+1)
    
    colunas = pegarColunas(tabuleiro, indicesZeradosLin) # Pegando as colunas ao qual o indice da linha é zero
    colMinZeros = pegarColMinZero(colunas)               # Pegando o indice da coluna com menos zeros
    indicesZeradosCol = []
    numerosFaltantesCol = []
    for i in range(9):
        if(colunas[colMinZeros][1][i] == '0'):
            indicesZeradosCol.append(i)
        if(colunas[colMinZeros][1].count(str(i+1)) == 0):
            numerosFaltantesCol.append(i+1)
    faltantesIguaisLinCol = pegarItrLinCol(numerosFaltantesLin, numerosFaltantesCol) # Pegando os números faltantes em comum da linha e da coluna
    if len(faltantesIguaisLinCol) == 1:                 # Verificando se existe apenas um número faltante em comum
        tabuleiro[linhaInd][colunas[colMinZeros][0][0]] = str(faltantesIguaisLinCol[0])
        solucionarTabuleiro(tabuleiro)                   # Aqui retorno para a função principal para que funcione de forma recursiva
    else:
        quadrado = pegarQuadrado(linhaInd, colunas[colMinZeros][0][0])
        numerosFaltantesQua = pegarFaltantesQua(quadrado);

    print(linhaInd, colunas[colMinZeros][0][0])

def pegarQuadrado(indLin, indCol):
    quadrado = []
    if (indLin >= 0 and indLin <= 2):
        if (indCol >= 0 and indCol <= 2):
            for i in range(0, 3):
                linha = []
                for j in range(0, 3):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 3 and indCol <= 5):
            for i in range(0, 3):
                linha = []
                for j in range(3, 6):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 6 and indCol <= 8):
            for i in range(0, 3):
                linha = []
                for j in range(6, 9):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        else:
            print("Não foi possivel definir quadrado >coluna<")
    elif (indLin >= 3 and indLin <= 5):
        if (indCol >= 0 and indCol <= 2):
            for i in range(3, 6):
                linha = []
                for j in range(0, 3):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 3 and indCol <= 5):
            for i in range(3, 6):
                linha = []
                for j in range(3, 6):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 6 and indCol <= 8):
            for i in range(3, 6):
                linha = []
                for j in range(6, 9):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        else:
            print("Não foi possivel definir quadrado >coluna<")
    elif (indLin >= 6 and indLin <= 8):
        if (indCol >= 0 and indCol <= 2):
            for i in range(6, 9):
                linha = []
                for j in range(0, 3):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 3 and indCol <= 5):
            for i in range(6, 9):
                linha = []
                for j in range(3, 6):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        elif (indCol >= 6 and indCol <= 8):
            for i in range(6, 9):
                linha = []
                for j in range(6, 9):
                    linha.append(tabuleiro[i][j])
                quadrado.append(linha)
            return quadrado
        else:
            print("Não foi possivel definir quadrado >coluna<")
    else:
        print("Não foi possivel definir quadrado >lina<")
        
def pegarItrLinCol(lin, col):
    itr = []
    if len(lin) > len(col):
        for vlr in col:
            for i in range(len(lin)):
                if vlr == lin[i]:
                    itr.append(vlr)
                    continue
    elif len(col) > len(lin):
        for vlr in lin:
            for i in range(len(col)):
                if vlr == col[i]:
                    itr.append(vlr)
                    continue
    else:
        for vlr in col:
            for i in range(len(lin)):
                if vlr == lin[i]:
                    itr.append(vlr)
                    continue
    return itr


def pegarColMinZero(colunas):                   # Função que retorna a coluna com menos zeros
    colMinZeros = 0
    qtdZerosColAux = 9
    for i in range(len(colunas)):
        qtdZerosCol = 0
        for vlr in colunas[i][1]:
            if vlr == '0':
                qtdZerosCol += 1
        if qtdZerosCol < qtdZerosColAux:
            colMinZeros = i
            qtdZerosColAux = qtdZerosCol
    return colMinZeros

def pegarColunas(tabuleiro, indZerados):        # Função para pegar as colunas referente ao ao indices zerados da linha
    colunas = []
    for indCol in indZerados:
        colunas.append([[indCol],pegarColuna(tabuleiro, indCol)])
    return colunas

def pegarColuna(tabuleiro, indColuna):          # Pegando a coluna por indice
    coluna = []
    for i in range(9):
        coluna.append(tabuleiro[i][indColuna])
    return coluna

def solucionarTabuleiro(tabuleiro):             # função que retorna o tabuleiro solucionado
    linCol = selecionarLinCol(tabuleiro)
    if(linCol[0][1] == linCol[1][1]):
        solucionarLin(tabuleiro, linCol[1][0])
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