while True:
    num1 = float(input('digite o primeiro número:'))
    op = input('digite a operação matemática a ser feita: ')
    num2 = float(input('digite o segundo número: '))
    
    if op=='+':
        result = num1 + num2
    elif op =='-':
        result = num1 - num2
    elif op =='/':
        result = num1 / num2
    elif op =='*':
        result = num1 * num2
    else: print('operação não reconhecida!')
    print('{} {} {} = {}' .format(num1, op, num2, result))


