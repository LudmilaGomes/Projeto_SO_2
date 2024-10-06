import numpy as np

# definição das variáveis usadas
# captura os dados do arquivo
with open('dados.txt') as arquivo:
    seq_referencias = list(int(linha) for linha in arquivo)

# retira o primeiro elemento da lista salva acima (esse valor é referente à quantidade de quadros usada)
quant_quadros = seq_referencias.pop(0)

# a partir da quantidade de quadros, estabelece a lista 'paginas' com tamanho quant_quadros para ser usada
paginas = np.array([None] * quant_quadros)

# igualmente, para cada página existe um contador; a lista representando os contadores é definida abaixo
contador_pag = np.array([0] * quant_quadros)

# contador para a quantidade de substituições de páginas realizadas
contador_subs = 0

# loop para percorrer cada valor de referência
while len(seq_referencias) != 0:
    # retira o primeiro valor da fila de referências para buscá-lo nas páginas na iteração atual
    ref = seq_referencias.pop(0)
    arr_sequencia = np.array(seq_referencias)

    # verifica a presença da referência na lista de páginas
    if ref in paginas:
        # se a referência está dentre as páginas e não precisamos realizar uma substituição
        pass
    else:  # se a referência não está na lista e precisamos realizar uma substituição
        # precisamos incluir essa referência

        contador_subs += 1  # incrementa contador de substituições ocorridas

        # referência é adicionada à página em uma posição que ainda não possui referência (está vazia = None)
        if None in paginas:
            # salva valor da primeira ocorrência da página vazia (ou seja, salva um elemento)
            # where() retorna uma lista com uma lista das posições dessas ocorrências, tipo dos valores etc.
            # por isso, usamos [0][0]
            i_vazio = (np.where(paginas == None))[0][0]
            paginas[i_vazio] = ref
        # se as páginas já estão ocupadas (não há página vazia), substituímos uma delas a partir do algoritmo ótimo
        else:
            # vamos percorrer as páginas
            for i in range(len(paginas)):
                # pag recebe valor da página atual
                pag = paginas[i]
                # where() busca as ocorrências da página atual (pag) na sequência de referências da entrada
                # assim, salvamos a lista de ocorrências (e por isso usamos [0], para acessar o primeiro elemento da tupla retornada)
                prox_ocorr_pag = np.where(arr_sequencia == pag)[0]
                # quando não encontramos a página atual (pag) não ocorre na sequência de referências, o tamanho da lista salva é 0
                if prox_ocorr_pag.size == 0:
                    # e o contador referente a essa página recebe -1
                    contador_pag[i] = -1
                else:
                    # caso contrário, o contador recebe a posição da primeira ocorrência
                    # representa a distância dessa ocorrência para o momento atual em que estamos na sequência de referências
                    contador_pag[i] = prox_ocorr_pag[0]
                    # isso é usado da seguinte forma: achamos a maior distância; a página a ser substituída é a que apresenta essa distância maior

            # se encontra -1, quer dizer que o valor da página não será mais usado pelas entradas da sequência de referências e este é substituído
            if -1 in contador_pag:
                # salva posição no array da página a ser substituída
                pag_subst = np.where(contador_pag == -1)[0][0]
            else:
                # se não encontra -1, busca página que guarda o valor que ocorrerá com maior distância para que este seja substituído
                maior = contador_pag.max()
                # encontra posição do que apresenta maior distância
                pag_subst = np.where(contador_pag == maior)[0][0]
            # realiza a substituição pelo novo valor de referência
            paginas[pag_subst] = ref

    # converte o array numpy em lista do python
    seq_referencias = arr_sequencia.tolist()


# abrindo o arquivo para ler mais uma vez
with open('dados.txt', 'r') as file:
    numeros = file.readlines()

# cada linha do arquivo 'dados.txt' será convertida em um número inteiro e armazenada na lista 'numeros'
numeros = [int(numero.strip()) for numero in numeros]

# o primeiro número da lista 'numeros' representa o tamanho do quadro de páginas na memória
num_quadros = numeros[0]

# 'lista' contém os números restantes (páginas de referência) do arquivo, cada um com o caontador igual a  0
lista = [[numero, 0] for numero in numeros[1:]]

# inicializa a lista 'lista_quadro_atual' com as primeiras páginas (até o tamanho do quadro) e define o valor do quadro para cada página
lista_quadro_atual = lista[:num_quadros]

# 'falta_quadro' armazena a quantidade de vezes que uma página foi substituída no quadro
falta_quadro = num_quadros

# atribuimos um contador para cada página nos quadros iniciais, representando o tempo em que foi carregada na memóri
for i in range(num_quadros):
    lista_quadro_atual[i][1] = i + 1

# remove da lista original as páginas que já estão no quadro
del lista[:num_quadros]

# loop para verificar as páginas restantes da lista
for i in range(len(lista)):

    # caso a página da lista atual (lista[i][0]) não estiver no quadro de páginas
    if lista[i][0] not in [q[0] for q in lista_quadro_atual]:

        # é necessário encontrar a página com o menor valor (ou seja, a mais antiga no quadro)
        menor_valor = min(lista_quadro_atual, key=lambda x: x[1])

        # encontramos a página com o maior valor de tempo de chegada no quadro
        maior_valor = max(lista_quadro_atual, key=lambda x: x[1])

        # atualiza o valor de contagem da nova página com base no maior valor do quadro
        lista[i][1] = maior_valor[1] + 1

        # substitui a página com o menor valor de contagem pela nova página
        index_menor_valor = lista_quadro_atual.index(menor_valor)
        lista_quadro_atual[index_menor_valor] = lista[i]

        # incrementa a contagem de faltas de quadro, pois uma página foi substituída
        falta_quadro += 1
    else:
        # se a página já estiver no quadro, não faz nada
        continue

# Guarda o valor de falta_quadros pois essa variável será reutilizada no próximo algoritmo
quadros_fifo = falta_quadro

# a leitura e organização dos dados nas filas e variáveis segue a mesma lógica do algoritmo FIFO
with open('dados.txt', 'r') as file:
    numeros = file.readlines()


numeros = [int(numero.strip()) for numero in numeros]

num_quadros = numeros[0]

lista = [[numero, 0] for numero in numeros[1:]]

lista_quadro_atual = lista[:num_quadros]

falta_quadro = num_quadros

for i in range(num_quadros):
    lista_quadro_atual[i][1] = i + 1

del lista[:num_quadros]

for i in range(len(lista)):
    if lista[i][0] not in [q[0] for q in lista_quadro_atual]:

        menor_valor = min(lista_quadro_atual, key=lambda x: x[1])

        maior_valor = max(lista_quadro_atual, key=lambda x: x[1])

        lista[i][1] = maior_valor[1] + 1

        index_menor_valor = lista_quadro_atual.index(menor_valor)
        lista_quadro_atual[index_menor_valor] = lista[i]

        falta_quadro += 1
    else:
        # nesse caso caso o quadro já esteja na memória, ao contrário do FIFO, é atualizado o contador
        for q in lista_quadro_atual:
            if q[0] == lista[i][0]:
                # atualiza o tempo de referência para o maior valor atual + 1
                q[1] = max(lista_quadro_atual, key=lambda x: x[1])[1] + 1
                break


print("FIFO", quadros_fifo)

print('OTM', contador_subs)

print("LRU", falta_quadro)
