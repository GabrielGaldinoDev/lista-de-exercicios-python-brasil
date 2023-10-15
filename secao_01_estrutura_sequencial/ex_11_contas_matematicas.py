"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    # Solicita dois números inteiros e um número real ao usuário
    numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
    numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
    numero_real = float(input("Digite um número real: "))

    # Realiza os cálculos
    resultado1 = round((2 * numero_inteiro1) * (numero_inteiro2 / 2), 2)
    resultado2 = round((3 * numero_inteiro1) + numero_real, 2)
    resultado3 = round(numero_real ** 3, 2)

    # Exibe os resultados com duas casas decimais
    print(f'O produto do dobro do primeiro com metade do segundo é {resultado1:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {resultado2:.2f}')
    print(f'O terceiro elevado ao cubo é {resultado3:.2f}')



