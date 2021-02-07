# SOMA
def soma():
    z = float(0)
    w = float(0)
    x = (float(input('Quantos números deseja calcular? ')))
    while z < x:
        y = (float(input('Digite o número: ')))
        w = w + y
        z = z + 1
    print('''
O resultado é:''', w)
    print('')


# SUBTRAÇÃO
def subtracao():
    z = float(0)
    x = (float(input('Quantos números deseja subtrair do valor inicial:  ')))
    w = (float(input('Qual o valor inicial que deseja subtrair: ')))
    while z < x:
        y = (float(input('Digite o número: ')))
        w = w - y
        z = z + 1
    print('''
O resultado é:''', w)
    print('')


# DIVISÃO
def divisao():
    z = float(0)
    x = (float(input('Quantos números deseja dividir do valor inicial:  ')))
    w = (float(input('Qual o valor inicial que deseja dividir: ')))
    while z < x:
        y = (float(input('Digite o número: ')))
        w = w / y
        z = z + 1
    print('''
O resultado é:''', w)
    print('')


# MULTIPLICAÇÃO
def multiplicacao():
    z = float(0)
    w = float(0)
    x = (float(input('Quantos números deseja calcular? ')))
    while z < x:
        y = (float(input('Digite o número: ')))
        w = w * y
        z = z + 1
    print('''
O resultado é:''', w)
    print('')


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
    else:
        print('')
        print('''------------------------
      VÁ À MERDA
 Tente de novo, otário
------------------------''')
        resposta()
        print('')


# FUNÇÃO RAÍZ CALCULADORA
def calculadora():
    rep = 'Sim'
    while rep == 'Sim' or rep == 'sim':
        print('')
        op = int(input('''------------------------
       CALCULADORA
------------------------
Escolha uma opção abaixo
------------------------
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
[5] CANCELAR
------------------------
    '''))
        if op == 1:
            soma()
        elif op == 2:
            subtracao()
        elif op == 3:
            multiplicacao()
        elif op == 4:
            divisao()
        else:
            print('''------------------------
   OPERAÇÃO CANCELADA
------------------------''')
        resposta()


calculadora()