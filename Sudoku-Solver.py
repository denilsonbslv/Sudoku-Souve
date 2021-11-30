# Função para criar o tabuleiro com as linhas
def criarTabuleiro(linhas):
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
    # Pegando os valores das linhas e adiconando ao tabuleiro
    for i in range(9):
        j = 0
        for num in linhas[i]:
            tabuleiro[i][j] = num
            j += 1
    # Aqui retorno o tabuleiro para ser resolvido
    return(tabuleiro)

# Função para pegar a linha com menos zero
def selecionarCol(tabuleiro):
    qtdZeroCol = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        for j in range(9):
            if(tabuleiro[i][j] == "0"):
                qtdZeroCol[i] += 1

    minVlr = 9
    for vlr in qtdZeroCol:
        if vlr < minVlr and vlr != 0:
            minVlr = vlr
    
    if qtdZeroCol.count('0') == 9:
        return [0]
    
    return [qtdZeroCol.index(minVlr), minVlr]

# Função para pegar a coluna com menos zero
def selecionarLin(tabuleiro):
    qtdZeroLin = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        for j in range(9):
            if(tabuleiro[i][j] == "0"):
                qtdZeroLin[i] += 1

    minVlr = 9
    for vlr in qtdZeroLin:
        if vlr < minVlr and vlr != 0:
            minVlr = vlr
    
    if qtdZeroLin.count('0') == 9:
        return [0]

    return [qtdZeroLin.index(minVlr), minVlr]

# Função para pegar uma coluna pelo seu indice
def pegarColuna(tabuleiro, indColuna):
    coluna = []
    for i in range(9):
        coluna.append(tabuleiro[i][indColuna])
    return coluna

# Função para pegar colunas pelos indices
def pegarColunas(tabuleiro, indZerados):
    colunas = []
    for indCol in indZerados:
        colunas.append([[indCol],pegarColuna(tabuleiro, indCol)])
    return colunas

# Função para pegar a coluna com menos zeros
def pegarColunaMenosZero(colunas):
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
    return colunas[colMinZeros]

# Função para pegar o quadrado referente a linha e a coluna
def pegarQuadrado(tabuleiro, indLinha, indColuna):
    quadrado = []
    if (indLinha >= 0 and indLinha <= 2):
        if (indColuna >= 0 and indColuna <= 2):
            for i in range(0, 3):
                for j in range(0, 3):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 3 and indColuna <= 5):
            for i in range(0, 3):
                for j in range(3, 6):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 6 and indColuna <= 8):
            for i in range(0, 3):
                for j in range(6, 9):
                    quadrado.append(tabuleiro[i][j])
        else:
            print("Não foi possivel definir quadrado >coluna<")
    elif (indLinha >= 3 and indLinha <= 5):
        if (indColuna >= 0 and indColuna <= 2):
            for i in range(3, 6):
                for j in range(0, 3):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 3 and indColuna <= 5):
            for i in range(3, 6):
                for j in range(3, 6):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 6 and indColuna <= 8):
            for i in range(3, 6):
                for j in range(6, 9):
                    quadrado.append(tabuleiro[i][j])
        else:
            print("Não foi possivel definir quadrado >coluna<")
    elif (indLinha >= 6 and indLinha <= 8):
        if (indColuna >= 0 and indColuna <= 2):
            for i in range(6, 9):
                for j in range(0, 3):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 3 and indColuna <= 5):
            for i in range(6, 9):
                for j in range(3, 6):
                    quadrado.append(tabuleiro[i][j])
        elif (indColuna >= 6 and indColuna <= 8):
            for i in range(6, 9):
                for j in range(6, 9):
                    quadrado.append(tabuleiro[i][j])
        else:
            print("Não foi possivel definir quadrado >coluna<")
    else:
        print("Não foi possivel definir quadrado >lina<")

    return quadrado;

# Função para pegar os valores faltantes em comum entre a linha coluna e o quadrado
def pegarvaloresFaltantes(linha, coluna, quadrado):
    vlrComuns = []
    if len(linha) > len(coluna) and len(linha) > len(quadrado): # Caso a linha seja quem tenha mais valores faltantes
        if len(coluna) > len(quadrado): # Caso a coluna tenha mais valores faltantes que o quadrado
            for vlrQ in quadrado:
                for i in range(len(coluna)):
                    for j in range(len(linha)):
                        if vlrQ == coluna[i] and vlrQ == linha[j] :
                            vlrComuns.append(vlrQ)
                            continue 
        else:                           # Caso a quadrado tenha mais valores faltantes que o coluna
            for vlrC in coluna:
                for i in range(len(quadrado)):
                    for j in range(len(linha)):
                        if vlrC == quadrado[i] and vlrC == linha[j]:
                            vlrComuns.append(vlrC)
                            continue
    elif len(coluna) > len(linha) and len(coluna) > len(quadrado): # Caso a coluna seja quem tenha mais valores faltantes
        if len(linha) > len(quadrado):  # Caso a linha tenha mais valores faltantes que o quadrado
            for vlrQ in quadrado:
                for i in range(len(linha)):
                    for j in range(len(coluna)):
                        if vlrQ == linha[i] and vlrQ == coluna[j]:
                            vlrComuns.append(vlrQ)
                            continue 
        else:                           # Caso a quadrado tenha mais valores faltantes que o linha
            for vlrL in linha:
                for i in range(len(quadrado)):
                    for j in range(len(coluna)):
                        if vlrL == coluna[j] and vlrL == quadrado[i]:
                            vlrComuns.append(vlrL)
                            continue
    else:                                                          # Caso a quadrado seja quem tenha mais valores faltantes
        if len(linha) > len(coluna):    # Caso a linha tenha mais valores faltantes que a coluna
            for vlrC in coluna:
                for i in range(len(linha)):
                    for j in range(len(quadrado)):
                        if vlrC == linha[i] and vlrC == quadrado[j]:
                            vlrComuns.append(vlrC)
                            continue
        else:                           # Caso a coluna tenha mais valores faltantes que a linha
            for vlrL in linha:
                for i in range(len(coluna)):
                    for j in range(len(quadrado)):
                        if vlrL == coluna[i] and vlrL == quadrado[j]:
                            vlrComuns.append(vlrL)
                            continue
    return vlrComuns

# Pegar quantas vezes o valor se repete no tabuleiro
def pegarValorCorreto(tabuleiro, colunas, valoresFaltantes):
    recorrenciaColunas = []
    for i in range(len(valoresFaltantes)):
        cont = 0
        for j in range(len(colunas)):
            if colunas[j][1].count(str(valoresFaltantes[i])) == 1:
                cont+=1
        recorrenciaColunas.append(cont)

    recorrenciaTabuleiro = []
    for vlr in valoresFaltantes:
        contadorRec = 0
        for i in range(9):
            if tabuleiro[i].count(str(vlr)) == 1:
                contadorRec+=1
        recorrenciaTabuleiro.append(contadorRec)
    
    maiorRecCol = max(recorrenciaColunas)
    menorRecTab = min(recorrenciaTabuleiro)

    colMaior = 0
    tabMaior = 0

    for i in range(len(valoresFaltantes)):
        if(recorrenciaColunas[i] > recorrenciaTabuleiro[i]):
            colMaior += 1
        if(recorrenciaColunas[i] < recorrenciaTabuleiro[i]):
            tabMaior += 1
            
    if colMaior > tabMaior:
        return valoresFaltantes[recorrenciaColunas.index(maiorRecCol)] 
    elif tabMaior > colMaior:
        return valoresFaltantes[recorrenciaTabuleiro.index(menorRecTab)] 
    else:
        return valoresFaltantes[0] 

# Função para solucionar uma linha
def solucionarLin(tabuleiro, indiceLinha):
    indiceLinha = int(indiceLinha[0])
    indicesZeradosLin = []
    numerosFaltantesLin = []
    linha = tabuleiro[indiceLinha]

    # Pegar os indices zerados da linha e os valores faltantes
    for i in range(9):
        if(linha[i] == '0'):
            indicesZeradosLin.append(i)
        if(linha.count(str(i+1)) == 0):
            numerosFaltantesLin.append(i+1)
    
    indicesZeradosCol = []
    numerosFaltantesCol = []
    colunas = pegarColunas(tabuleiro, indicesZeradosLin)
    coluna = pegarColunaMenosZero(colunas)
    indiceColuna = int(coluna[0][0])
    coluna = coluna[1]

    # Pegar os indices zerados da coluna e os valores faltantes
    for i in range(9):
        if(coluna[i] == '0'):
            indicesZeradosCol.append(i)
        if(coluna.count(str(i+1)) == 0):
            numerosFaltantesCol.append(i+1)
    
    # Pegar quadrado referente a intersecção da linha e da coluna
    indicesZeradosQua = []
    numerosFaltantesQua = []
    quadrado = pegarQuadrado(tabuleiro, indiceLinha, indiceColuna)

    # Pegar os indices zerados do quadrado e os valores faltantes
    for i in range(9):
        if(quadrado[i] == '0'):
            indicesZeradosQua.append(i)
        if(quadrado.count(str(i+1)) == 0):
            numerosFaltantesQua.append(i+1)

    valoresComunsFaltantes =  pegarvaloresFaltantes(numerosFaltantesLin, numerosFaltantesCol, numerosFaltantesQua)

    if len(valoresComunsFaltantes) == 1:
        tabuleiro[indiceLinha][indiceColuna] = str(valoresComunsFaltantes[0])
    else:

        VlrMenosRecorre = pegarValorCorreto(tabuleiro, colunas, valoresComunsFaltantes)
        
        tabuleiro[indiceLinha][indiceColuna] = str(VlrMenosRecorre)

    return tabuleiro
    

# Função para solucionar uma coluna
def solucionarCol(tabuleiro, colMenosZero):
    print()


def resolverSudoku(tabuleiro):                                          # Função para solucionar sudoku
    linMenosZero = selecionarLin(tabuleiro)
    colMenosZero = selecionarCol(tabuleiro)

    if linMenosZero[1] > colMenosZero[1]:
        tabuleiro = solucionarLin(tabuleiro, linMenosZero)
    elif colMenosZero[1] > linMenosZero[1]:
        tabuleiro = solucionarCol(tabuleiro, colMenosZero)
    else:
        tabuleiro = solucionarLin(tabuleiro, linMenosZero)

    if len(linMenosZero) == 1 and len(colMenosZero) == 1:
        return tabuleiro

    return resolverSudoku(tabuleiro)

linhas = ["120070560","507932080","000001000","010240050","308000402","070085010","000700000","080423701","034010028"]

tabuleiro = criarTabuleiro(linhas)

print(tabuleiro)

tabuleiro = resolverSudoku(tabuleiro)

print(tabuleiro)