# Projeto 2 para a Disciplina de Sistemas Operacionais

Objetivo do Projeto: implementação de algoritmos de substituição de páginas estudados na disciplina para simular o funcionamento destes.
 - FIFO (First In, First Out)
 - OTM (Algoritmo Ótimo)
 - LRU (Least Recently Used ou Menos Recentemente Utilizado)

O programa deverá ler de um arquivo um conjunto de número inteiros onde o primeiro número representa a quantidade de quadros de memória disponíveis na RAM e os demais representam a sequência de referências às páginas, sempre um número por linha. Também deve imprimir na saída o número de faltas de páginas obtido com a utilização de cada um dos algoritmos.

A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória RAM e, em seguida, a sequência de referências à memória.

A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a utilização de cada um deles.

| Entrada                                                                 | Saída                     |
| ----------------------------------------------------------------------- | ------------------------- |
| 4<br>1<br>2<br>3<br>4<br>1<br>2<br>5<br>1<br>2<br>3<br>4<br>5           | FIFO 10<br>OTM 6<br>LRU 8 |
| 3<br>1<br>2<br>3<br>4<br>2<br>1<br>5<br>1<br>2<br>3                     | FIFO 8<br>OTM 6<br>LRU 7  |
| 3<br>1<br>2<br>5<br>2<br>3<br>4<br>7<br>2<br>7<br>4<br>5<br>3<br>5<br>2 | FIFO 9<br>OTM 8<br>LRU 10 |
| 3<br>1<br>2<br>3<br>4<br>5<br>6                                         | FIFO 6<br>OTM 6<br>LRU 6  |
