def converter_string_flutuante(valor):

    valor = valor.replace('(', '').replace(')', '')

    if '.' in valor and ',' in valor:
        valor = float(valor.replace('.', '').replace(',', '.'))
    elif ',' in valor:
        valor = float(valor.replace(',', '.'))
    valor = float(valor)
    return round(valor, 2)


def converter_flutuante_string(valor):
    valor = str(valor).replace('.', ',')
    return valor


if __name__ == '__main__':
    difal = '0,0'

    print(converter_string_flutuante(difal))
