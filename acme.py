#!/usr/bin/env python
# coding: utf-8

compressor = False


def reduz_um_grau():
    '''Função do hardware'''


def liga_compressor():
    global compressor
    compressor = True


def refrigera(temp_atual, temp_desejada):
    '''reduz temperatura atual ate temperatura desejada'''

    custo = 0.0
    if not compressor:
        liga_compressor()
        custo += 0.50
    max_temp = temp_desejada + 2
    if temp_atual > max_temp:
        while temp_atual > max_temp:
            reduz_um_grau()
            temp_atual -= 1
            custo += 0.10
    return temp_atual, custo


def simulador(temp_inicial, temp_desejada, delta_temp, tempo):
    '''Simulador simples do ar-condicionado'''
    custo = 0.0
    temp = temp_inicial
    for _ in range(tempo):
        temp, novo_custo = refrigera(temp, temp_desejada)
        custo += novo_custo
        temp += delta_temp
    return custo


if __name__ == '__main__':
    minutos = 360
    print('Ligando ar-condicionado')
    custo = simulador(30, 20, 0.5, minutos)
    print('Total gasto nos %d minutos foram R$ %.2f' % (minutos, custo))
