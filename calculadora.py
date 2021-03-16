def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def divisao (a,b):
    return a / b

def multiplicacao (a,b):
    return a * b

x = int(input("Digite um número: "))
y = int(input("Digite mais um número: "))
op = input("Qual operação deseja fazer? +, -, / ou * ? ")
result = 0

if op == '+':
    result = soma(x,y)
elif op == '-':
    result = subtracao(x,y)
elif op == '/':
    result = divisao(x,y)
elif op == '*':
    result = multiplicacao(x,y)
else:
    print("Por favor digite uma operação válida.")


if result != 0:
    print('O resultado de {} {} {} é {}.'.format(x,op,y,result))