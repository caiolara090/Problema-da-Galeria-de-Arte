# Problema-da-Galeria-de-Arte

## Introdução

Esse trabalho tem como objetivo mostrar uma forma de resolver o Problema da Galeria de Arte, um clássico problema da área de Geometria Computacional. Nele, veremos como, a partir de uma planta 2D de uma construção, é possível encontrar o número mínimo de câmeras necessário para cobrir toda a área do local.

## Implementação

Toda a parte de triangulação e a DFS, executados nesse trabalho, estão disponíveis no notebook Colab. Lá há um passo a passo de como foram feita as funções e como é possível executá-las sobre os dados de entrada. Sugere-se usar o arquivo Teste.txt como entrada, fazendo seu upload para o Colab e, em seguida, executar o notebook, uma vez que seus dados já estão no formato correto.

## GitHub Pages

Adicionalmente, foi feita uma página no GitHub Pages para explicar um pouco sobre a teoria de todas as operações feitas com pontos e arestas nesse trabalho, juntamente com algumas ilustrações para facilitar o entendimento do algoritmo. A página está disponível em: https://caiolara090.github.io/Problema-da-Galeria-de-Arte/

## Animação

Caso seja de interesse animar a triangulação e a DFS, é necessário, antes, executar alguns passos:

1 - Certifique-se de ter instalado Python em sua máquina

2 - Instale a biblioteca Manim seguindo o tutorial disponível no link: https://docs.manim.community/en/stable/installation/linux.html

3 - Rode o notebook do Colab disponível nesse projeto com os dados, por exemplo, disponíveis em Teste.txt

4 - Com os arquivos gerados (a saber, pontos.txt, triangulos.txt e cores.txt) no mesmo diretório que animacao.py, rode o programa (manim animacao.py PlotPoints)

5 - Aguarde. Em alguns minutos sua animação será gerada (Se a instância for muito grande e você não quiser esperar muito, digite <manim -pql animacao.py PlotPoints>)
