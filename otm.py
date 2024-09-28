import numpy as np

# definição das variáveis usadas

# funciona
# testar com mais entradas!
# comentar

# 
with open('dados.txt') as arquivo:
  seq_referencias = list(int(linha) for linha in arquivo)

# 
quant_quadros = seq_referencias.pop(0)

# 
paginas = np.array([None] * quant_quadros)

# 
contador_pag = np.array([0] * quant_quadros)

# 
contador_subs = 0

# print(quant_quadros)
# print(seq_referencias)
# print(paginas)
# print(contador_pag)
# print(contador_subs)

# loop para percorrer cada valor de referência
while len(seq_referencias) != 0:
  # 
  ref = seq_referencias.pop(0)
  arr_sequencia = np.array(seq_referencias)
  # print('ref:', ref)
  # print('seq_referencias antes das mudanças', seq_referencias)
  # print('paginas antes das mudanças', paginas)
  # se a referência está na lista de páginas
  if ref in paginas:
    # print('passou!')
    pass
  else: # se a referência não está na lista
    # precisamos incluir essa referência

    contador_subs += 1

    # referência é adicionada à página em uma posição que ainda não possui referência (está vazia = None)
    if None in paginas:
      i_vazio = (np.where(paginas == None))[0][0]
      paginas[i_vazio] = ref
    else: # se as páginas já estão ocupadas, substituímos uma delas a partir do algoritmo ótimo
      # 
      arr_sequencia = np.array(seq_referencias)
      # print('arr_sequencia', arr_sequencia)
      # print('paginas', paginas)
      for i in range(len(paginas)):
        pag = paginas[i]
        # print('minha pag', pag)
        prox_ocorr_pag = np.where(arr_sequencia == pag)[0]
        # print('prox_ocorr_pag', prox_ocorr_pag)
        if prox_ocorr_pag.size == 0:
          # print('prox_ocorr_pag SIZE É 0', prox_ocorr_pag)
          contador_pag[i] = -1
        else: 
          # print('prox_ocorr_pag SIZE NÃO É 0', prox_ocorr_pag)
          contador_pag[i] = prox_ocorr_pag[0]

      if -1 in contador_pag:
        pag_subst = np.where(contador_pag == -1)[0][0]
        # print('pag_subst HELP1', pag_subst)
      else:
        maior = contador_pag.max()
        pag_subst = np.where(contador_pag == maior)[0][0]
        # print('pag_subst HELP2', pag_subst)
      paginas[pag_subst] = ref

  seq_referencias = arr_sequencia.tolist()
  # print('seq_referencias depois das mudanças', seq_referencias)
  # print('paginas depois das mudanças', paginas)
  # print()

print('OTM', contador_subs)
