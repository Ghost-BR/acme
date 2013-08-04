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
    minimal_temp = temp_desejada - 2
    if temp_atual > max_temp:
        while temp_atual > minimal_temp:
            reduz_um_grau()
            temp_atual -= 1
            custo += 0.10
    return custo
