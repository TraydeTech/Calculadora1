# Calculadora
# Jefferson Trayde


print('=======================================')
print('=           Seja Bem vindo            =')
print('=     A minha primeira Calculadora    =')
print('=======================================')

def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria:
+ SOMA
- SUBTRAÇÃO
* MUTIPLICAÇÃO
/ DIVISÃO
''')

    number_1 = int(input('Por favor, digite o primeiro número: '))
    number_2 = int(input('Por favor, digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')


    again()

def again():
    calc_again = input('''
Deseja calcular novamente?
Por favor digite S para Sim ou N pare Não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

calculate()