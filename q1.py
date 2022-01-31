#questão 1:  - Qual a cidade de cada estado que possui o maior PIB per capita, no ano de 2018? 
# (Informe a cidade, o estado ao qual ela pertence e o seu PIB per capita).

from asyncore import write

dados_organizados = [] 
dados_questao1 = []

def dataset(file): #organizando o .txt para melhor entendimento.
    arquivo = open(file, 'r', encoding='latin1')
    for linhas in arquivo:
        linhas = linhas.strip() #separar as linhas
        colunas = linhas.split(";") #separar as colunas, de acordo com o doc, com ";"
        dados = (colunas[0], colunas[1], colunas[2],colunas[3],colunas[4], colunas[5],colunas[6], colunas[7], colunas[8], colunas[9])  #>>> para melhor trabalhar com as colunas                 
                 #0 - Ano        #5 - VAB INDUSTRIA
                 #1 - Sigla      #6 - VAB SERVIÇOS
                 #2 - Estado     #7 - VAB ADM
                 #3 - Município  #8 - IMPOSTOS
                 #4 - VAB AGRO   #9 - PIB PER CAPITA
        dados_organizados.append(dados)   
    arquivo.close()
    return dados_organizados

arquivo = dataset(r"C:/Users/dreee/OneDrive/Documents/trainee-desafio/dataset/pib_municipio_2010_a_2018.txt")
ano = input('Escolha um ano para saber quais municípios têm o maior Pib Per Capita por Estado: ') #escolha o ano
qtdline = int(len(dados_organizados)) 
y = 1
z = 0
x = 0
#variáveis de controle

while y < qtdline: #definindo cada dado do nosso "dados organizados"
    if dados_organizados[y][0] == ano:
        dados_organizados.sort() #organizando os resultados
        uf = dados_organizados[y][1] # sigla do estado
        estado = dados_organizados[y][2] #estado
        municipio = dados_organizados[y][3] #cidade
        ppc = float(dados_organizados[y][9]) #valores de pib per capita
        #para organizar só os dados que vamos usar na primeira questão
        if len(dados_questao1) == 0:
            dados_questao1.insert(z,(uf,estado,municipio,ppc))
            z=(len(dados_questao1))-1
        
        if uf == dados_questao1[z][0] and ppc > float(dados_questao1[z][3]):
            dados_questao1.pop(z)
            dados_questao1.insert(z,(uf,estado,municipio,ppc))
            z=(len(dados_questao1))-1

        if uf != dados_questao1[z][0]:
            z=(len(dados_questao1))
            dados_questao1.insert(z, (uf,estado,municipio,ppc))
            z=(len(dados_questao1))-1
        y+=1
    else:
        y+=1

saída = open('C:/Users/dreee/OneDrive/Documents/trainee-desafio/q1/questão_01_saída.txt', 'w') #escrevendo a resposta da questão em um arquivo .txt
i=0
while i < len(dados_questao1):
    saída.write(f'No ano de {ano}, o município {dados_questao1[i][2]}/{dados_questao1[i][0]} teve o maior PIB per capita: R$ {dados_questao1[i][3]}\n')
    i+=1
saída.close()



