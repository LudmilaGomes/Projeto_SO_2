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
  else: # se a referência não está na lista e precisamos realizar uma substituição
    # precisamos incluir essa referência

    contador_subs += 1 # incrementa contador de substituições ocorridas

    # referência é adicionada à página em uma posição que ainda não possui referência (está vazia = None)
    if None in paginas:
      # salva valor da primeira ocorrência da página vazia (ou seja, salva um elemento)
      # where() retorna uma lista com uma lista das posições dessas ocorrências, tipo dos valores etc.
      # por isso, usamos [0][0]
      i_vazio = (np.where(paginas == None))[0][0]
      paginas[i_vazio] = ref
    else: # se as páginas já estão ocupadas (não há página vazia), substituímos uma delas a partir do algoritmo ótimo
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

print('OTM', contador_subs)
