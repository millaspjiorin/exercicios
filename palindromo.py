# Crie um programa que verifica se uma string é um palíndromo e retorna True ou False.

def palindromo (palavra):
    reverso = palavra[::-1]
    if palavra == reverso:
        return True
    else:
        return False

palavra = input('Por favor digite uma palavra: ')
verifica = palindromo(palavra)

if verifica == True:
    print('A palavra {} é um palíndromo.'.format(palavra))
else:
    print('A palavra {} não é um palíndromo.'.format(palavra))


