def comoSeLivrarDeZerosNaDiagonal(m):
    perms = permutacoes(list(range(len(m))))

    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(m, perms[i], perms[j]):
                return [perms[i], perms[j]];


def haZeroNaDiagonal(m):
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0: qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0


def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1


matriz = [[2, 3, 0, 28], \
          [4, 2, 0, 24], \
          [3, 2, 0, 16]]

poeUmNaDiagonalPrincipalNaLinha(1, matriz)
print(matriz)
# print (haZeroNaDiagonal(matriz))


def haZeroNaDiagonal(m):
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0: qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0


def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1


matriz = [[2, 3, 5, 1], \
          [9, 2, 6, 7], \
          [3, 6, 2, 9]]

poeUmNaDiagonalPrincipalNaLinha(1, matriz)
#print(matriz)
# print (haZeroNaDiagonal(matriz))
matriz = len(matriz)
numlinha = 0
while numlinha > 0:
    numlinha = numlinha - 1
    numlinha = len(matriz)

lin = 0
while lin <= 3:
    col = 0
    while col <= 4:
        print(lin, col, )
        #m[lin][col]=0 torna tudo 0
        col += 1
    lin += 1


matriz = [[2, 3, 5, 1], \
          [9,7, 6, 7], \
          [3, 6, 2, 9]]
lin1 = 0
while lin1 <= len(matriz):
    lin2 = lin1 + 1
    while lin2 <= len(matriz):
        print(lin1, lin2)
        #if dentdigualQdodividir(lin1,lin2):print('sistema impossivel')
        lin2 += 1
    lin1 += 1


# função que calcula o determinante de uma matriz
def determinante():
    # Recebe a ordem da matriz
    qtd = int(input('Informe o ordem da matriz: '))

    # Inicializa a matriz, ainda com 'lixo de endereços de memória' nele
    matriz = np.empty([qtd, qtd], dtype=float)
    print('\n')

    # Adiciona elementos na matriz
    for i in range(0, qtd):
        for j in range(0, qtd):
            matriz[i][j] = float(input('Digite [{}][{}] da matriz: '.format(i + 1, j + 1)))

    # Imprime a matriz
    print('\nA matriz é:\n', matriz)

    # a variável 'determinante' recebe o determinante da matriz
    determinante = np.linalg.det(matriz)

    # Imprime o determinante
    print('\nO determinante da matriz é: {:.2f}.'.format(determinante))

    # função não retorna nada
    return None

'''def ColocaumnaPrincipal (linha, m):

    divisor = m[linha][linha]
    for colu in range(len(m)+1):
        #Linha linha da matriz sendo dividida
        m[linha][colu] /= divisor

def SubTrailinha(coluna, m, linha):

    #Pega o multiplicador para zerar
    const = m[linha][coluna]
    for coluna1 in range(len(m[coluna])):
        #Subtrai um termo
        m[linha][coluna1] -= (m[coluna][coluna1])


    def carregaMatriz(nomeArq):

        arq = open(nomeArq, "r")
        qtdLins = int(arq.readline())
        ret = []
        for lin in range(qtdLins):
            texto = arq.readline().split()
            linha = []
            for col in range(qtdLins + 1): linha.append(float(texto[col]))
            ret.append(linha)
        arq.close()
        return ret

    def permuta(linha, perm, perms):
        if linha == []:
            perms.append(perm)
        else:
            for lin in range(len(linha)):
                permuta(linha[0:lin] + linha[lin + 1:len(linha)], perm + [linha[lin]], perms)

    def permutacoes(linha):

        perms = []
        permuta(linha, [], perms)
        return perms

    def combinacoesDeLinhas2a2(m):

        ret = []
        for lin in range(len(m)):
            for col in range(lin + 1, len(m)):
                ret.append([lin, col])
        return ret

    def haZeroNaDiagonal(m, ordL, ordC):

        qtdDeZeros = 0
        posicao = 0
        while posicao < len(m):
            if m[ordL[posicao]][ordC[posicao]] == 0: qtdDeZeros += 1
            posicao += 1
        return qtdDeZeros > 0

    def comoSeLivrarDeZerosNaDiagonal(m):

        perms = permutacoes(list(range(len(m))))
        for i in range(len(perms)):
            for j in range(len(perms)):
                if not haZeroNaDiagonal(m, perms[i], perms[j]):
                    return [perms[i], perms[j]];
        return None

    print(comoSeLivrarDeZerosNaDiagonal(matriz))
    print(combinacoesDeLinhas2a2(matriz))

matriz = [[3,3,5,1], \
          [9,4,6,7],  \
          [3,6,4,9]]
linhas = len(matriz)

for linha in range(linhas):

    ColocaumnaPrincipal(linha,matriz)
    for subtrai in range(linhas):
        if linha != subtrai:
            SubTrailinha(linha, matriz, subtrai)

print(matriz)
for subtrai2 in range(linhas):

    print(f'A variável {subtrai2 + 1} é igual á: {matriz[subtrai2][linhas]}')
'''