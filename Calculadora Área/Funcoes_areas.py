#ÁREA CÍRCULO
def area_circulo():    
    print('Estamos falando de um Círculo.')
    r = float(input('Diga o valor do Raio: '))
    area_circulo = (r ** 2) * 3.14
    print('A area do Circulo é:', area_circulo)

#ÁREA TRIANGULO RETANGULO
def area_triangulo_retangulo():
    print('Área do Triangulo Retagulo: ')
    bt = float(input('Diga o valor da base: '))
    ht = float(input('Diga o valor da altura: '))
    area_triangulo = (bt * ht) / 2
    print('A area do Triagulo Retangulo é: ', area_triangulo)

#ÁREA TRIANGULO EQUILÁTERO
def area_triangulo_equilátero():
    print('Área do Triangulo Equilátero: ')
    lt = float(input('Diga o valor do lado: '))
    import math
    area_triangulo = (math.sqrt(3)/4) * (lt ** 2)
    print('A area do Triagulo Equilátero é: ', area_triangulo)

#ÁREA TRIANGULO ISÓSCELES 
def area_triangulo_isosceles():
    print('Área do Triangulo Isosceles: ')
    lt = float(input('Diga o valor do lado: '))
    ht = float(input('Diga o valor da altura: '))
    area_triangulo = (lt * ht) / 2
    print('A area do Triagulo Isósceles é: ', area_triangulo)

#ÁREA DO QUADRADO EQUILÁTERO
def area_quadrado():
    print('Área do Quadrado Equilátero:')
    lq = float(input('Diga o valor do lado: '))
    area_do_quadrado = lq ** 2
    print('A área do quadrado é:', area_do_quadrado)

#ARÉA DO RETANGULO
def area_retangulo():
    print('Área do Retângulo:')
    bq = float(input('Diga o valor da base: '))
    hq = float(input('Diga o valor da altura: '))
    area_do_retangulo = bq * hq
    print('A área do quadrado é:', area_do_retangulo)

#ÁREA DO LOSANGO
def area_losango():
    print('Área do Losango:')
    Dl = float(input('Diga o valor da diagonal maior: '))
    dl = float(input('Diga o valor da diagonal menor: '))
    area_do_losango = (Dl * dl) / 2
    print('A área do losango é:', area_do_losango)

#ÁREA DO TRAPÉZIO
def area_trapezio():
    print('Área do Trapézio: ')
    Bt = float(input('Diga o valor da base maior: '))
    bt = float(input('Diga o valor da base menor: '))
    ht = float(input('Diga o valor da altura: '))
    area_do_trapezio = ((Bt + bt) / 2) * ht
    print('A area do Trapézio é: ', area_do_trapezio)

#ÁREA DE DO POLÍGONO
def area_poligono():
    print('Área do polígono: ')
    ap = float(input('Diga o valor do apótema: '))
    pp = float(input('Diga o valor do semiperímetro: '))
    area_do_poligono = (ap * pp) / 2
    print('A area do Trapézio é: ', area_do_poligono)

#--------------------------------------------------------------------------------#



