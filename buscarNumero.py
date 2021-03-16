'''
Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado. 
O programa deve retornar o índice onde o valor foi encontrado, ou informar caso não encontre o valor.
'''


from random import randint

numeros = []

while len(numeros) < 5:
    sorteado = randint(1,10)
    if sorteado not in numeros:
        numeros.append(sorteado)

num_escolhido = int(input('Digite um número de 1 a 10: '))

if num_escolhido in numeros:
    posicao = numeros.index(num_escolhido)
    print('O número {} é o {} da lista. '.format(num_escolhido, posicao + 1))
else:
    print('O número escolhido não faz parte da lista, apenas os números: {}'.format(numeros))


