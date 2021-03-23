import Funcoes_areas
# FUNÇÃO CABEÇÁRIO

def cabecario(titulo):
    print('-'*(len(titulo)+2))
    print(titulo.center(len(titulo)+2))
    print('-' * (len(titulo)+2))

# LOOP RESPOSTA

def resposta():
    rep = str(input('Deseja calcular novamente? (Sim/Não) '))
    if rep == 'sim' or rep == 'Sim':
        calculadora()
    elif rep == 'Não' or rep == 'não':
        print('')
        cabecario('OBRIGADO POR USAR')

# CALCULADORA

def calculadora():
    print('')
    op = int(input(f'''{'-' * 24}
       CALCULADORA
{'-' * 24}
Escolha uma opção abaixo
{'-' * 24}
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
{'-' * 24}
    '''))
    if op == 1:
        Funcoes_areas.area_circulo()
    elif op == 2:
        Funcoes_areas.area_triangulo_retangulo()
    elif op == 3:
        Funcoes_areas.area_triangulo_equilátero()
    elif op == 4:
        Funcoes_areas.area_triangulo_isosceles()
    elif op == 5:
        Funcoes_areas.area_quadrado()
    elif op == 6:
        Funcoes_areas.area_retangulo()
    elif op == 7:
        Funcoes_areas.area_losango()
    elif op == 8:
        Funcoes_areas.area_trapezio()
    elif op == 9:
        Funcoes_areas.area_poligono()
    else:
       cabecario('OPERAÇÃO CANCELADA')
    print('')
    resposta()

calculadora()