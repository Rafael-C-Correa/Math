# LOOP RESPOSTA
def resposta():
    rep = str(input('Deseja calcular novamente? (Sim/Não) '))
    if rep == 'sim' or rep == 'Sim':
        calculadora()
    elif rep == 'Não' or rep == 'não':
        print('')
        print('''------------------------
    OBRIGADO POR USAR
------------------------''')

# CALCULADORA
def calculadora():
    print('')
    op = int(input('''------------------------
       CALCULADORA
------------------------
Escolha uma opção abaixo
------------------------
[1] CÍRCULO
[2] TRIANGULO RETANGULO
[3] TRIANGULO EQUILÁTERO
[4] TRIANGULO ISÓSCELES 
[5] QUADRADO EQUILÁTERO
[6] RETANGULO
[7] LOSANGO
[8] TRAPÉZIO
[9] POLÍGONO
[10] CANCELAR
------------------------
    '''))
    if op == 1:
        from Funcoes_areas import area_circulo
        area_circulo()
    elif op == 2:
        from Funcoes_areas import area_triangulo_retangulo
        area_triangulo_retangulo()
    elif op == 3:
        from Funcoes_areas import area_triangulo_equilátero
        area_triangulo_equilátero()
    elif op == 4:
        from Funcoes_areas import area_triangulo_isosceles
        area_triangulo_isosceles()
    elif op == 5:
        from Funcoes_areas import area_quadrado
        area_quadrado()
    elif op == 6:
        from Funcoes_areas import area_retangulo
        area_retangulo()
    elif op == 7:
        from Funcoes_areas import area_losango
        area_losango()
    elif op == 8:
        from Funcoes_areas import area_trapezio
        area_trapezio()
    elif op == 9:
        from Funcoes_areas import area_poligono
        area_poligono()
    else:
       print('''------------------------
   OPERAÇÃO CANCELADA
------------------------''') 
    print('')
    resposta()
calculadora()