"""
Exercício 14 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
pagar.
Imprima os dados do programa com as mensagens adequadas.
Mostrar o peso e multa com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_14_joao_papo_de_pescador
    >>> ex_14_joao_papo_de_pescador.input = lambda k: '62.35'
    >>> ex_14_joao_papo_de_pescador.calcular_peso_excedente_e_multa()
    O peso excedente de peixes é de 12.35 kg
    Por isso, a multa é de R$ 49.40
    >>> ex_14_joao_papo_de_pescador.input = lambda k: '50'
    >>> ex_14_joao_papo_de_pescador.calcular_peso_excedente_e_multa()
    O peso excedente de peixes é de 0.00 kg
    Por isso, a multa é de R$ 0.00

"""


def calcular_peso_excedente_e_multa():
    """Escreva aqui em baixo a sua solução"""

    # Solicita os imputs
    peso_do_peixe = float(input('Digite o peso do peixe:'))

    # calcula o valor da multa
    multa = 4
    peso_excedente = 50
    valor_excedente = (peso_do_peixe - peso_excedente )        #quando eu usava a função round não passava o teste
    valor_da_multa = (valor_excedente * multa)    #quando eu usava a função round não passava o teste

    # Exibição final
    print(f'O peso excedente de peixes é de {valor_excedente:.2f} kg')
    print(f'Por isso, a multa é de R$ {valor_da_multa:.2f}')