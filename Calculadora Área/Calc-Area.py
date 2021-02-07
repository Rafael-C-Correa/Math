print('-------------------')
print('CALCULADORA DE AREA')
print('-------------------')
resposta = 'Sim'
while resposta == 'Sim' or resposta == 'sim':
    numero_de_lados = float(input('Quantos lados a figura possui? '))
    while numero_de_lados > 4 or numero_de_lados == 2 or numero_de_lados == 1:
        print(' ')
        print('Esta calaculadora só calcula figuras de 0, 3 ou 4 lados, tente novamente')
        print(' ')
        numero_de_lados = int(input('Quantos lados a figura possui? '))
# AREA DO TRIANGULO
    if numero_de_lados == 3:
        print('Estamos falando de um Triangulo')
        bt = float(input('Diga o valor da base: '))
        ht = float(input('Diga o valor da altura: '))
        area_triangulo = (bt * ht) / 2
        print('A area do Triagulo é: ', area_triangulo)
# AREA DO QUADRADO
    elif numero_de_lados == 4:
        print('Estamos falando de um Quadrilátero')
        bq = float(input('Diga o valor da base: '))
        hq = float(input('Diga o valor da altura: '))
        area_quadrado = bq * hq
        print('A área do quadrado é:', area_quadrado)
# AREA DO CIRCULO
    elif numero_de_lados == 0:
        print('Estamos falando de um Círculo.')
        r = float(input('Diga o valor do Raio: '))
        area_circulo = (r * r) * 3.14
        print('A area do Circulo é:', area_circulo)
    print(' ')
    resposta = str(input('Quer calcular novamente? (Sim/Não): '))
    print(' ')
else:
    print(' ')
    print('--------')
    print('OBRIGADO')
    print('--------')
