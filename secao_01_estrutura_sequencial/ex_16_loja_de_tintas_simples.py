"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00



"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    # Solicita a área a ser pintada em metros quadrados
    area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

    # Define a taxa de cobertura de tinta (1 litro para cada 3 metros quadrados)
    litros_por_metro_quadrado = 1 / 3

    # Calcula a quantidade de litros de tinta necessários
    litros_necessarios = area_a_ser_pintada * litros_por_metro_quadrado

    # Define o tamanho das latas de tinta e o preço por lata
    tamanho_lata = 18  # 18 litros por lata
    preco_lata = 80.00  # Preço por lata

    # Calcula a quantidade de latas necessárias
    quantidade_latas = int(litros_necessarios / tamanho_lata)
    if litros_necessarios % tamanho_lata != 0:
        quantidade_latas += 1

    # Calcula o preço total
    preco_total = quantidade_latas * preco_lata

    # Exibe a quantidade de latas e o preço total
    print(f'Você deve comprar {quantidade_latas} lata(s) tinta ao custo de R$ {preco_total:.2f}')


