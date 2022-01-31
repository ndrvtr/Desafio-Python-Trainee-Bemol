#- Qual o valor médio do Produto Interno Bruto da cidade de Manaus no período que abrange o dataset?
#(O Produto Interno Bruto consiste na soma dos valores da Agropecuária, Indústria, Serviços, Administração e Impostos).

dados_organizados = [] 
dados_questao2 = []

def dataset(file): #mesma coisa da q1.
    arquivo = open(file, 'r', encoding='latin1')
    for linhas in arquivo:
        linhas = linhas.strip() 
        colunas = linhas.split(";") 
        dados = (colunas[0], colunas[1], colunas[2],colunas[3],colunas[4], colunas[5],colunas[6], colunas[7], colunas[8], colunas[9])
        dados_organizados.append(dados)   
    arquivo.close()
    return dados_organizados

arquivo = dataset(r"./trainee-desafio/dataset/pib_municipio_2010_a_2018.txt")
qtdline = int(len(dados_organizados))
#até aqui também a mesma coisa.

#definiremos nosso input para podermos selecionar qualquer município e intervalo entre anos.
munic = input('Escolha o município: ')
anoc = input('Escolha o ano inicial: ')
anof = input('Escolha o ano final: ')
y = 1
while y < qtdline:                                
    if dados_organizados[y][3] == munic:
        muni = dados_organizados[y][3]
        valor = (float(dados_organizados[y][4])+float(dados_organizados[y][5])+
        float(dados_organizados[y][6])+float(dados_organizados[y][7])+float(dados_organizados[y][8]))
        z= len(dados_questao2)     #0   #1
        dados_questao2.insert(z,(muni,valor))          
        y+=1
    else:
        y+=1 
i = 0
x = 0
while i < len(dados_questao2):
    x+=(dados_questao2[i][1]) #soma dos valores feito aqui ↑↑↑↑↑↑↑↑↑↑
    i+=1

#print(x/(len(dados_questao2)))

saída = open('./trainee-desafio/q2/questão_02_saída.txt', 'w')
saída.write(f'Valor médio do PIB entre {anoc} e {anof}: R$ {x/(len(dados_questao2))}')
saída.close()