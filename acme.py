#!/usr/bin/env python
# coding: utf-8

compressor = False


def reduz_um_grau():
    pass


def refrigera(temp_atual, temp_desejada):
    global compressor

    custo = 0.0
    if not compressor:
        compressor = True
        custo += 0.50
    max_temp = temp_desejada + 2
    if temp_atual > max_temp:
        while temp_atual > max_temp:
            reduz_um_grau()
            temp_atual -= 1
            custo += 0.10
    return temp_atual, custo


def simulador(temp_inicial, temp_desejada, delta_temp, tempo):
    custo = 0.0
    temp = temp_inicial
    print('Temperatura atual {} C'.format(temp))
    print('Ligando ar-condicionado')
    for i in range(tempo):
        temp, new_custo = refrigera(temp, temp_desejada)
        print('Temperatura apos refrigera {} C'.format(temp))
        custo += new_custo
        print('Passaram {} minutos'. format(i))
        temp += delta_temp
        print('Temperatura subil {} C, {:.2f} C'.format(delta_temp, temp))
    return custo


if __name__ == '__main__':
    minutos = 360
    custo = simulador(30, 20, 0.5, minutos)
    print('Total gasto nos {} minutos foram ${:.2f}'.format(minutos, custo))
